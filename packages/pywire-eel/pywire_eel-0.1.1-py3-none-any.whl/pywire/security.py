"""
Simplified security configuration for PyWire.
"""

import re
from typing import Dict, Any, List


class InputValidator:
    """Basic input validation."""

    def __init__(self):
        pass

    def validate_function_name(self, func_name: str) -> bool:
        """Validate function name to prevent malicious calls."""
        if not isinstance(func_name, str):
            return False

        if not re.match(r'^[a-zA-Z][a-zA-Z0-9_]*$', func_name):
            return False

        if func_name.startswith('_'):
            return False

        dangerous_funcs = {
            'eval', 'exec', 'compile', '__import__', 'open', 'file'
        }

        if func_name in dangerous_funcs:
            return False

        return True

    def validate_args(self, args: List[Any]) -> List[Any]:
        """Basic argument validation."""
        return args


class SecurityConfig:
    """Simplified security configuration."""

    def __init__(self, http_port: int = None):
        self.enable_input_validation = True
        self.max_message_size = 1024 * 1024  # 1MB
        self.http_port = http_port
        self.allowed_origins = {
            "http://127.0.0.1:<server_port>",
            "http://localhost:<server_port>",
        }

    def is_origin_allowed(self, origin: str) -> bool:
        """Check if the Origin header value is allowed."""
        if not isinstance(origin, str) or not origin:
            return False
        if self.http_port is not None:
            expected1 = f"http://localhost:{self.http_port}"
            expected2 = f"http://127.0.0.1:{self.http_port}"
            return origin == expected1 or origin == expected2
        pattern = r'^http://(localhost|127\.0\.0\.1)(:\\d+)?$'
        return re.match(pattern, origin) is not None

    def update(self, **kwargs):
        """Update security configuration."""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
