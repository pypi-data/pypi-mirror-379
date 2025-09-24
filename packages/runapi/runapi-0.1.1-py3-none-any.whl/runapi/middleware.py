import time
import json
import logging
from typing import Callable, Dict, Any, List, Optional
from fastapi import Request, Response, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.middleware.cors import CORSMiddleware as FastAPICORSMiddleware
from fastapi.responses import JSONResponse
from collections import defaultdict
import asyncio


class RunApiMiddleware(BaseHTTPMiddleware):
    """Base middleware class for RunApi framework."""
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        """Override this method in subclasses."""
        return await call_next(request)


class RequestLoggingMiddleware(RunApiMiddleware):
    """Middleware for logging HTTP requests and responses."""
    
    def __init__(self, app, logger: Optional[logging.Logger] = None):
        super().__init__(app)
        self.logger = logger or logging.getLogger(__name__)
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        start_time = time.time()
        
        # Log request
        self.logger.info(f"Request: {request.method} {request.url}")
        
        response = await call_next(request)
        
        # Calculate processing time
        process_time = time.time() - start_time
        
        # Log response
        self.logger.info(
            f"Response: {response.status_code} - "
            f"Time: {process_time:.4f}s - "
            f"Size: {response.headers.get('content-length', 'unknown')}"
        )
        
        response.headers["X-Process-Time"] = str(process_time)
        return response


class RateLimitMiddleware(RunApiMiddleware):
    """Rate limiting middleware using in-memory storage."""
    
    def __init__(
        self, 
        app,
        calls: int = 100,
        period: int = 60,  # seconds
        key_func: Optional[Callable[[Request], str]] = None
    ):
        super().__init__(app)
        self.calls = calls
        self.period = period
        self.key_func = key_func or self._default_key_func
        self.requests: Dict[str, List[float]] = defaultdict(list)
        self.lock = asyncio.Lock()
    
    def _default_key_func(self, request: Request) -> str:
        """Default key function using client IP."""
        forwarded = request.headers.get("X-Forwarded-For")
        if forwarded:
            return forwarded.split(",")[0].strip()
        return request.client.host if request.client else "unknown"
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        key = self.key_func(request)
        current_time = time.time()
        
        async with self.lock:
            # Clean old requests
            self.requests[key] = [
                req_time for req_time in self.requests[key]
                if current_time - req_time < self.period
            ]
            
            # Check rate limit
            if len(self.requests[key]) >= self.calls:
                return JSONResponse(
                    status_code=429,
                    content={
                        "error": "Rate limit exceeded",
                        "message": f"Maximum {self.calls} requests per {self.period} seconds"
                    },
                    headers={"Retry-After": str(self.period)}
                )
            
            # Record this request
            self.requests[key].append(current_time)
        
        response = await call_next(request)
        
        # Add rate limit headers
        response.headers["X-RateLimit-Limit"] = str(self.calls)
        response.headers["X-RateLimit-Remaining"] = str(
            max(0, self.calls - len(self.requests[key]))
        )
        response.headers["X-RateLimit-Reset"] = str(
            int(current_time + self.period)
        )
        
        return response


class AuthMiddleware(RunApiMiddleware):
    """JWT-based authentication middleware."""
    
    def __init__(
        self,
        app,
        secret_key: str,
        algorithm: str = "HS256",
        protected_paths: Optional[List[str]] = None,
        excluded_paths: Optional[List[str]] = None,
        header_name: str = "Authorization",
        token_prefix: str = "Bearer "
    ):
        super().__init__(app)
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.protected_paths = protected_paths or []
        self.excluded_paths = excluded_paths or ["/docs", "/redoc", "/openapi.json"]
        self.header_name = header_name
        self.token_prefix = token_prefix
    
    def _is_protected_path(self, path: str) -> bool:
        """Check if path requires authentication."""
        # If no protected paths specified, protect all except excluded
        if not self.protected_paths:
            return path not in self.excluded_paths
        
        # Check if path matches any protected pattern
        for pattern in self.protected_paths:
            if path.startswith(pattern):
                return True
        return False
    
    def _extract_token(self, request: Request) -> Optional[str]:
        """Extract JWT token from request headers."""
        auth_header = request.headers.get(self.header_name)
        if not auth_header or not auth_header.startswith(self.token_prefix):
            return None
        
        return auth_header[len(self.token_prefix):].strip()
    
    def _verify_token(self, token: str) -> Optional[Dict[str, Any]]:
        """Verify JWT token and return payload."""
        try:
            # Note: In real implementation, you'd use python-jose or similar
            # This is a simplified version
            import base64
            import hmac
            import hashlib
            
            parts = token.split('.')
            if len(parts) != 3:
                return None
            
            header, payload, signature = parts
            
            # Verify signature (simplified)
            expected_sig = base64.urlsafe_b64encode(
                hmac.new(
                    self.secret_key.encode(),
                    f"{header}.{payload}".encode(),
                    hashlib.sha256
                ).digest()
            ).decode().rstrip('=')
            
            if not hmac.compare_digest(signature, expected_sig):
                return None
            
            # Decode payload
            payload_data = json.loads(
                base64.urlsafe_b64decode(payload + '==')
            )
            
            # Check expiration
            if 'exp' in payload_data and payload_data['exp'] < time.time():
                return None
            
            return payload_data
            
        except Exception:
            return None
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        path = request.url.path
        
        # Skip authentication for excluded paths
        if not self._is_protected_path(path):
            return await call_next(request)
        
        # Extract and verify token
        token = self._extract_token(request)
        if not token:
            return JSONResponse(
                status_code=401,
                content={"error": "Authentication required", "message": "Missing or invalid token"}
            )
        
        payload = self._verify_token(token)
        if not payload:
            return JSONResponse(
                status_code=401,
                content={"error": "Authentication failed", "message": "Invalid or expired token"}
            )
        
        # Add user info to request state
        request.state.user = payload
        
        return await call_next(request)


class SecurityHeadersMiddleware(RunApiMiddleware):
    """Add security headers to responses."""
    
    def __init__(
        self,
        app,
        include_server: bool = False,
        csp_policy: Optional[str] = None,
        hsts_max_age: int = 31536000  # 1 year
    ):
        super().__init__(app)
        self.include_server = include_server
        self.csp_policy = csp_policy
        self.hsts_max_age = hsts_max_age
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        response = await call_next(request)
        
        # Remove server header if requested
        if not self.include_server:
            if "Server" in response.headers:
                del response.headers["Server"]
        
        # Add security headers
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        
        # Add HSTS header for HTTPS
        if request.url.scheme == "https":
            response.headers["Strict-Transport-Security"] = f"max-age={self.hsts_max_age}; includeSubDomains"
        
        # Add CSP header if policy is defined
        if self.csp_policy:
            response.headers["Content-Security-Policy"] = self.csp_policy
        
        return response


class CompressionMiddleware(RunApiMiddleware):
    """Simple compression middleware for JSON responses."""
    
    def __init__(self, app, minimum_size: int = 1000):
        super().__init__(app)
        self.minimum_size = minimum_size
    
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        response = await call_next(request)
        
        # Check if client accepts compression
        accept_encoding = request.headers.get("Accept-Encoding", "")
        if "gzip" not in accept_encoding.lower():
            return response
        
        # Check content type and size
        content_type = response.headers.get("Content-Type", "")
        if not (content_type.startswith("application/json") or content_type.startswith("text/")):
            return response
        
        # Get response body
        body = b""
        async for chunk in response.body_iterator:
            body += chunk
        
        if len(body) < self.minimum_size:
            return Response(
                content=body,
                status_code=response.status_code,
                headers=dict(response.headers),
                media_type=response.media_type
            )
        
        # Compress with gzip
        import gzip
        compressed_body = gzip.compress(body)
        
        # Create new response with compressed content
        new_response = Response(
            content=compressed_body,
            status_code=response.status_code,
            headers=dict(response.headers),
            media_type=response.media_type
        )
        
        new_response.headers["Content-Encoding"] = "gzip"
        new_response.headers["Content-Length"] = str(len(compressed_body))
        
        return new_response


class CORSMiddleware:
    """CORS middleware wrapper for FastAPI's CORS middleware."""
    
    def __init__(
        self,
        allow_origins: List[str] = None,
        allow_credentials: bool = False,
        allow_methods: List[str] = None,
        allow_headers: List[str] = None,
        expose_headers: List[str] = None,
        max_age: int = 600
    ):
        self.allow_origins = allow_origins or ["*"]
        self.allow_credentials = allow_credentials
        self.allow_methods = allow_methods or ["*"]
        self.allow_headers = allow_headers or ["*"]
        self.expose_headers = expose_headers or []
        self.max_age = max_age
    
    def get_middleware(self):
        """Get FastAPI CORS middleware instance."""
        return FastAPICORSMiddleware(
            allow_origins=self.allow_origins,
            allow_credentials=self.allow_credentials,
            allow_methods=self.allow_methods,
            allow_headers=self.allow_headers,
            expose_headers=self.expose_headers,
            max_age=self.max_age
        )


# Convenience functions
def create_rate_limit_middleware(app, calls: int = 100, period: int = 60):
    """Create rate limiting middleware."""
    return RateLimitMiddleware(app, calls=calls, period=period)


def create_auth_middleware(
    app, 
    secret_key: str,
    protected_paths: List[str] = None,
    excluded_paths: List[str] = None
):
    """Create authentication middleware."""
    return AuthMiddleware(
        app,
        secret_key=secret_key,
        protected_paths=protected_paths,
        excluded_paths=excluded_paths
    )


def create_logging_middleware(app, logger: logging.Logger = None):
    """Create request logging middleware."""
    return RequestLoggingMiddleware(app, logger=logger)


def create_security_middleware(
    app,
    include_server: bool = False,
    csp_policy: str = None,
    hsts_max_age: int = 31536000
):
    """Create security headers middleware."""
    return SecurityHeadersMiddleware(
        app,
        include_server=include_server,
        csp_policy=csp_policy,
        hsts_max_age=hsts_max_age
    )