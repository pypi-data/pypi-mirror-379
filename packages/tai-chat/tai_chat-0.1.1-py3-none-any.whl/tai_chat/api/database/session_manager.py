# Este archivo ha sido generado automáticamente por tai-sql
# No modifiques este archivo directamente

from __future__ import annotations
import os
import re
from urllib.parse import (
    unquote,
    urlparse,
    parse_qs
)
from typing import (
    Optional,
    AsyncGenerator
)
from contextlib import asynccontextmanager
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine,
    AsyncSession,
    async_sessionmaker
)

class AsyncSessionManager:
    """
    Gestor de sesiones asíncronas para SQLAlchemy.
    
    Esta clase centraliza la gestión del ciclo de vida completo de las sesiones
    SQLAlchemy, proporcionando una interfaz consistente y segura para todas
    las operaciones de base de datos.
    
    Características principales:
    - Configuración automática del engine basada en variables de entorno
    - Context managers para gestión automática de transacciones
    - Soporte para sesiones individuales y transacciones compartidas
    - Manejo robusto de errores con rollback automático
    - Pool de conexiones optimizado para aplicaciones web
    
    Métodos principales:
        `get_session`: Context manager para sesiones automáticas
    
    Atributos:
        `engine` (AsyncEngine): Motor SQLAlchemy configurado
        `session_factory` (async_sessionmaker): Factoría de sesiones

    Configuración del Engine:
        - Pool size: 5 conexiones
        - Max overflow: 5 conexiones adicionales
        - Pool timeout: 30 segundos
        - Pool recycle: 3600 segundos
        - Pre-ping True para detectar conexiones perdidas
    
    Ejemplos de uso:
        ```python
        # Para transacciones automáticas
        async with db_api.session_manager.get_session() as session:
            user = await db_api.user.create(name="Juan", session=session)
            await db_api.post.create(title='Hola', content='Mundo', author_id=user.id, session=session)
            # Commit automático
        # Rollback automático en caso de error
        ```
    """
    
    def __init__(self):
        """Inicializa el gestor de sesiones"""
        self._engine: Optional[AsyncEngine] = None
        self._session_factory: Optional[async_sessionmaker] = None
    
    @property
    def async_driver_mapping(self) -> dict:
        """
        Mapeo de drivers síncronos a sus versiones asíncronas.
        
        Returns:
            dict: Mapeo de drivers
        """
        return {
            'postgresql': 'postgresql+asyncpg',
            'mysql': 'mysql+aiomysql',
            'mssql': 'mssql+aioodbc',
            # Agregar más mapeos según sea necesario
        }
    
    @property
    def engine(self) -> AsyncEngine:
        """Acceso al motor de base de datos"""
        if not self._engine:
            # Configuración desde variable de entorno (recomendado)
            connection_string = os.getenv('CHATBOT_DATABASE_URL')
            if not connection_string:
                raise ValueError('Variable de entorno "MAIN_DATABASE_URL" no encontrada')
            url = self.from_connection_string(connection_string)
            
            # Configuración del motor
            engine_kwargs = {
                'echo': False,
                'pool_pre_ping': True,
                'pool_recycle': 3600,
                'pool_size': 5,
                'max_overflow': 5,
                'pool_timeout': 30
            }
            
            self._engine = create_async_engine(url, **engine_kwargs)
        return self._engine
    
    @property
    def session_factory(self) -> async_sessionmaker:
        """Configura la factoría de sesiones"""
        if not self._session_factory:
            if not self.engine:
                raise ValueError("Motor de base de datos no configurado")
            self._session_factory = async_sessionmaker(
                bind=self.engine,
                autoflush=False,
                autocommit=False
            )
        return self._session_factory
    
    @asynccontextmanager
    async def get_session(self) -> AsyncGenerator[AsyncSession, None, None]:
        """
        Context manager para obtener una sesión.
            
        Yields:
            AsyncSession: Sesión SQLAlchemy configurada
            
        Example:
            ```python
            async with db.session_manager.get_session() as session:
                await db.user.create(name="Juan", email="juan@triplealpha.in", session=session)
                # Commit automático al salir del context manager
            ```
        """
        session: AsyncSession = self.session_factory()
        
        try:
            if not session.in_transaction():
                await session.begin()
            
            yield session
            
            # Commit si hay una transacción activa
            if session.in_transaction():
                await session.commit()
            
        except Exception as e:
            # Rollback en caso de error
            if session.in_transaction():
                await session.rollback()
            raise e
        finally:
            # Siempre cerrar la sesión
            await session.close()

    def from_connection_string(self, connection_string: str) -> URL:
        """
        Crea una URL desde un string de conexión.
        
        Args:
            connection_string: String de conexión completo
            
        Returns:
            Instancia de URL configurada desde string
            
        Raises:
            ValueError: Si el string de conexión no es válido
        """
        try:
            
            # Mejorar el parsing para manejar caracteres especiales
            connection_string = connection_string.strip()
            
            # Verificar formato básico
            if '://' not in connection_string:
                raise ValueError("String de conexión debe tener formato: driver://user:pass@host:port/db")
            
            # Usar urlparse con manejo mejorado de caracteres especiales
            parse = urlparse(connection_string)
            
            # Validar componentes esenciales
            if not parse.scheme:
                raise ValueError("Driver no especificado en el string de conexión")
            
            if not parse.hostname:
                raise ValueError("Host no especificado en el string de conexión")
            
            # Transformar el driver a su versión asíncrona
            original_driver = parse.scheme
            async_driver = self.async_driver_mapping.get(original_driver, original_driver)
            
            # Si el driver ya incluye un adaptador (ej: postgresql+asyncpg), mantenerlo
            if '+' in original_driver:
                async_driver = original_driver
            
            # Manejar la base de datos (puede estar vacía para algunos casos)
            database = parse.path[1:] if parse.path and len(parse.path) > 1 else None

            # Manejar puerto con valor por defecto según el driver
            port = parse.port
            if port is None:
                # Asignar puertos por defecto según el driver
                default_ports = {
                    'postgresql': 5432,
                    'mysql': 3306,
                    'sqlite': None,
                    'mssql': 1433,
                    'oracle': 1521
                }
                port = default_ports.get(parse.scheme, None)
            
            # Parsear query parameters de forma más robusta
            query_params = {}
            if parse.query:
                try:
                    query_params = parse_qs(parse.query)
                    # Convertir listas de un elemento a valores únicos
                    query_params = {k: v[0] if len(v) == 1 else v for k, v in query_params.items()}
                except Exception as e:
                    # Si falla el parsing de query, continuar sin ellos
                    print(f"⚠️  Advertencia: No se pudieron parsear los parámetros de consulta: {e}")
                    query_params = {}
            
            # Crear la URL con manejo de errores mejorado
            try:
                return URL.create(
                    drivername=async_driver,
                    username=parse.username,
                    password=parse.password,  # urlparse maneja el unquoting automáticamente
                    host=parse.hostname,
                    port=port,
                    database=database,
                    query=query_params
                )
            except Exception as url_error:
                # Proporcionar información más detallada del error
                raise ValueError(
                    f"Error creando URL SQLAlchemy: {url_error}\n"
                    f"Componentes parseados:\n"
                    f"  - Driver: {parse.scheme}\n"
                    f"  - Usuario: {parse.username}\n"
                    f"  - Host: {parse.hostname}\n"
                    f"  - Puerto: {port}\n"
                    f"  - Base de datos: {database}\n"
                    f"  - Tiene contraseña: {'Sí' if parse.password else 'No'}"
                )
            
        except Exception as e:
            return self.from_connection_string_escaped(connection_string)

    def from_connection_string_escaped(self, connection_string: str) -> URL:
        """
        Versión alternativa que maneja manualmente el escaping de caracteres especiales.
        
        Útil cuando urlparse falla con caracteres especiales en las contraseñas.
        
        Args:
            connection_string: String de conexión que puede contener caracteres especiales
            
        Returns:
            URL
        """
        
        try:
            
            # Parsear manualmente para manejar caracteres especiales
            # Patrón para extraer componentes: driver://user:pass@host:port/db
            pattern = r'^([^:]+)://([^:]+):([^@]+)@([^:/]+)(?::(\d+))?(?:/(.*))?$'
            match = re.match(pattern, connection_string.strip())
            
            if not match:
                raise ValueError(
                    "Formato de connection string no válido.\n"
                    "Esperado: driver://username:password@host:port/database"
                )
            
            driver, username, password, host, port, database_and_query = match.groups()

            async_driver = self.async_driver_mapping.get(driver, driver)
            
            # Separar database de query parameters si existen
            database = None
            query_params = {}
            
            if database_and_query:
                if '?' in database_and_query:
                    database, query_string = database_and_query.split('?', 1)
                    # Parsear query parameters
                    for param in query_string.split('&'):
                        if '=' in param:
                            key, value = param.split('=', 1)
                            query_params[unquote(key)] = unquote(value)
                else:
                    database = database_and_query
            
            # Convertir puerto a entero si existe
            if port:
                try:
                    port = int(port)
                except ValueError:
                    raise ValueError(f"Puerto inválido: {port}")
            
            else:
                # Asignar puertos por defecto según el driver
                default_ports = {
                    'postgresql': 5432,
                    'mysql': 3306,
                    'sqlite': None,
                    'mssql': 1433,
                    'oracle': 1521
                }
                port = default_ports.get(driver, None)
            
            # Crear URL SQLAlchemy
            return URL.create(
                drivername=async_driver,
                username=unquote(username) if username else None,
                password=unquote(password) if password else None,
                host=unquote(host) if host else None,
                port=port,
                database=unquote(database) if database else None,
                query=query_params
            )
            
        except Exception as e:
            raise ValueError(f"Error en parsing manual: {e}")
