"""
chat-demo - Authentication Module
Generado automáticamente por tai-api set-auth

Módulo de autenticación con JWT y manejo de sesiones.
"""

from .jwt import JWTHandler, TokenPayload
from .dependencies import (
    get_current_user,
    CurrentUser,
    oauth2_scheme
)
from .auth_router import router as auth_router

__all__ = [
    # JWT Handler
    "JWTHandler",
    "TokenPayload",
    
    # Dependencies
    "get_current_user",
    "CurrentUser",
    "oauth2_scheme",
    
    # Routers
    "auth_router",
]