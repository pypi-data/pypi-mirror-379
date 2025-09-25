"""
chat-demo - JWT Token Handler
Generado automáticamente por tai-api set-auth

Este módulo maneja la creación, validación y decodificación de tokens JWT
para el sistema de autenticación basado en base de datos.
"""

import os
from jose import jwt
from jose.exceptions import JWTError, ExpiredSignatureError
import uuid
from datetime import datetime, timedelta, timezone
from typing import Optional
from pydantic import BaseModel

from ..resources import InvalidTokenException, TokenExpiredException

# Configuración JWT
JWT_SECRET_KEY = os.getenv("SECRET_KEY")
if not JWT_SECRET_KEY:
    raise ValueError("La clave secreta JWT no está configurada. Establezca la variable de entorno SECRET_KEY.")
JWT_ALGORITHM = "HS256"
JWT_EXPIRATION = 600  # Token válido por N minutos

class TokenPayload(BaseModel):
    """Estructura del payload del token JWT"""
    username: str
    exp: datetime
    session_id: str
    
    class Config:
        json_encoders = {
            datetime: lambda v: int(v.timestamp())
        }

class JWTHandler:
    """Manejador de tokens JWT para autenticación"""
    
    @staticmethod
    def create_token(username: str, session_id: str) -> str:
        """
        Crea un nuevo token JWT con los datos del usuario.
        
        Args:
            username: Nombre de usuario
            session_id: ID único de la sesión
            
        Returns:
            str: Token JWT firmado
        """
        expiration = datetime.now(timezone.utc) + timedelta(minutes=JWT_EXPIRATION)
        
        payload = {
            "username": username,
            "exp": expiration,
            "session_id": session_id
        }
        
        token = jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
        return token
    
    @staticmethod
    def decode_token(token: str) -> Optional[TokenPayload]:
        """
        Decodifica y valida un token JWT.
        
        Args:
            token: Token JWT a decodificar
            
        Returns:
            TokenPayload: Datos del token si es válido, None si no
            
        Raises:
            InvalidTokenException: Si el token es inválido
            TokenExpiredException: Si el token ha expirado
        """
        
        try:
            payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
            
            # Convertir timestamp a datetime si es necesario
            if isinstance(payload.get('exp'), (int, float)):
                payload['exp'] = datetime.fromtimestamp(payload['exp'])
            
            return TokenPayload(**payload)
            
        except ExpiredSignatureError:
            raise TokenExpiredException("El token ha expirado")
        except JWTError:
            raise InvalidTokenException("Token inválido")
        except Exception as e:
            raise InvalidTokenException(f"Error al decodificar token: {str(e)}")
    
    @staticmethod
    def generate_session_id() -> str:
        """
        Genera un ID único para la sesión.
        
        Returns:
            str: UUID4 como string
        """
        return str(uuid.uuid4())
    