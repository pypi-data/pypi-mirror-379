# Este archivo ha sido generado automáticamente por tai-sql
# No modifiques este archivo directamente
from __future__ import annotations
from typing import (
    List,
    Optional,
    Dict,
    Literal,
    Any
)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import (
    select,
    update,
    delete,
    func
)

from .session_manager import AsyncSessionManager
from .dtos import *
from .utils import (
    error_handler,
    get_loading_options,
    load_relationships_from_dto
)
from .models import *

from tai_alphi import Alphi
from datetime import datetime

# Logger
logger = Alphi.get_logger_by_name("tai-chatbot")

class UsuarioAsyncDAO:
    """
    Clase DAO asíncrona para el modelo Usuario.
    
    Proporciona operaciones completas de Create, Read, Update y Delete
    para el modelo Usuario con soporte para gestión automática
    y manual de sesiones SQLAlchemy.
    
    Características principales:
    - Soporte dual: sesiones automáticas o compartidas
    - Type hints completos para mejor experiencia de desarrollo
    - Manejo robusto de errores con rollback automático
    - Operaciones optimizadas con flush para obtener IDs
    - Filtros flexibles en todas las operaciones de búsqueda
    
    Métodos de lectura:
        find(**filters, session=None): Busca un único registro
        find_many(limit, offset, order_by, order, **filters, session=None): Busca múltiples registros
        count(**filters, session=None): Cuenta registros

    Métodos de escritura:
        create(**data, session=None): Crea un nuevo registro
        create_many(records, session=None): Crea múltiples registros
        update(filters, **data, session=None): Actualiza registros existentes
        delete(**filters, session=None): Elimina registros

    Parámetros de sesión:
        Todos los métodos aceptan un parámetro opcional 'session':
        - Si session=None: Se crea una sesión automática con commit
        - Si session=AsyncSession: Se usa la sesión proporcionada (para transacciones)
    
    Ejemplos de uso:
        ```python
        # Operaciones simples (sesión automática)
        crud = UsuarioDAO(session_manager)
        record = await crud.create(username="valor")
        found = await crud.find_by_id(1)
        
        # Operaciones transaccionales (sesión compartida)
        async with session_manager.transaction() as session:
            record1 = await crud.create(data="valor1", session=session)
            record2 = await crud.create(data="valor2", session=session)
            # Ambos se crean en la misma transacción
        ```
    """
    
    def __init__(self, session_manager: AsyncSessionManager):
        """
        Inicializa el AsyncDAO con un gestor de sesiones.
        
        Args:
            session_manager: Gestor de sesiones asíncronas
        """
        self.session_manager = session_manager
    
    @error_handler
    async def find(
        self,
        username: str,
        includes: Optional[List[str]] = None,
        session: Optional[AsyncSession] = None
    ) -> Optional[UsuarioRead]:
        """
        Busca un único registro por primary key con carga optimizada de relaciones.
        
        Args:
            username: Filtrar por username
            includes: Lista de relaciones a incluir (formato: 'relation' o 'relation.nested')
            session: Sesión existente (opcional)
            
        Returns:
            Instancia del modelo o None si no se encuentra
            
        Examples:
            Incluir relación simple

            await dao.find(id=1, includes=['author'])
            
            Incluir relaciones anidadas

            await dao.find(id=1, includes=['author', 'author.posts'])
            
            Múltiples relaciones

            await dao.find(id=1, includes=['author', 'comments', 'tags'])
        """
        logger.info(f"[chatbot] 🔍 Buscando Usuario:")
        logger.info(f"[chatbot]     username={username}")
        logger.info(f"[chatbot]     includes={includes}")
        
        # Construir query base
        query = select(Usuario)
        
        # Aplicar filtros de búsqueda
        query = query.where(Usuario.username == username)
        
        # Aplicar opciones de carga optimizada
        if includes:
            loading_options = get_loading_options(Usuario, includes)
            if loading_options:
                query = query.options(*loading_options)
        
        # Ejecutar query
        async def execute_query(session: AsyncSession) -> Optional[UsuarioRead]:
            result = await session.execute(query)
            instance = result.scalars().first()
            
            if instance:
                logger.info(f"[chatbot] ✅ Usuario encontrado exitosamente")
                return UsuarioRead.from_instance(
                    instance, 
                    includes=includes, 
                    max_depth=5
                )
            else:
                logger.info(f"[chatbot] 📭 Usuario no encontrado")
                return None
        
        if session is not None:
            return await execute_query(session)
        else:
            async with self.session_manager.get_session() as session:
                return await execute_query(session)

    @error_handler
    async def find_many(
        self,
        limit: Optional[int] = None, 
        offset: Optional[int] = None,
        order_by: Optional[List[str]] = None,
        order: Literal["ASC", "DESC"] = "ASC",
        username: Optional[str] = None,
        password: Optional[str] = None,
        email: Optional[str] = None,
        avatar: Optional[str] = None,
        session_id: Optional[str] = None,
        min_created_at: Optional[datetime] = None,
        max_created_at: Optional[datetime] = None,
        min_updated_at: Optional[datetime] = None,
        max_updated_at: Optional[datetime] = None,
        is_active: Optional[bool] = None,
        includes: Optional[List[str]] = None,
        session: Optional[AsyncSession] = None
    ) -> List[UsuarioRead]:
        """
        Busca múltiples registros con carga optimizada de relaciones.
        
        Args:
            - limit: Límite de registros a retornar
            - offset: Número de registros a saltar
            - order_by: Lista de nombres de columnas para ordenar los resultados
            - order: ASC/DESC (por defecto ASC). Solo se aplica si se especifica order_by.
            - username: Filtrar por username
            - password: Filtrar por password
            - email: Filtrar por email
            - avatar: Filtrar por avatar
            - session_id: Filtrar por session_id
            - min_created_at: Filtrar por valor mínimo de created_at (incluído)
            - max_created_at: Filtrar por valor máximo de created_at (incluído)
            - min_updated_at: Filtrar por valor mínimo de updated_at (incluído)
            - max_updated_at: Filtrar por valor máximo de updated_at (incluído)
            - is_active: Filtrar por is_active
            - includes: Lista de relaciones a incluir (formato: 'relation' o 'relation.nested')
            - session: Sesión existente (opcional)
            
        Returns:
            Lista de instancias del modelo
            
        Examples:
            Búsqueda simple con relaciones

            await dao.find_many(limit=10, includes=['author'])
            
            Relaciones anidadas

            await dao.find_many(
                ..., 
                includes=['author', 'author.profile', 'comments']
            )
            
            Ordenamiento ascendente por columnas

            await dao.find_many(order_by=['created_at', 'name'], order='ASC')
            
            Ordenamiento descendente por columnas

            await dao.find_many(order_by=['created_at', 'name'], order='DESC')
            
            Paginación

            # Obtener los primeros 10 registros
            await dao.find_many(limit=10)
            
            # Obtener los últimos 5 registros ordenados por fecha
            await dao.find_many(limit=5, order_by=['created_at'], order='DESC')
            
            # Paginación con offset
            await dao.find_many(limit=10, offset=20)
            
        """
        logger.info(f"[chatbot] 🔍 Buscando múltiples Usuario:")
        logger.info(f"[chatbot]     limit={limit}")
        logger.info(f"[chatbot]     offset={offset}")
        logger.info(f"[chatbot]     order_by={order_by}")
        logger.info(f"[chatbot]     order={order}")
        logger.info(f"[chatbot]     includes={includes}")
        
        # Construir query base
        query = select(Usuario)

        # Filters
        filters = {}
        
        # Aplicar filtros de búsqueda
        if username is not None:
            filters['username'] = username
            query = query.where(Usuario.username == username)
        if password is not None:
            filters['password'] = password
            query = query.where(Usuario.password == password)
        if email is not None:
            filters['email'] = email
            if isinstance(email, str) and '%' in email:
                query = query.where(Usuario.email.ilike(email))
            else:
                query = query.where(Usuario.email == email)
        if avatar is not None:
            filters['avatar'] = avatar
            if isinstance(avatar, str) and '%' in avatar:
                query = query.where(Usuario.avatar.ilike(avatar))
            else:
                query = query.where(Usuario.avatar == avatar)
        if session_id is not None:
            filters['session_id'] = session_id
            if isinstance(session_id, str) and '%' in session_id:
                query = query.where(Usuario.session_id.ilike(session_id))
            else:
                query = query.where(Usuario.session_id == session_id)
        if min_created_at is not None:
            filters['min_created_at'] = min_created_at
            query = query.where(Usuario.created_at >= min_created_at)
        if max_created_at is not None:
            filters['max_created_at'] = max_created_at
            query = query.where(Usuario.created_at <= max_created_at)
        if min_updated_at is not None:
            filters['min_updated_at'] = min_updated_at
            query = query.where(Usuario.updated_at >= min_updated_at)
        if max_updated_at is not None:
            filters['max_updated_at'] = max_updated_at
            query = query.where(Usuario.updated_at <= max_updated_at)
        if is_active is not None:
            filters['is_active'] = is_active
            query = query.where(Usuario.is_active == is_active)
        
        # Log de parámetros aplicados
        if filters:
            logger.info(f"[chatbot]     filters={filters}")
        
        # Aplicar opciones de carga optimizada
        if includes:
            loading_options = get_loading_options(Usuario, includes)
            if loading_options:
                query = query.options(*loading_options)

        # Aplicar ordenamiento
        if order_by:
            for column_name in order_by:
                if hasattr(Usuario, column_name):
                    column = getattr(Usuario, column_name)
                    if order.upper() == "DESC":
                        query = query.order_by(column.desc())
                    elif order.upper() == "ASC":
                        query = query.order_by(column.asc())
                else:
                    logger.warning(f"[chatbot] ⚠️ Columna '{column_name}' no existe en modelo Usuario, ignorando en order_by")
        
        # Aplicar límite (solo valores positivos)
        if limit is not None and limit > 0:
            query = query.limit(limit)

        # Aplicar paginación
        if offset is not None:
            query = query.offset(offset)

        # Ejecutar query
        async def execute_query(session: AsyncSession) -> List[UsuarioRead]:
            results = await session.execute(query)
            instances = results.scalars().all()
            
            logger.info(f"[chatbot] ✅ Encontrados {len(instances)} registros Usuario")
            
            return [
                UsuarioRead.from_instance(
                    instance, 
                    includes=includes, 
                    max_depth=5
                ) 
                for instance in instances
            ]
        
        if session is not None:
            return await execute_query(session)
        else:
            async with self.session_manager.get_session() as session:
                return await execute_query(session)
    
    @error_handler
    async def create(
        self, 
        usuario: UsuarioCreate,
        session: Optional[AsyncSession] = None
    ) -> UsuarioRead:
        """
        Crea un nuevo registro.
        
        Args:
            usuario: Datos del usuario a crear
            session: Sesión existente (opcional)
            
        Returns:
            Instancia del modelo creado
        """
        logger.info(f"[chatbot] 🆕 Creando nuevo Usuario")

        instance = usuario.to_instance()

        if session is not None:
            session.add(instance)
            await session.flush()  # Asegura que se genere el ID si es autoincrement
            included = await load_relationships_from_dto(session, instance, usuario)
            data = UsuarioRead.from_created_instance(instance, included)
        else:
            async with self.session_manager.get_session() as session:
                session.add(instance)
                await session.flush()  # Asegura que se genere el ID si es autoincrement
                included = await load_relationships_from_dto(session, instance, usuario)
                data = UsuarioRead.from_created_instance(instance, included)
        
        logger.info(f"[chatbot] ✅ Usuario creado exitosamente con username={getattr(data, 'username', 'N/A')}")
        return data
    
    @error_handler
    async def create_many(self, records: List[UsuarioCreate], session: Optional[AsyncSession] = None) -> int:
        """
        Crea múltiples registros en la tabla usuario.
        
        Args:
            records: Lista de UsuarioCreate con los datos de los registros
            session: Sesión existente (opcional)
            
        Returns:
            Número de registros creados

        """
        logger.info(f"[chatbot] 🔢 Creando {len(records)} registros Usuario")

        instances = []
        for record in records:
            instances.append(record.to_instance())
        
        if session is not None:
            session.add_all(instances)
            await session.flush()  # Asegura que se generen los IDs si son autoincrement
        else:
            async with self.session_manager.get_session() as session:
                session.add_all(instances)
                await session.flush()  # Asegura que se generen los IDs si son autoincrement

        logger.info(f"[chatbot] ✅ {len(instances)} registros Usuario creados exitosamente")

        return len(instances)
    
    @error_handler
    async def update(
        self, 
        username: str,
        updated_values: UsuarioUpdateValues,
        session: Optional[AsyncSession] = None
    ) -> int:
        """
        Actualiza registros que coincidan con los filtros.
        
        Args:
            username: Identificador del registro
            updated_values: Datos a actualizar
            session: Sesión existente (opcional)
            
        Returns:
            Número de registros actualizados
        """

        update_data = updated_values.to_dict()

        if not update_data:  # Solo actualizar si hay datos
            return 0

        logger.info(f"[chatbot] 🔄 Actualizando Usuario:")
        logger.info(f"[chatbot]     username={username}")
        logger.info(f"[chatbot]     valores={update_data}")

        query = select(Usuario)
        
        query = query.where(Usuario.username == username)

        if session is not None:
            result = await session.execute(query)
            record = result.scalar_one_or_none()
            if record is None:
                return 0
            for key, value in update_data.items():
                setattr(record, key, value)

            await session.flush()  # Aplicar cambios a la base de datos    
        else:
            async with self.session_manager.get_session() as session:
                result = await session.execute(query)
                record = result.scalar_one_or_none()
                if record is None:
                    return 0
                for key, value in update_data.items():
                    setattr(record, key, value)

                await session.flush()  # Aplicar cambios a la base de datos

        logger.info(f"[chatbot]  ✅ 1 registros Usuario actualizados exitosamente")

        return 1
    
    @error_handler
    async def update_many(
        self,
        payload: UsuarioUpdate, 
        session: Optional[AsyncSession] = None
    ) -> int:
        """
        Actualiza múltiples registros basándose en campos de coincidencia.
        
        Args:
            payload: Datos de actualización y filtros
            session: Sesión existente (opcional)
            
        Returns:
            Número total de registros actualizados
        """
        logger.info(f"[chatbot] 🔄 Actualizando múltiples Usuario con filtros: {payload.filter.to_dict()}, valores: {payload.values.to_dict()}")
            
        filters = payload.filter.to_dict()
        values = payload.values.to_dict()
        
        if not filters and not values:  # Solo actualizar si hay filtros y valores
            return 0

        query = update(Usuario)
        
        for key, value in filters.items():
            query = query.where(getattr(Usuario, key) == value)
        
        query = query.values(**values)
                
        if session is not None:
            result = await session.execute(query)
        else:
            async with self.session_manager.get_session() as session:
                result = await session.execute(query)
        
        logger.info(f"[chatbot] ✅ {result.rowcount} registros Usuario actualizados masivamente exitosamente")

        return result.rowcount
    
    @error_handler
    async def delete(
        self, 
        username: str,
        session: Optional[AsyncSession] = None
    ) -> int:
        """
        Elimina un registro atentiendo a su primary key.
        
        Args:
            username: Filtrar por username para eliminar
            session: Sesión existente (opcional)
            
        Returns:
            Número de registros eliminados
        """
        logger.info(f"[chatbot] 🗑️ Eliminando Usuario:")
        logger.info(f"[chatbot]    username={username}")

        query = delete(Usuario)
        
        query = query.where(Usuario.username == username)

        if session is not None:
            result = await session.execute(query)
        else:
            async with self.session_manager.get_session() as session:
                result = await session.execute(query)

        logger.info(f"[chatbot] ✅ {result.rowcount} registros Usuario eliminados exitosamente")

        return result.rowcount
    
    @error_handler
    async def delete_many(self, filters_list: List[Dict[str, Any]]) -> int:
        """
        Elimina múltiples registros basándose en una lista de filtros.
        
        Args:
            filters_list: Lista de diccionarios con filtros para cada eliminación
            
        Returns:
            Número total de registros eliminados
        """
        logger.info(f"[chatbot] 🗑️ Eliminando múltiples Usuario con {len(filters_list)} filtros")

        total_deleted = 0
        async def execute_query(session: AsyncSession) -> int:
            for filters in filters_list:
                query = delete(Usuario)
                
                for key, value in filters.items():
                    if hasattr(Usuario, key):
                        query = query.where(getattr(Usuario, key) == value)
                
                result = await session.execute(query)
                total_deleted += result.rowcount
        
        if session is not None:
            await execute_query(session)
        else:
            async with self.session_manager.get_session() as session:
                await execute_query(session)
        
        logger.info(f"[chatbot] ✅ {total_deleted} registros Usuario eliminados masivamente exitosamente")
        
        return total_deleted
    
    @error_handler
    async def count(
        self,
        username: Optional[str] = None,
        password: Optional[str] = None,
        email: Optional[str] = None,
        avatar: Optional[str] = None,
        session_id: Optional[str] = None,
        min_created_at: Optional[datetime] = None,
        max_created_at: Optional[datetime] = None,
        min_updated_at: Optional[datetime] = None,
        max_updated_at: Optional[datetime] = None,
        is_active: Optional[bool] = None,
        session: Optional[AsyncSession] = None
    ) -> int:
        """
        Cuenta registros que coincidan con los filtros.
        
        Args:
            - username: Filtrar por username
            - password: Filtrar por password
            - email: Filtrar por email
            - avatar: Filtrar por avatar
            - session_id: Filtrar por session_id
            - min_created_at: Filtrar por valor mínimo de created_at (incluído)
            - max_created_at: Filtrar por valor máximo de created_at (incluído)
            - min_updated_at: Filtrar por valor mínimo de updated_at (incluído)
            - max_updated_at: Filtrar por valor máximo de updated_at (incluído)
            - is_active: Filtrar por is_active
            - session: Sesión existente (opcional)
            
        Returns:
            Número de registros que coinciden con los filtros
        """
        logger.info(f"[chatbot] 🔢 Contando registros Usuario con filtros aplicados")
        
        query = select(func.count()).select_from(Usuario)
        
        # Filters
        filters = {}
        
        if username is not None:
            filters['username'] = username
            query = query.where(Usuario.username == username)
        if password is not None:
            filters['password'] = password
            query = query.where(Usuario.password == password)
        if email is not None:
            filters['email'] = email
            if isinstance(email, str) and '%' in email:
                query = query.where(Usuario.email.ilike(email))
            else:
                query = query.where(Usuario.email == email)
        if avatar is not None:
            filters['avatar'] = avatar
            if isinstance(avatar, str) and '%' in avatar:
                query = query.where(Usuario.avatar.ilike(avatar))
            else:
                query = query.where(Usuario.avatar == avatar)
        if session_id is not None:
            filters['session_id'] = session_id
            if isinstance(session_id, str) and '%' in session_id:
                query = query.where(Usuario.session_id.ilike(session_id))
            else:
                query = query.where(Usuario.session_id == session_id)
        if min_created_at is not None:
            filters['min_created_at'] = min_created_at
            query = query.where(Usuario.created_at >= min_created_at)
        if max_created_at is not None:
            filters['max_created_at'] = max_created_at
            query = query.where(Usuario.created_at <= max_created_at)
        if min_updated_at is not None:
            filters['min_updated_at'] = min_updated_at
            query = query.where(Usuario.updated_at >= min_updated_at)
        if max_updated_at is not None:
            filters['max_updated_at'] = max_updated_at
            query = query.where(Usuario.updated_at <= max_updated_at)
        if is_active is not None:
            filters['is_active'] = is_active
            query = query.where(Usuario.is_active == is_active)
        
        # Log de parámetros aplicados
        if filters:
            logger.info(f"[chatbot]     filters={filters}")

        if session is not None:
            result = await session.execute(query)
        else:
            async with self.session_manager.get_session() as session:
                result = await session.execute(query)

        count_result = result.scalar() or 0
        logger.info(f"[chatbot] ✅ Conteo Usuario completado: {count_result} registros")
        return count_result
    
    @error_handler
    async def exists(
        self,
        username: Optional[str] = None,
        password: Optional[str] = None,
        email: Optional[str] = None,
        avatar: Optional[str] = None,
        session_id: Optional[str] = None,
        min_created_at: Optional[datetime] = None,
        max_created_at: Optional[datetime] = None,
        min_updated_at: Optional[datetime] = None,
        max_updated_at: Optional[datetime] = None,
        is_active: Optional[bool] = None,
        session: Optional[AsyncSession] = None
    ) -> bool:
        """
        Verifica si existe al menos un registro que coincida con los filtros.
        
        Args:
            - username: Filtrar por username
            - password: Filtrar por password
            - email: Filtrar por email
            - avatar: Filtrar por avatar
            - session_id: Filtrar por session_id
            - min_created_at: Filtrar por valor mínimo de created_at (incluído)
            - max_created_at: Filtrar por valor máximo de created_at (incluído)
            - min_updated_at: Filtrar por valor mínimo de updated_at (incluído)
            - max_updated_at: Filtrar por valor máximo de updated_at (incluído)
            - is_active: Filtrar por is_active
            session: Sesión existente (opcional)
            
        Returns:
            True si existe al menos un registro, False en caso contrario
        """
        logger.info(f"[chatbot] ❓ Verificando existencia de registros Usuario")
        
        records = await self.count(
            username=username,
            password=password,
            email=email,
            avatar=avatar,
            session_id=session_id,
            min_created_at=min_created_at,
            max_created_at=max_created_at,
            min_updated_at=min_updated_at,
            max_updated_at=max_updated_at,
            is_active=is_active,
            session=session
        )
        exists_result = records > 0
        logger.info(f"[chatbot] ✅ Verificación Usuario completada: {'existe' if exists_result else 'no existe'}")
        return exists_result


class ChatAsyncDAO:
    """
    Clase DAO asíncrona para el modelo Chat.
    
    Proporciona operaciones completas de Create, Read, Update y Delete
    para el modelo Chat con soporte para gestión automática
    y manual de sesiones SQLAlchemy.
    
    Características principales:
    - Soporte dual: sesiones automáticas o compartidas
    - Type hints completos para mejor experiencia de desarrollo
    - Manejo robusto de errores con rollback automático
    - Operaciones optimizadas con flush para obtener IDs
    - Filtros flexibles en todas las operaciones de búsqueda
    
    Métodos de lectura:
        find(**filters, session=None): Busca un único registro
        find_many(limit, offset, order_by, order, **filters, session=None): Busca múltiples registros
        count(**filters, session=None): Cuenta registros

    Métodos de escritura:
        create(**data, session=None): Crea un nuevo registro
        create_many(records, session=None): Crea múltiples registros
        update(filters, **data, session=None): Actualiza registros existentes
        delete(**filters, session=None): Elimina registros

    Parámetros de sesión:
        Todos los métodos aceptan un parámetro opcional 'session':
        - Si session=None: Se crea una sesión automática con commit
        - Si session=AsyncSession: Se usa la sesión proporcionada (para transacciones)
    
    Ejemplos de uso:
        ```python
        # Operaciones simples (sesión automática)
        crud = ChatDAO(session_manager)
        found = await crud.find_by_id(1)
        
        # Operaciones transaccionales (sesión compartida)
        async with session_manager.transaction() as session:
            record1 = await crud.create(data="valor1", session=session)
            record2 = await crud.create(data="valor2", session=session)
            # Ambos se crean en la misma transacción
        ```
    """
    
    def __init__(self, session_manager: AsyncSessionManager):
        """
        Inicializa el AsyncDAO con un gestor de sesiones.
        
        Args:
            session_manager: Gestor de sesiones asíncronas
        """
        self.session_manager = session_manager
    
    @error_handler
    async def find(
        self,
        id: int,
        includes: Optional[List[str]] = None,
        session: Optional[AsyncSession] = None
    ) -> Optional[ChatRead]:
        """
        Busca un único registro por primary key con carga optimizada de relaciones.
        
        Args:
            id: Filtrar por id
            includes: Lista de relaciones a incluir (formato: 'relation' o 'relation.nested')
            session: Sesión existente (opcional)
            
        Returns:
            Instancia del modelo o None si no se encuentra
            
        Examples:
            Incluir relación simple

            await dao.find(id=1, includes=['author'])
            
            Incluir relaciones anidadas

            await dao.find(id=1, includes=['author', 'author.posts'])
            
            Múltiples relaciones

            await dao.find(id=1, includes=['author', 'comments', 'tags'])
        """
        logger.info(f"[chatbot] 🔍 Buscando Chat:")
        logger.info(f"[chatbot]     id={id}")
        logger.info(f"[chatbot]     includes={includes}")
        
        # Construir query base
        query = select(Chat)
        
        # Aplicar filtros de búsqueda
        query = query.where(Chat.id == id)
        
        # Aplicar opciones de carga optimizada
        if includes:
            loading_options = get_loading_options(Chat, includes)
            if loading_options:
                query = query.options(*loading_options)
        
        # Ejecutar query
        async def execute_query(session: AsyncSession) -> Optional[ChatRead]:
            result = await session.execute(query)
            instance = result.scalars().first()
            
            if instance:
                logger.info(f"[chatbot] ✅ Chat encontrado exitosamente")
                return ChatRead.from_instance(
                    instance, 
                    includes=includes, 
                    max_depth=5
                )
            else:
                logger.info(f"[chatbot] 📭 Chat no encontrado")
                return None
        
        if session is not None:
            return await execute_query(session)
        else:
            async with self.session_manager.get_session() as session:
                return await execute_query(session)

    @error_handler
    async def find_many(
        self,
        limit: Optional[int] = None, 
        offset: Optional[int] = None,
        order_by: Optional[List[str]] = None,
        order: Literal["ASC", "DESC"] = "ASC",
        title: Optional[str] = None,
        username: Optional[str] = None,
        min_created_at: Optional[datetime] = None,
        max_created_at: Optional[datetime] = None,
        min_updated_at: Optional[datetime] = None,
        max_updated_at: Optional[datetime] = None,
        is_active: Optional[bool] = None,
        includes: Optional[List[str]] = None,
        session: Optional[AsyncSession] = None
    ) -> List[ChatRead]:
        """
        Busca múltiples registros con carga optimizada de relaciones.
        
        Args:
            - limit: Límite de registros a retornar
            - offset: Número de registros a saltar
            - order_by: Lista de nombres de columnas para ordenar los resultados
            - order: ASC/DESC (por defecto ASC). Solo se aplica si se especifica order_by.
            - title: Filtrar por title
            - username: Filtrar por username
            - min_created_at: Filtrar por valor mínimo de created_at (incluído)
            - max_created_at: Filtrar por valor máximo de created_at (incluído)
            - min_updated_at: Filtrar por valor mínimo de updated_at (incluído)
            - max_updated_at: Filtrar por valor máximo de updated_at (incluído)
            - is_active: Filtrar por is_active
            - includes: Lista de relaciones a incluir (formato: 'relation' o 'relation.nested')
            - session: Sesión existente (opcional)
            
        Returns:
            Lista de instancias del modelo
            
        Examples:
            Búsqueda simple con relaciones

            await dao.find_many(limit=10, includes=['author'])
            
            Relaciones anidadas

            await dao.find_many(
                ..., 
                includes=['author', 'author.profile', 'comments']
            )
            
            Ordenamiento ascendente por columnas

            await dao.find_many(order_by=['created_at', 'name'], order='ASC')
            
            Ordenamiento descendente por columnas

            await dao.find_many(order_by=['created_at', 'name'], order='DESC')
            
            Paginación

            # Obtener los primeros 10 registros
            await dao.find_many(limit=10)
            
            # Obtener los últimos 5 registros ordenados por fecha
            await dao.find_many(limit=5, order_by=['created_at'], order='DESC')
            
            # Paginación con offset
            await dao.find_many(limit=10, offset=20)
            
        """
        logger.info(f"[chatbot] 🔍 Buscando múltiples Chat:")
        logger.info(f"[chatbot]     limit={limit}")
        logger.info(f"[chatbot]     offset={offset}")
        logger.info(f"[chatbot]     order_by={order_by}")
        logger.info(f"[chatbot]     order={order}")
        logger.info(f"[chatbot]     includes={includes}")
        
        # Construir query base
        query = select(Chat)

        # Filters
        filters = {}
        
        # Aplicar filtros de búsqueda
        if title is not None:
            filters['title'] = title
            if isinstance(title, str) and '%' in title:
                query = query.where(Chat.title.ilike(title))
            else:
                query = query.where(Chat.title == title)
        if username is not None:
            filters['username'] = username
            query = query.where(Chat.username == username)
        if min_created_at is not None:
            filters['min_created_at'] = min_created_at
            query = query.where(Chat.created_at >= min_created_at)
        if max_created_at is not None:
            filters['max_created_at'] = max_created_at
            query = query.where(Chat.created_at <= max_created_at)
        if min_updated_at is not None:
            filters['min_updated_at'] = min_updated_at
            query = query.where(Chat.updated_at >= min_updated_at)
        if max_updated_at is not None:
            filters['max_updated_at'] = max_updated_at
            query = query.where(Chat.updated_at <= max_updated_at)
        if is_active is not None:
            filters['is_active'] = is_active
            query = query.where(Chat.is_active == is_active)
        
        # Log de parámetros aplicados
        if filters:
            logger.info(f"[chatbot]     filters={filters}")
        
        # Aplicar opciones de carga optimizada
        if includes:
            loading_options = get_loading_options(Chat, includes)
            if loading_options:
                query = query.options(*loading_options)

        # Aplicar ordenamiento
        if order_by:
            for column_name in order_by:
                if hasattr(Chat, column_name):
                    column = getattr(Chat, column_name)
                    if order.upper() == "DESC":
                        query = query.order_by(column.desc())
                    elif order.upper() == "ASC":
                        query = query.order_by(column.asc())
                else:
                    logger.warning(f"[chatbot] ⚠️ Columna '{column_name}' no existe en modelo Chat, ignorando en order_by")
        
        # Aplicar límite (solo valores positivos)
        if limit is not None and limit > 0:
            query = query.limit(limit)

        # Aplicar paginación
        if offset is not None:
            query = query.offset(offset)

        # Ejecutar query
        async def execute_query(session: AsyncSession) -> List[ChatRead]:
            results = await session.execute(query)
            instances = results.scalars().all()
            
            logger.info(f"[chatbot] ✅ Encontrados {len(instances)} registros Chat")
            
            return [
                ChatRead.from_instance(
                    instance, 
                    includes=includes, 
                    max_depth=5
                ) 
                for instance in instances
            ]
        
        if session is not None:
            return await execute_query(session)
        else:
            async with self.session_manager.get_session() as session:
                return await execute_query(session)
    
    @error_handler
    async def create(
        self, 
        chat: ChatCreate,
        session: Optional[AsyncSession] = None
    ) -> ChatRead:
        """
        Crea un nuevo registro.
        
        Args:
            chat: Datos del chat a crear
            session: Sesión existente (opcional)
            
        Returns:
            Instancia del modelo creado
        """
        logger.info(f"[chatbot] 🆕 Creando nuevo Chat")

        instance = chat.to_instance()

        if session is not None:
            session.add(instance)
            await session.flush()  # Asegura que se genere el ID si es autoincrement
            included = await load_relationships_from_dto(session, instance, chat)
            data = ChatRead.from_created_instance(instance, included)
        else:
            async with self.session_manager.get_session() as session:
                session.add(instance)
                await session.flush()  # Asegura que se genere el ID si es autoincrement
                included = await load_relationships_from_dto(session, instance, chat)
                data = ChatRead.from_created_instance(instance, included)
        
        logger.info(f"[chatbot] ✅ Chat creado exitosamente con id={getattr(data, 'id', 'N/A')}")
        return data
    
    @error_handler
    async def create_many(self, records: List[ChatCreate], session: Optional[AsyncSession] = None) -> int:
        """
        Crea múltiples registros en la tabla chat.
        
        Args:
            records: Lista de ChatCreate con los datos de los registros
            session: Sesión existente (opcional)
            
        Returns:
            Número de registros creados

        """
        logger.info(f"[chatbot] 🔢 Creando {len(records)} registros Chat")

        instances = []
        for record in records:
            instances.append(record.to_instance())
        
        if session is not None:
            session.add_all(instances)
            await session.flush()  # Asegura que se generen los IDs si son autoincrement
        else:
            async with self.session_manager.get_session() as session:
                session.add_all(instances)
                await session.flush()  # Asegura que se generen los IDs si son autoincrement

        logger.info(f"[chatbot] ✅ {len(instances)} registros Chat creados exitosamente")

        return len(instances)
    
    @error_handler
    async def update(
        self, 
        id: int,
        updated_values: ChatUpdateValues,
        session: Optional[AsyncSession] = None
    ) -> int:
        """
        Actualiza registros que coincidan con los filtros.
        
        Args:
            id: Identificador del registro
            updated_values: Datos a actualizar
            session: Sesión existente (opcional)
            
        Returns:
            Número de registros actualizados
        """

        update_data = updated_values.to_dict()

        if not update_data:  # Solo actualizar si hay datos
            return 0

        logger.info(f"[chatbot] 🔄 Actualizando Chat:")
        logger.info(f"[chatbot]     id={id}")
        logger.info(f"[chatbot]     valores={update_data}")

        query = select(Chat)
        
        query = query.where(Chat.id == id)

        if session is not None:
            result = await session.execute(query)
            record = result.scalar_one_or_none()
            if record is None:
                return 0
            for key, value in update_data.items():
                setattr(record, key, value)

            await session.flush()  # Aplicar cambios a la base de datos    
        else:
            async with self.session_manager.get_session() as session:
                result = await session.execute(query)
                record = result.scalar_one_or_none()
                if record is None:
                    return 0
                for key, value in update_data.items():
                    setattr(record, key, value)

                await session.flush()  # Aplicar cambios a la base de datos

        logger.info(f"[chatbot]  ✅ 1 registros Chat actualizados exitosamente")

        return 1
    
    @error_handler
    async def update_many(
        self,
        payload: ChatUpdate, 
        session: Optional[AsyncSession] = None
    ) -> int:
        """
        Actualiza múltiples registros basándose en campos de coincidencia.
        
        Args:
            payload: Datos de actualización y filtros
            session: Sesión existente (opcional)
            
        Returns:
            Número total de registros actualizados
        """
        logger.info(f"[chatbot] 🔄 Actualizando múltiples Chat con filtros: {payload.filter.to_dict()}, valores: {payload.values.to_dict()}")
            
        filters = payload.filter.to_dict()
        values = payload.values.to_dict()
        
        if not filters and not values:  # Solo actualizar si hay filtros y valores
            return 0

        query = update(Chat)
        
        for key, value in filters.items():
            query = query.where(getattr(Chat, key) == value)
        
        query = query.values(**values)
                
        if session is not None:
            result = await session.execute(query)
        else:
            async with self.session_manager.get_session() as session:
                result = await session.execute(query)
        
        logger.info(f"[chatbot] ✅ {result.rowcount} registros Chat actualizados masivamente exitosamente")

        return result.rowcount
    
    @error_handler
    async def delete(
        self, 
        id: int,
        session: Optional[AsyncSession] = None
    ) -> int:
        """
        Elimina un registro atentiendo a su primary key.
        
        Args:
            id: Filtrar por id para eliminar
            session: Sesión existente (opcional)
            
        Returns:
            Número de registros eliminados
        """
        logger.info(f"[chatbot] 🗑️ Eliminando Chat:")
        logger.info(f"[chatbot]    id={id}")

        query = delete(Chat)
        
        query = query.where(Chat.id == id)

        if session is not None:
            result = await session.execute(query)
        else:
            async with self.session_manager.get_session() as session:
                result = await session.execute(query)

        logger.info(f"[chatbot] ✅ {result.rowcount} registros Chat eliminados exitosamente")

        return result.rowcount
    
    @error_handler
    async def delete_many(self, filters_list: List[Dict[str, Any]]) -> int:
        """
        Elimina múltiples registros basándose en una lista de filtros.
        
        Args:
            filters_list: Lista de diccionarios con filtros para cada eliminación
            
        Returns:
            Número total de registros eliminados
        """
        logger.info(f"[chatbot] 🗑️ Eliminando múltiples Chat con {len(filters_list)} filtros")

        total_deleted = 0
        async def execute_query(session: AsyncSession) -> int:
            for filters in filters_list:
                query = delete(Chat)
                
                for key, value in filters.items():
                    if hasattr(Chat, key):
                        query = query.where(getattr(Chat, key) == value)
                
                result = await session.execute(query)
                total_deleted += result.rowcount
        
        if session is not None:
            await execute_query(session)
        else:
            async with self.session_manager.get_session() as session:
                await execute_query(session)
        
        logger.info(f"[chatbot] ✅ {total_deleted} registros Chat eliminados masivamente exitosamente")
        
        return total_deleted
    
    @error_handler
    async def count(
        self,
        title: Optional[str] = None,
        username: Optional[str] = None,
        min_created_at: Optional[datetime] = None,
        max_created_at: Optional[datetime] = None,
        min_updated_at: Optional[datetime] = None,
        max_updated_at: Optional[datetime] = None,
        is_active: Optional[bool] = None,
        session: Optional[AsyncSession] = None
    ) -> int:
        """
        Cuenta registros que coincidan con los filtros.
        
        Args:
            - title: Filtrar por title
            - username: Filtrar por username
            - min_created_at: Filtrar por valor mínimo de created_at (incluído)
            - max_created_at: Filtrar por valor máximo de created_at (incluído)
            - min_updated_at: Filtrar por valor mínimo de updated_at (incluído)
            - max_updated_at: Filtrar por valor máximo de updated_at (incluído)
            - is_active: Filtrar por is_active
            - session: Sesión existente (opcional)
            
        Returns:
            Número de registros que coinciden con los filtros
        """
        logger.info(f"[chatbot] 🔢 Contando registros Chat con filtros aplicados")
        
        query = select(func.count()).select_from(Chat)
        
        # Filters
        filters = {}
        
        if title is not None:
            filters['title'] = title
            if isinstance(title, str) and '%' in title:
                query = query.where(Chat.title.ilike(title))
            else:
                query = query.where(Chat.title == title)
        if username is not None:
            filters['username'] = username
            query = query.where(Chat.username == username)
        if min_created_at is not None:
            filters['min_created_at'] = min_created_at
            query = query.where(Chat.created_at >= min_created_at)
        if max_created_at is not None:
            filters['max_created_at'] = max_created_at
            query = query.where(Chat.created_at <= max_created_at)
        if min_updated_at is not None:
            filters['min_updated_at'] = min_updated_at
            query = query.where(Chat.updated_at >= min_updated_at)
        if max_updated_at is not None:
            filters['max_updated_at'] = max_updated_at
            query = query.where(Chat.updated_at <= max_updated_at)
        if is_active is not None:
            filters['is_active'] = is_active
            query = query.where(Chat.is_active == is_active)
        
        # Log de parámetros aplicados
        if filters:
            logger.info(f"[chatbot]     filters={filters}")

        if session is not None:
            result = await session.execute(query)
        else:
            async with self.session_manager.get_session() as session:
                result = await session.execute(query)

        count_result = result.scalar() or 0
        logger.info(f"[chatbot] ✅ Conteo Chat completado: {count_result} registros")
        return count_result
    
    @error_handler
    async def exists(
        self,
        title: Optional[str] = None,
        username: Optional[str] = None,
        min_created_at: Optional[datetime] = None,
        max_created_at: Optional[datetime] = None,
        min_updated_at: Optional[datetime] = None,
        max_updated_at: Optional[datetime] = None,
        is_active: Optional[bool] = None,
        session: Optional[AsyncSession] = None
    ) -> bool:
        """
        Verifica si existe al menos un registro que coincida con los filtros.
        
        Args:
            - title: Filtrar por title
            - username: Filtrar por username
            - min_created_at: Filtrar por valor mínimo de created_at (incluído)
            - max_created_at: Filtrar por valor máximo de created_at (incluído)
            - min_updated_at: Filtrar por valor mínimo de updated_at (incluído)
            - max_updated_at: Filtrar por valor máximo de updated_at (incluído)
            - is_active: Filtrar por is_active
            session: Sesión existente (opcional)
            
        Returns:
            True si existe al menos un registro, False en caso contrario
        """
        logger.info(f"[chatbot] ❓ Verificando existencia de registros Chat")
        
        records = await self.count(
            title=title,
            username=username,
            min_created_at=min_created_at,
            max_created_at=max_created_at,
            min_updated_at=min_updated_at,
            max_updated_at=max_updated_at,
            is_active=is_active,
            session=session
        )
        exists_result = records > 0
        logger.info(f"[chatbot] ✅ Verificación Chat completada: {'existe' if exists_result else 'no existe'}")
        return exists_result


class MensajeAsyncDAO:
    """
    Clase DAO asíncrona para el modelo Mensaje.
    
    Proporciona operaciones completas de Create, Read, Update y Delete
    para el modelo Mensaje con soporte para gestión automática
    y manual de sesiones SQLAlchemy.
    
    Características principales:
    - Soporte dual: sesiones automáticas o compartidas
    - Type hints completos para mejor experiencia de desarrollo
    - Manejo robusto de errores con rollback automático
    - Operaciones optimizadas con flush para obtener IDs
    - Filtros flexibles en todas las operaciones de búsqueda
    
    Métodos de lectura:
        find(**filters, session=None): Busca un único registro
        find_many(limit, offset, order_by, order, **filters, session=None): Busca múltiples registros
        count(**filters, session=None): Cuenta registros

    Métodos de escritura:
        create(**data, session=None): Crea un nuevo registro
        create_many(records, session=None): Crea múltiples registros
        update(filters, **data, session=None): Actualiza registros existentes
        delete(**filters, session=None): Elimina registros

    Parámetros de sesión:
        Todos los métodos aceptan un parámetro opcional 'session':
        - Si session=None: Se crea una sesión automática con commit
        - Si session=AsyncSession: Se usa la sesión proporcionada (para transacciones)
    
    Ejemplos de uso:
        ```python
        # Operaciones simples (sesión automática)
        crud = MensajeDAO(session_manager)
        found = await crud.find_by_id(1)
        
        # Operaciones transaccionales (sesión compartida)
        async with session_manager.transaction() as session:
            record1 = await crud.create(data="valor1", session=session)
            record2 = await crud.create(data="valor2", session=session)
            # Ambos se crean en la misma transacción
        ```
    """
    
    def __init__(self, session_manager: AsyncSessionManager):
        """
        Inicializa el AsyncDAO con un gestor de sesiones.
        
        Args:
            session_manager: Gestor de sesiones asíncronas
        """
        self.session_manager = session_manager
    
    @error_handler
    async def find(
        self,
        id: int,
        includes: Optional[List[str]] = None,
        session: Optional[AsyncSession] = None
    ) -> Optional[MensajeRead]:
        """
        Busca un único registro por primary key con carga optimizada de relaciones.
        
        Args:
            id: Filtrar por id
            includes: Lista de relaciones a incluir (formato: 'relation' o 'relation.nested')
            session: Sesión existente (opcional)
            
        Returns:
            Instancia del modelo o None si no se encuentra
            
        Examples:
            Incluir relación simple

            await dao.find(id=1, includes=['author'])
            
            Incluir relaciones anidadas

            await dao.find(id=1, includes=['author', 'author.posts'])
            
            Múltiples relaciones

            await dao.find(id=1, includes=['author', 'comments', 'tags'])
        """
        logger.info(f"[chatbot] 🔍 Buscando Mensaje:")
        logger.info(f"[chatbot]     id={id}")
        logger.info(f"[chatbot]     includes={includes}")
        
        # Construir query base
        query = select(Mensaje)
        
        # Aplicar filtros de búsqueda
        query = query.where(Mensaje.id == id)
        
        # Aplicar opciones de carga optimizada
        if includes:
            loading_options = get_loading_options(Mensaje, includes)
            if loading_options:
                query = query.options(*loading_options)
        
        # Ejecutar query
        async def execute_query(session: AsyncSession) -> Optional[MensajeRead]:
            result = await session.execute(query)
            instance = result.scalars().first()
            
            if instance:
                logger.info(f"[chatbot] ✅ Mensaje encontrado exitosamente")
                return MensajeRead.from_instance(
                    instance, 
                    includes=includes, 
                    max_depth=5
                )
            else:
                logger.info(f"[chatbot] 📭 Mensaje no encontrado")
                return None
        
        if session is not None:
            return await execute_query(session)
        else:
            async with self.session_manager.get_session() as session:
                return await execute_query(session)

    @error_handler
    async def find_many(
        self,
        limit: Optional[int] = None, 
        offset: Optional[int] = None,
        order_by: Optional[List[str]] = None,
        order: Literal["ASC", "DESC"] = "ASC",
        content: Optional[str] = None,
        role: Optional[str] = None,
        min_timestamp: Optional[datetime] = None,
        max_timestamp: Optional[datetime] = None,
        chat_id: Optional[int] = None,
        includes: Optional[List[str]] = None,
        session: Optional[AsyncSession] = None
    ) -> List[MensajeRead]:
        """
        Busca múltiples registros con carga optimizada de relaciones.
        
        Args:
            - limit: Límite de registros a retornar
            - offset: Número de registros a saltar
            - order_by: Lista de nombres de columnas para ordenar los resultados
            - order: ASC/DESC (por defecto ASC). Solo se aplica si se especifica order_by.
            - content: Filtrar por content
            - role: Filtrar por role
            - min_timestamp: Filtrar por valor mínimo de timestamp (incluído)
            - max_timestamp: Filtrar por valor máximo de timestamp (incluído)
            - chat_id: Filtrar por chat_id
            - includes: Lista de relaciones a incluir (formato: 'relation' o 'relation.nested')
            - session: Sesión existente (opcional)
            
        Returns:
            Lista de instancias del modelo
            
        Examples:
            Búsqueda simple con relaciones

            await dao.find_many(limit=10, includes=['author'])
            
            Relaciones anidadas

            await dao.find_many(
                ..., 
                includes=['author', 'author.profile', 'comments']
            )
            
            Ordenamiento ascendente por columnas

            await dao.find_many(order_by=['created_at', 'name'], order='ASC')
            
            Ordenamiento descendente por columnas

            await dao.find_many(order_by=['created_at', 'name'], order='DESC')
            
            Paginación

            # Obtener los primeros 10 registros
            await dao.find_many(limit=10)
            
            # Obtener los últimos 5 registros ordenados por fecha
            await dao.find_many(limit=5, order_by=['created_at'], order='DESC')
            
            # Paginación con offset
            await dao.find_many(limit=10, offset=20)
            
        """
        logger.info(f"[chatbot] 🔍 Buscando múltiples Mensaje:")
        logger.info(f"[chatbot]     limit={limit}")
        logger.info(f"[chatbot]     offset={offset}")
        logger.info(f"[chatbot]     order_by={order_by}")
        logger.info(f"[chatbot]     order={order}")
        logger.info(f"[chatbot]     includes={includes}")
        
        # Construir query base
        query = select(Mensaje)

        # Filters
        filters = {}
        
        # Aplicar filtros de búsqueda
        if content is not None:
            filters['content'] = content
            if isinstance(content, str) and '%' in content:
                query = query.where(Mensaje.content.ilike(content))
            else:
                query = query.where(Mensaje.content == content)
        if role is not None:
            filters['role'] = role
            if isinstance(role, str) and '%' in role:
                query = query.where(Mensaje.role.ilike(role))
            else:
                query = query.where(Mensaje.role == role)
        if min_timestamp is not None:
            filters['min_timestamp'] = min_timestamp
            query = query.where(Mensaje.timestamp >= min_timestamp)
        if max_timestamp is not None:
            filters['max_timestamp'] = max_timestamp
            query = query.where(Mensaje.timestamp <= max_timestamp)
        if chat_id is not None:
            filters['chat_id'] = chat_id
            query = query.where(Mensaje.chat_id == chat_id)
        
        # Log de parámetros aplicados
        if filters:
            logger.info(f"[chatbot]     filters={filters}")
        
        # Aplicar opciones de carga optimizada
        if includes:
            loading_options = get_loading_options(Mensaje, includes)
            if loading_options:
                query = query.options(*loading_options)

        # Aplicar ordenamiento
        if order_by:
            for column_name in order_by:
                if hasattr(Mensaje, column_name):
                    column = getattr(Mensaje, column_name)
                    if order.upper() == "DESC":
                        query = query.order_by(column.desc())
                    elif order.upper() == "ASC":
                        query = query.order_by(column.asc())
                else:
                    logger.warning(f"[chatbot] ⚠️ Columna '{column_name}' no existe en modelo Mensaje, ignorando en order_by")
        
        # Aplicar límite (solo valores positivos)
        if limit is not None and limit > 0:
            query = query.limit(limit)

        # Aplicar paginación
        if offset is not None:
            query = query.offset(offset)

        # Ejecutar query
        async def execute_query(session: AsyncSession) -> List[MensajeRead]:
            results = await session.execute(query)
            instances = results.scalars().all()
            
            logger.info(f"[chatbot] ✅ Encontrados {len(instances)} registros Mensaje")
            
            return [
                MensajeRead.from_instance(
                    instance, 
                    includes=includes, 
                    max_depth=5
                ) 
                for instance in instances
            ]
        
        if session is not None:
            return await execute_query(session)
        else:
            async with self.session_manager.get_session() as session:
                return await execute_query(session)
    
    @error_handler
    async def create(
        self, 
        mensaje: MensajeCreate,
        session: Optional[AsyncSession] = None
    ) -> MensajeRead:
        """
        Crea un nuevo registro.
        
        Args:
            mensaje: Datos del mensaje a crear
            session: Sesión existente (opcional)
            
        Returns:
            Instancia del modelo creado
        """
        logger.info(f"[chatbot] 🆕 Creando nuevo Mensaje")

        instance = mensaje.to_instance()

        if session is not None:
            session.add(instance)
            await session.flush()  # Asegura que se genere el ID si es autoincrement
            included = await load_relationships_from_dto(session, instance, mensaje)
            data = MensajeRead.from_created_instance(instance, included)
        else:
            async with self.session_manager.get_session() as session:
                session.add(instance)
                await session.flush()  # Asegura que se genere el ID si es autoincrement
                included = await load_relationships_from_dto(session, instance, mensaje)
                data = MensajeRead.from_created_instance(instance, included)
        
        logger.info(f"[chatbot] ✅ Mensaje creado exitosamente con id={getattr(data, 'id', 'N/A')}")
        return data
    
    @error_handler
    async def create_many(self, records: List[MensajeCreate], session: Optional[AsyncSession] = None) -> int:
        """
        Crea múltiples registros en la tabla mensaje.
        
        Args:
            records: Lista de MensajeCreate con los datos de los registros
            session: Sesión existente (opcional)
            
        Returns:
            Número de registros creados

        """
        logger.info(f"[chatbot] 🔢 Creando {len(records)} registros Mensaje")

        instances = []
        for record in records:
            instances.append(record.to_instance())
        
        if session is not None:
            session.add_all(instances)
            await session.flush()  # Asegura que se generen los IDs si son autoincrement
        else:
            async with self.session_manager.get_session() as session:
                session.add_all(instances)
                await session.flush()  # Asegura que se generen los IDs si son autoincrement

        logger.info(f"[chatbot] ✅ {len(instances)} registros Mensaje creados exitosamente")

        return len(instances)
    
    @error_handler
    async def update(
        self, 
        id: int,
        updated_values: MensajeUpdateValues,
        session: Optional[AsyncSession] = None
    ) -> int:
        """
        Actualiza registros que coincidan con los filtros.
        
        Args:
            id: Identificador del registro
            updated_values: Datos a actualizar
            session: Sesión existente (opcional)
            
        Returns:
            Número de registros actualizados
        """

        update_data = updated_values.to_dict()

        if not update_data:  # Solo actualizar si hay datos
            return 0

        logger.info(f"[chatbot] 🔄 Actualizando Mensaje:")
        logger.info(f"[chatbot]     id={id}")
        logger.info(f"[chatbot]     valores={update_data}")

        query = select(Mensaje)
        
        query = query.where(Mensaje.id == id)

        if session is not None:
            result = await session.execute(query)
            record = result.scalar_one_or_none()
            if record is None:
                return 0
            for key, value in update_data.items():
                setattr(record, key, value)

            await session.flush()  # Aplicar cambios a la base de datos    
        else:
            async with self.session_manager.get_session() as session:
                result = await session.execute(query)
                record = result.scalar_one_or_none()
                if record is None:
                    return 0
                for key, value in update_data.items():
                    setattr(record, key, value)

                await session.flush()  # Aplicar cambios a la base de datos

        logger.info(f"[chatbot]  ✅ 1 registros Mensaje actualizados exitosamente")

        return 1
    
    @error_handler
    async def update_many(
        self,
        payload: MensajeUpdate, 
        session: Optional[AsyncSession] = None
    ) -> int:
        """
        Actualiza múltiples registros basándose en campos de coincidencia.
        
        Args:
            payload: Datos de actualización y filtros
            session: Sesión existente (opcional)
            
        Returns:
            Número total de registros actualizados
        """
        logger.info(f"[chatbot] 🔄 Actualizando múltiples Mensaje con filtros: {payload.filter.to_dict()}, valores: {payload.values.to_dict()}")
            
        filters = payload.filter.to_dict()
        values = payload.values.to_dict()
        
        if not filters and not values:  # Solo actualizar si hay filtros y valores
            return 0

        query = update(Mensaje)
        
        for key, value in filters.items():
            query = query.where(getattr(Mensaje, key) == value)
        
        query = query.values(**values)
                
        if session is not None:
            result = await session.execute(query)
        else:
            async with self.session_manager.get_session() as session:
                result = await session.execute(query)
        
        logger.info(f"[chatbot] ✅ {result.rowcount} registros Mensaje actualizados masivamente exitosamente")

        return result.rowcount
    
    @error_handler
    async def delete(
        self, 
        id: int,
        session: Optional[AsyncSession] = None
    ) -> int:
        """
        Elimina un registro atentiendo a su primary key.
        
        Args:
            id: Filtrar por id para eliminar
            session: Sesión existente (opcional)
            
        Returns:
            Número de registros eliminados
        """
        logger.info(f"[chatbot] 🗑️ Eliminando Mensaje:")
        logger.info(f"[chatbot]    id={id}")

        query = delete(Mensaje)
        
        query = query.where(Mensaje.id == id)

        if session is not None:
            result = await session.execute(query)
        else:
            async with self.session_manager.get_session() as session:
                result = await session.execute(query)

        logger.info(f"[chatbot] ✅ {result.rowcount} registros Mensaje eliminados exitosamente")

        return result.rowcount
    
    @error_handler
    async def delete_many(self, filters_list: List[Dict[str, Any]]) -> int:
        """
        Elimina múltiples registros basándose en una lista de filtros.
        
        Args:
            filters_list: Lista de diccionarios con filtros para cada eliminación
            
        Returns:
            Número total de registros eliminados
        """
        logger.info(f"[chatbot] 🗑️ Eliminando múltiples Mensaje con {len(filters_list)} filtros")

        total_deleted = 0
        async def execute_query(session: AsyncSession) -> int:
            for filters in filters_list:
                query = delete(Mensaje)
                
                for key, value in filters.items():
                    if hasattr(Mensaje, key):
                        query = query.where(getattr(Mensaje, key) == value)
                
                result = await session.execute(query)
                total_deleted += result.rowcount
        
        if session is not None:
            await execute_query(session)
        else:
            async with self.session_manager.get_session() as session:
                await execute_query(session)
        
        logger.info(f"[chatbot] ✅ {total_deleted} registros Mensaje eliminados masivamente exitosamente")
        
        return total_deleted
    
    @error_handler
    async def count(
        self,
        content: Optional[str] = None,
        role: Optional[str] = None,
        min_timestamp: Optional[datetime] = None,
        max_timestamp: Optional[datetime] = None,
        chat_id: Optional[int] = None,
        session: Optional[AsyncSession] = None
    ) -> int:
        """
        Cuenta registros que coincidan con los filtros.
        
        Args:
            - content: Filtrar por content
            - role: Filtrar por role
            - min_timestamp: Filtrar por valor mínimo de timestamp (incluído)
            - max_timestamp: Filtrar por valor máximo de timestamp (incluído)
            - chat_id: Filtrar por chat_id
            - session: Sesión existente (opcional)
            
        Returns:
            Número de registros que coinciden con los filtros
        """
        logger.info(f"[chatbot] 🔢 Contando registros Mensaje con filtros aplicados")
        
        query = select(func.count()).select_from(Mensaje)
        
        # Filters
        filters = {}
        
        if content is not None:
            filters['content'] = content
            if isinstance(content, str) and '%' in content:
                query = query.where(Mensaje.content.ilike(content))
            else:
                query = query.where(Mensaje.content == content)
        if role is not None:
            filters['role'] = role
            if isinstance(role, str) and '%' in role:
                query = query.where(Mensaje.role.ilike(role))
            else:
                query = query.where(Mensaje.role == role)
        if min_timestamp is not None:
            filters['min_timestamp'] = min_timestamp
            query = query.where(Mensaje.timestamp >= min_timestamp)
        if max_timestamp is not None:
            filters['max_timestamp'] = max_timestamp
            query = query.where(Mensaje.timestamp <= max_timestamp)
        if chat_id is not None:
            filters['chat_id'] = chat_id
            query = query.where(Mensaje.chat_id == chat_id)
        
        # Log de parámetros aplicados
        if filters:
            logger.info(f"[chatbot]     filters={filters}")

        if session is not None:
            result = await session.execute(query)
        else:
            async with self.session_manager.get_session() as session:
                result = await session.execute(query)

        count_result = result.scalar() or 0
        logger.info(f"[chatbot] ✅ Conteo Mensaje completado: {count_result} registros")
        return count_result
    
    @error_handler
    async def exists(
        self,
        content: Optional[str] = None,
        role: Optional[str] = None,
        min_timestamp: Optional[datetime] = None,
        max_timestamp: Optional[datetime] = None,
        chat_id: Optional[int] = None,
        session: Optional[AsyncSession] = None
    ) -> bool:
        """
        Verifica si existe al menos un registro que coincida con los filtros.
        
        Args:
            - content: Filtrar por content
            - role: Filtrar por role
            - min_timestamp: Filtrar por valor mínimo de timestamp (incluído)
            - max_timestamp: Filtrar por valor máximo de timestamp (incluído)
            - chat_id: Filtrar por chat_id
            session: Sesión existente (opcional)
            
        Returns:
            True si existe al menos un registro, False en caso contrario
        """
        logger.info(f"[chatbot] ❓ Verificando existencia de registros Mensaje")
        
        records = await self.count(
            content=content,
            role=role,
            min_timestamp=min_timestamp,
            max_timestamp=max_timestamp,
            chat_id=chat_id,
            session=session
        )
        exists_result = records > 0
        logger.info(f"[chatbot] ✅ Verificación Mensaje completada: {'existe' if exists_result else 'no existe'}")
        return exists_result


class TokenUsageAsyncDAO:
    """
    Clase DAO asíncrona para el modelo TokenUsage.
    
    Proporciona operaciones completas de Create, Read, Update y Delete
    para el modelo TokenUsage con soporte para gestión automática
    y manual de sesiones SQLAlchemy.
    
    Características principales:
    - Soporte dual: sesiones automáticas o compartidas
    - Type hints completos para mejor experiencia de desarrollo
    - Manejo robusto de errores con rollback automático
    - Operaciones optimizadas con flush para obtener IDs
    - Filtros flexibles en todas las operaciones de búsqueda
    
    Métodos de lectura:
        find(**filters, session=None): Busca un único registro
        find_many(limit, offset, order_by, order, **filters, session=None): Busca múltiples registros
        count(**filters, session=None): Cuenta registros

    Métodos de escritura:
        create(**data, session=None): Crea un nuevo registro
        create_many(records, session=None): Crea múltiples registros
        update(filters, **data, session=None): Actualiza registros existentes
        delete(**filters, session=None): Elimina registros

    Parámetros de sesión:
        Todos los métodos aceptan un parámetro opcional 'session':
        - Si session=None: Se crea una sesión automática con commit
        - Si session=AsyncSession: Se usa la sesión proporcionada (para transacciones)
    
    Ejemplos de uso:
        ```python
        # Operaciones simples (sesión automática)
        crud = TokenUsageDAO(session_manager)
        found = await crud.find_by_id(1)
        
        # Operaciones transaccionales (sesión compartida)
        async with session_manager.transaction() as session:
            record1 = await crud.create(data="valor1", session=session)
            record2 = await crud.create(data="valor2", session=session)
            # Ambos se crean en la misma transacción
        ```
    """
    
    def __init__(self, session_manager: AsyncSessionManager):
        """
        Inicializa el AsyncDAO con un gestor de sesiones.
        
        Args:
            session_manager: Gestor de sesiones asíncronas
        """
        self.session_manager = session_manager
    
    @error_handler
    async def find(
        self,
        id: int,
        includes: Optional[List[str]] = None,
        session: Optional[AsyncSession] = None
    ) -> Optional[TokenUsageRead]:
        """
        Busca un único registro por primary key con carga optimizada de relaciones.
        
        Args:
            id: Filtrar por id
            includes: Lista de relaciones a incluir (formato: 'relation' o 'relation.nested')
            session: Sesión existente (opcional)
            
        Returns:
            Instancia del modelo o None si no se encuentra
            
        Examples:
            Incluir relación simple

            await dao.find(id=1, includes=['author'])
            
            Incluir relaciones anidadas

            await dao.find(id=1, includes=['author', 'author.posts'])
            
            Múltiples relaciones

            await dao.find(id=1, includes=['author', 'comments', 'tags'])
        """
        logger.info(f"[chatbot] 🔍 Buscando TokenUsage:")
        logger.info(f"[chatbot]     id={id}")
        logger.info(f"[chatbot]     includes={includes}")
        
        # Construir query base
        query = select(TokenUsage)
        
        # Aplicar filtros de búsqueda
        query = query.where(TokenUsage.id == id)
        
        # Aplicar opciones de carga optimizada
        if includes:
            loading_options = get_loading_options(TokenUsage, includes)
            if loading_options:
                query = query.options(*loading_options)
        
        # Ejecutar query
        async def execute_query(session: AsyncSession) -> Optional[TokenUsageRead]:
            result = await session.execute(query)
            instance = result.scalars().first()
            
            if instance:
                logger.info(f"[chatbot] ✅ TokenUsage encontrado exitosamente")
                return TokenUsageRead.from_instance(
                    instance, 
                    includes=includes, 
                    max_depth=5
                )
            else:
                logger.info(f"[chatbot] 📭 TokenUsage no encontrado")
                return None
        
        if session is not None:
            return await execute_query(session)
        else:
            async with self.session_manager.get_session() as session:
                return await execute_query(session)

    @error_handler
    async def find_many(
        self,
        limit: Optional[int] = None, 
        offset: Optional[int] = None,
        order_by: Optional[List[str]] = None,
        order: Literal["ASC", "DESC"] = "ASC",
        prompt_tokens: Optional[int] = None,
        min_prompt_tokens: Optional[int] = None,
        max_prompt_tokens: Optional[int] = None,
        completion_tokens: Optional[int] = None,
        min_completion_tokens: Optional[int] = None,
        max_completion_tokens: Optional[int] = None,
        total_tokens: Optional[int] = None,
        min_total_tokens: Optional[int] = None,
        max_total_tokens: Optional[int] = None,
        model_name: Optional[str] = None,
        provider: Optional[str] = None,
        min_cost_usd: Optional[float] = None,
        max_cost_usd: Optional[float] = None,
        min_timestamp: Optional[datetime] = None,
        max_timestamp: Optional[datetime] = None,
        message_id: Optional[int] = None,
        includes: Optional[List[str]] = None,
        session: Optional[AsyncSession] = None
    ) -> List[TokenUsageRead]:
        """
        Busca múltiples registros con carga optimizada de relaciones.
        
        Args:
            - limit: Límite de registros a retornar
            - offset: Número de registros a saltar
            - order_by: Lista de nombres de columnas para ordenar los resultados
            - order: ASC/DESC (por defecto ASC). Solo se aplica si se especifica order_by.
            - prompt_tokens: Filtrar por prompt_tokens
            - min_prompt_tokens: Filtrar por fecha mínima (incluída)
            - max_prompt_tokens: Filtrar por fecha máxima (incluída)
            - completion_tokens: Filtrar por completion_tokens
            - min_completion_tokens: Filtrar por fecha mínima (incluída)
            - max_completion_tokens: Filtrar por fecha máxima (incluída)
            - total_tokens: Filtrar por total_tokens
            - min_total_tokens: Filtrar por fecha mínima (incluída)
            - max_total_tokens: Filtrar por fecha máxima (incluída)
            - model_name: Filtrar por model_name
            - provider: Filtrar por provider
            - min_cost_usd: Filtrar por valor mínimo de cost_usd (incluído)
            - max_cost_usd: Filtrar por valor máximo de cost_usd (incluído)
            - min_timestamp: Filtrar por valor mínimo de timestamp (incluído)
            - max_timestamp: Filtrar por valor máximo de timestamp (incluído)
            - message_id: Filtrar por message_id
            - includes: Lista de relaciones a incluir (formato: 'relation' o 'relation.nested')
            - session: Sesión existente (opcional)
            
        Returns:
            Lista de instancias del modelo
            
        Examples:
            Búsqueda simple con relaciones

            await dao.find_many(limit=10, includes=['author'])
            
            Relaciones anidadas

            await dao.find_many(
                ..., 
                includes=['author', 'author.profile', 'comments']
            )
            
            Ordenamiento ascendente por columnas

            await dao.find_many(order_by=['created_at', 'name'], order='ASC')
            
            Ordenamiento descendente por columnas

            await dao.find_many(order_by=['created_at', 'name'], order='DESC')
            
            Paginación

            # Obtener los primeros 10 registros
            await dao.find_many(limit=10)
            
            # Obtener los últimos 5 registros ordenados por fecha
            await dao.find_many(limit=5, order_by=['created_at'], order='DESC')
            
            # Paginación con offset
            await dao.find_many(limit=10, offset=20)
            
        """
        logger.info(f"[chatbot] 🔍 Buscando múltiples TokenUsage:")
        logger.info(f"[chatbot]     limit={limit}")
        logger.info(f"[chatbot]     offset={offset}")
        logger.info(f"[chatbot]     order_by={order_by}")
        logger.info(f"[chatbot]     order={order}")
        logger.info(f"[chatbot]     includes={includes}")
        
        # Construir query base
        query = select(TokenUsage)

        # Filters
        filters = {}
        
        # Aplicar filtros de búsqueda
        if prompt_tokens is not None:
            filters['prompt_tokens'] = prompt_tokens
            query = query.where(TokenUsage.prompt_tokens == prompt_tokens)
        if min_prompt_tokens is not None:
            filters['min_prompt_tokens'] = min_prompt_tokens
            query = query.where(TokenUsage.prompt_tokens >= min_prompt_tokens)
        if max_prompt_tokens is not None:
            filters['max_prompt_tokens'] = max_prompt_tokens
            query = query.where(TokenUsage.prompt_tokens <= max_prompt_tokens)
        if completion_tokens is not None:
            filters['completion_tokens'] = completion_tokens
            query = query.where(TokenUsage.completion_tokens == completion_tokens)
        if min_completion_tokens is not None:
            filters['min_completion_tokens'] = min_completion_tokens
            query = query.where(TokenUsage.completion_tokens >= min_completion_tokens)
        if max_completion_tokens is not None:
            filters['max_completion_tokens'] = max_completion_tokens
            query = query.where(TokenUsage.completion_tokens <= max_completion_tokens)
        if total_tokens is not None:
            filters['total_tokens'] = total_tokens
            query = query.where(TokenUsage.total_tokens == total_tokens)
        if min_total_tokens is not None:
            filters['min_total_tokens'] = min_total_tokens
            query = query.where(TokenUsage.total_tokens >= min_total_tokens)
        if max_total_tokens is not None:
            filters['max_total_tokens'] = max_total_tokens
            query = query.where(TokenUsage.total_tokens <= max_total_tokens)
        if model_name is not None:
            filters['model_name'] = model_name
            if isinstance(model_name, str) and '%' in model_name:
                query = query.where(TokenUsage.model_name.ilike(model_name))
            else:
                query = query.where(TokenUsage.model_name == model_name)
        if provider is not None:
            filters['provider'] = provider
            if isinstance(provider, str) and '%' in provider:
                query = query.where(TokenUsage.provider.ilike(provider))
            else:
                query = query.where(TokenUsage.provider == provider)
        if min_cost_usd is not None:
            filters['min_cost_usd'] = min_cost_usd
            query = query.where(TokenUsage.cost_usd >= min_cost_usd)
        if max_cost_usd is not None:
            filters['max_cost_usd'] = max_cost_usd
            query = query.where(TokenUsage.cost_usd <= max_cost_usd)
        if min_timestamp is not None:
            filters['min_timestamp'] = min_timestamp
            query = query.where(TokenUsage.timestamp >= min_timestamp)
        if max_timestamp is not None:
            filters['max_timestamp'] = max_timestamp
            query = query.where(TokenUsage.timestamp <= max_timestamp)
        if message_id is not None:
            filters['message_id'] = message_id
            query = query.where(TokenUsage.message_id == message_id)
        
        # Log de parámetros aplicados
        if filters:
            logger.info(f"[chatbot]     filters={filters}")
        
        # Aplicar opciones de carga optimizada
        if includes:
            loading_options = get_loading_options(TokenUsage, includes)
            if loading_options:
                query = query.options(*loading_options)

        # Aplicar ordenamiento
        if order_by:
            for column_name in order_by:
                if hasattr(TokenUsage, column_name):
                    column = getattr(TokenUsage, column_name)
                    if order.upper() == "DESC":
                        query = query.order_by(column.desc())
                    elif order.upper() == "ASC":
                        query = query.order_by(column.asc())
                else:
                    logger.warning(f"[chatbot] ⚠️ Columna '{column_name}' no existe en modelo TokenUsage, ignorando en order_by")
        
        # Aplicar límite (solo valores positivos)
        if limit is not None and limit > 0:
            query = query.limit(limit)

        # Aplicar paginación
        if offset is not None:
            query = query.offset(offset)

        # Ejecutar query
        async def execute_query(session: AsyncSession) -> List[TokenUsageRead]:
            results = await session.execute(query)
            instances = results.scalars().all()
            
            logger.info(f"[chatbot] ✅ Encontrados {len(instances)} registros TokenUsage")
            
            return [
                TokenUsageRead.from_instance(
                    instance, 
                    includes=includes, 
                    max_depth=5
                ) 
                for instance in instances
            ]
        
        if session is not None:
            return await execute_query(session)
        else:
            async with self.session_manager.get_session() as session:
                return await execute_query(session)
    
    @error_handler
    async def create(
        self, 
        token_usage: TokenUsageCreate,
        session: Optional[AsyncSession] = None
    ) -> TokenUsageRead:
        """
        Crea un nuevo registro.
        
        Args:
            token_usage: Datos del token_usage a crear
            session: Sesión existente (opcional)
            
        Returns:
            Instancia del modelo creado
        """
        logger.info(f"[chatbot] 🆕 Creando nuevo TokenUsage")

        instance = token_usage.to_instance()

        if session is not None:
            session.add(instance)
            await session.flush()  # Asegura que se genere el ID si es autoincrement
            included = await load_relationships_from_dto(session, instance, token_usage)
            data = TokenUsageRead.from_created_instance(instance, included)
        else:
            async with self.session_manager.get_session() as session:
                session.add(instance)
                await session.flush()  # Asegura que se genere el ID si es autoincrement
                included = await load_relationships_from_dto(session, instance, token_usage)
                data = TokenUsageRead.from_created_instance(instance, included)
        
        logger.info(f"[chatbot] ✅ TokenUsage creado exitosamente con id={getattr(data, 'id', 'N/A')}")
        return data
    
    @error_handler
    async def create_many(self, records: List[TokenUsageCreate], session: Optional[AsyncSession] = None) -> int:
        """
        Crea múltiples registros en la tabla token_usage.
        
        Args:
            records: Lista de TokenUsageCreate con los datos de los registros
            session: Sesión existente (opcional)
            
        Returns:
            Número de registros creados

        """
        logger.info(f"[chatbot] 🔢 Creando {len(records)} registros TokenUsage")

        instances = []
        for record in records:
            instances.append(record.to_instance())
        
        if session is not None:
            session.add_all(instances)
            await session.flush()  # Asegura que se generen los IDs si son autoincrement
        else:
            async with self.session_manager.get_session() as session:
                session.add_all(instances)
                await session.flush()  # Asegura que se generen los IDs si son autoincrement

        logger.info(f"[chatbot] ✅ {len(instances)} registros TokenUsage creados exitosamente")

        return len(instances)
    
    @error_handler
    async def update(
        self, 
        id: int,
        updated_values: TokenUsageUpdateValues,
        session: Optional[AsyncSession] = None
    ) -> int:
        """
        Actualiza registros que coincidan con los filtros.
        
        Args:
            id: Identificador del registro
            updated_values: Datos a actualizar
            session: Sesión existente (opcional)
            
        Returns:
            Número de registros actualizados
        """

        update_data = updated_values.to_dict()

        if not update_data:  # Solo actualizar si hay datos
            return 0

        logger.info(f"[chatbot] 🔄 Actualizando TokenUsage:")
        logger.info(f"[chatbot]     id={id}")
        logger.info(f"[chatbot]     valores={update_data}")

        query = select(TokenUsage)
        
        query = query.where(TokenUsage.id == id)

        if session is not None:
            result = await session.execute(query)
            record = result.scalar_one_or_none()
            if record is None:
                return 0
            for key, value in update_data.items():
                setattr(record, key, value)

            await session.flush()  # Aplicar cambios a la base de datos    
        else:
            async with self.session_manager.get_session() as session:
                result = await session.execute(query)
                record = result.scalar_one_or_none()
                if record is None:
                    return 0
                for key, value in update_data.items():
                    setattr(record, key, value)

                await session.flush()  # Aplicar cambios a la base de datos

        logger.info(f"[chatbot]  ✅ 1 registros TokenUsage actualizados exitosamente")

        return 1
    
    @error_handler
    async def update_many(
        self,
        payload: TokenUsageUpdate, 
        session: Optional[AsyncSession] = None
    ) -> int:
        """
        Actualiza múltiples registros basándose en campos de coincidencia.
        
        Args:
            payload: Datos de actualización y filtros
            session: Sesión existente (opcional)
            
        Returns:
            Número total de registros actualizados
        """
        logger.info(f"[chatbot] 🔄 Actualizando múltiples TokenUsage con filtros: {payload.filter.to_dict()}, valores: {payload.values.to_dict()}")
            
        filters = payload.filter.to_dict()
        values = payload.values.to_dict()
        
        if not filters and not values:  # Solo actualizar si hay filtros y valores
            return 0

        query = update(TokenUsage)
        
        for key, value in filters.items():
            query = query.where(getattr(TokenUsage, key) == value)
        
        query = query.values(**values)
                
        if session is not None:
            result = await session.execute(query)
        else:
            async with self.session_manager.get_session() as session:
                result = await session.execute(query)
        
        logger.info(f"[chatbot] ✅ {result.rowcount} registros TokenUsage actualizados masivamente exitosamente")

        return result.rowcount
    
    @error_handler
    async def delete(
        self, 
        id: int,
        session: Optional[AsyncSession] = None
    ) -> int:
        """
        Elimina un registro atentiendo a su primary key.
        
        Args:
            id: Filtrar por id para eliminar
            session: Sesión existente (opcional)
            
        Returns:
            Número de registros eliminados
        """
        logger.info(f"[chatbot] 🗑️ Eliminando TokenUsage:")
        logger.info(f"[chatbot]    id={id}")

        query = delete(TokenUsage)
        
        query = query.where(TokenUsage.id == id)

        if session is not None:
            result = await session.execute(query)
        else:
            async with self.session_manager.get_session() as session:
                result = await session.execute(query)

        logger.info(f"[chatbot] ✅ {result.rowcount} registros TokenUsage eliminados exitosamente")

        return result.rowcount
    
    @error_handler
    async def delete_many(self, filters_list: List[Dict[str, Any]]) -> int:
        """
        Elimina múltiples registros basándose en una lista de filtros.
        
        Args:
            filters_list: Lista de diccionarios con filtros para cada eliminación
            
        Returns:
            Número total de registros eliminados
        """
        logger.info(f"[chatbot] 🗑️ Eliminando múltiples TokenUsage con {len(filters_list)} filtros")

        total_deleted = 0
        async def execute_query(session: AsyncSession) -> int:
            for filters in filters_list:
                query = delete(TokenUsage)
                
                for key, value in filters.items():
                    if hasattr(TokenUsage, key):
                        query = query.where(getattr(TokenUsage, key) == value)
                
                result = await session.execute(query)
                total_deleted += result.rowcount
        
        if session is not None:
            await execute_query(session)
        else:
            async with self.session_manager.get_session() as session:
                await execute_query(session)
        
        logger.info(f"[chatbot] ✅ {total_deleted} registros TokenUsage eliminados masivamente exitosamente")
        
        return total_deleted
    
    @error_handler
    async def count(
        self,
        prompt_tokens: Optional[int] = None,
        min_prompt_tokens: Optional[int] = None,
        max_prompt_tokens: Optional[int] = None,
        completion_tokens: Optional[int] = None,
        min_completion_tokens: Optional[int] = None,
        max_completion_tokens: Optional[int] = None,
        total_tokens: Optional[int] = None,
        min_total_tokens: Optional[int] = None,
        max_total_tokens: Optional[int] = None,
        model_name: Optional[str] = None,
        provider: Optional[str] = None,
        min_cost_usd: Optional[float] = None,
        max_cost_usd: Optional[float] = None,
        min_timestamp: Optional[datetime] = None,
        max_timestamp: Optional[datetime] = None,
        message_id: Optional[int] = None,
        session: Optional[AsyncSession] = None
    ) -> int:
        """
        Cuenta registros que coincidan con los filtros.
        
        Args:
            - prompt_tokens: Filtrar por prompt_tokens
            - min_prompt_tokens: Filtrar por fecha mínima (incluída)
            - max_prompt_tokens: Filtrar por fecha máxima (incluída)
            - completion_tokens: Filtrar por completion_tokens
            - min_completion_tokens: Filtrar por fecha mínima (incluída)
            - max_completion_tokens: Filtrar por fecha máxima (incluída)
            - total_tokens: Filtrar por total_tokens
            - min_total_tokens: Filtrar por fecha mínima (incluída)
            - max_total_tokens: Filtrar por fecha máxima (incluída)
            - model_name: Filtrar por model_name
            - provider: Filtrar por provider
            - min_cost_usd: Filtrar por valor mínimo de cost_usd (incluído)
            - max_cost_usd: Filtrar por valor máximo de cost_usd (incluído)
            - min_timestamp: Filtrar por valor mínimo de timestamp (incluído)
            - max_timestamp: Filtrar por valor máximo de timestamp (incluído)
            - message_id: Filtrar por message_id
            - session: Sesión existente (opcional)
            
        Returns:
            Número de registros que coinciden con los filtros
        """
        logger.info(f"[chatbot] 🔢 Contando registros TokenUsage con filtros aplicados")
        
        query = select(func.count()).select_from(TokenUsage)
        
        # Filters
        filters = {}
        
        if prompt_tokens is not None:
            filters['prompt_tokens'] = prompt_tokens
            query = query.where(TokenUsage.prompt_tokens == prompt_tokens)
        if min_prompt_tokens is not None:
            filters['min_prompt_tokens'] = min_prompt_tokens
            query = query.where(TokenUsage.prompt_tokens >= min_prompt_tokens)
        if max_prompt_tokens is not None:
            filters['max_prompt_tokens'] = max_prompt_tokens
            query = query.where(TokenUsage.prompt_tokens <= max_prompt_tokens)
        if completion_tokens is not None:
            filters['completion_tokens'] = completion_tokens
            query = query.where(TokenUsage.completion_tokens == completion_tokens)
        if min_completion_tokens is not None:
            filters['min_completion_tokens'] = min_completion_tokens
            query = query.where(TokenUsage.completion_tokens >= min_completion_tokens)
        if max_completion_tokens is not None:
            filters['max_completion_tokens'] = max_completion_tokens
            query = query.where(TokenUsage.completion_tokens <= max_completion_tokens)
        if total_tokens is not None:
            filters['total_tokens'] = total_tokens
            query = query.where(TokenUsage.total_tokens == total_tokens)
        if min_total_tokens is not None:
            filters['min_total_tokens'] = min_total_tokens
            query = query.where(TokenUsage.total_tokens >= min_total_tokens)
        if max_total_tokens is not None:
            filters['max_total_tokens'] = max_total_tokens
            query = query.where(TokenUsage.total_tokens <= max_total_tokens)
        if model_name is not None:
            filters['model_name'] = model_name
            if isinstance(model_name, str) and '%' in model_name:
                query = query.where(TokenUsage.model_name.ilike(model_name))
            else:
                query = query.where(TokenUsage.model_name == model_name)
        if provider is not None:
            filters['provider'] = provider
            if isinstance(provider, str) and '%' in provider:
                query = query.where(TokenUsage.provider.ilike(provider))
            else:
                query = query.where(TokenUsage.provider == provider)
        if min_cost_usd is not None:
            filters['min_cost_usd'] = min_cost_usd
            query = query.where(TokenUsage.cost_usd >= min_cost_usd)
        if max_cost_usd is not None:
            filters['max_cost_usd'] = max_cost_usd
            query = query.where(TokenUsage.cost_usd <= max_cost_usd)
        if min_timestamp is not None:
            filters['min_timestamp'] = min_timestamp
            query = query.where(TokenUsage.timestamp >= min_timestamp)
        if max_timestamp is not None:
            filters['max_timestamp'] = max_timestamp
            query = query.where(TokenUsage.timestamp <= max_timestamp)
        if message_id is not None:
            filters['message_id'] = message_id
            query = query.where(TokenUsage.message_id == message_id)
        
        # Log de parámetros aplicados
        if filters:
            logger.info(f"[chatbot]     filters={filters}")

        if session is not None:
            result = await session.execute(query)
        else:
            async with self.session_manager.get_session() as session:
                result = await session.execute(query)

        count_result = result.scalar() or 0
        logger.info(f"[chatbot] ✅ Conteo TokenUsage completado: {count_result} registros")
        return count_result
    
    @error_handler
    async def exists(
        self,
        prompt_tokens: Optional[int] = None,
        min_prompt_tokens: Optional[int] = None,
        max_prompt_tokens: Optional[int] = None,
        completion_tokens: Optional[int] = None,
        min_completion_tokens: Optional[int] = None,
        max_completion_tokens: Optional[int] = None,
        total_tokens: Optional[int] = None,
        min_total_tokens: Optional[int] = None,
        max_total_tokens: Optional[int] = None,
        model_name: Optional[str] = None,
        provider: Optional[str] = None,
        min_cost_usd: Optional[float] = None,
        max_cost_usd: Optional[float] = None,
        min_timestamp: Optional[datetime] = None,
        max_timestamp: Optional[datetime] = None,
        message_id: Optional[int] = None,
        session: Optional[AsyncSession] = None
    ) -> bool:
        """
        Verifica si existe al menos un registro que coincida con los filtros.
        
        Args:
            - prompt_tokens: Filtrar por prompt_tokens
            - min_prompt_tokens: Filtrar por fecha mínima (incluída)
            - max_prompt_tokens: Filtrar por fecha máxima (incluída)
            - completion_tokens: Filtrar por completion_tokens
            - min_completion_tokens: Filtrar por fecha mínima (incluída)
            - max_completion_tokens: Filtrar por fecha máxima (incluída)
            - total_tokens: Filtrar por total_tokens
            - min_total_tokens: Filtrar por fecha mínima (incluída)
            - max_total_tokens: Filtrar por fecha máxima (incluída)
            - model_name: Filtrar por model_name
            - provider: Filtrar por provider
            - min_cost_usd: Filtrar por valor mínimo de cost_usd (incluído)
            - max_cost_usd: Filtrar por valor máximo de cost_usd (incluído)
            - min_timestamp: Filtrar por valor mínimo de timestamp (incluído)
            - max_timestamp: Filtrar por valor máximo de timestamp (incluído)
            - message_id: Filtrar por message_id
            session: Sesión existente (opcional)
            
        Returns:
            True si existe al menos un registro, False en caso contrario
        """
        logger.info(f"[chatbot] ❓ Verificando existencia de registros TokenUsage")
        
        records = await self.count(
            prompt_tokens=prompt_tokens,
            min_prompt_tokens=min_prompt_tokens,
            max_prompt_tokens=max_prompt_tokens,
            completion_tokens=completion_tokens,
            min_completion_tokens=min_completion_tokens,
            max_completion_tokens=max_completion_tokens,
            total_tokens=total_tokens,
            min_total_tokens=min_total_tokens,
            max_total_tokens=max_total_tokens,
            model_name=model_name,
            provider=provider,
            min_cost_usd=min_cost_usd,
            max_cost_usd=max_cost_usd,
            min_timestamp=min_timestamp,
            max_timestamp=max_timestamp,
            message_id=message_id,
            session=session
        )
        exists_result = records > 0
        logger.info(f"[chatbot] ✅ Verificación TokenUsage completada: {'existe' if exists_result else 'no existe'}")
        return exists_result


class UserStatsAsyncDAO:
    """
    Clase DAO asíncrona para el modelo UserStats.
    
    Proporciona operaciones completas de Create, Read, Update y Delete
    para el modelo UserStats con soporte para gestión automática
    y manual de sesiones SQLAlchemy.
    
    Características principales:
    - Soporte dual: sesiones automáticas o compartidas
    - Type hints completos para mejor experiencia de desarrollo
    - Manejo robusto de errores con rollback automático
    - Operaciones optimizadas con flush para obtener IDs
    - Filtros flexibles en todas las operaciones de búsqueda
    
    Métodos de lectura:
        find(**filters, session=None): Busca un único registro
        find_many(limit, offset, order_by, order, **filters, session=None): Busca múltiples registros
        count(**filters, session=None): Cuenta registros

    Parámetros de sesión:
        Todos los métodos aceptan un parámetro opcional 'session':
        - Si session=None: Se crea una sesión automática con commit
        - Si session=AsyncSession: Se usa la sesión proporcionada (para transacciones)
    
    Ejemplos de uso:
        ```python
        # Operaciones simples (sesión automática)
        crud = UserStatsDAO(session_manager)
        record = await crud.create(username="valor")
        found = await crud.find_by_id(1)
        
        # Operaciones transaccionales (sesión compartida)
        async with session_manager.transaction() as session:
            record1 = await crud.create(data="valor1", session=session)
            record2 = await crud.create(data="valor2", session=session)
            # Ambos se crean en la misma transacción
        ```
    """
    
    def __init__(self, session_manager: AsyncSessionManager):
        """
        Inicializa el AsyncDAO con un gestor de sesiones.
        
        Args:
            session_manager: Gestor de sesiones asíncronas
        """
        self.session_manager = session_manager
    

    @error_handler
    async def find_many(
        self,
        limit: Optional[int] = None, 
        offset: Optional[int] = None,
        order_by: Optional[List[str]] = None,
        order: Literal["ASC", "DESC"] = "ASC",
        username: Optional[str] = None,
        email: Optional[str] = None,
        total_chats: Optional[int] = None,
        min_total_chats: Optional[int] = None,
        max_total_chats: Optional[int] = None,
        active_chats: Optional[int] = None,
        min_active_chats: Optional[int] = None,
        max_active_chats: Optional[int] = None,
        total_messages: Optional[int] = None,
        min_total_messages: Optional[int] = None,
        max_total_messages: Optional[int] = None,
        min_created_at: Optional[datetime] = None,
        max_created_at: Optional[datetime] = None,
        min_last_activity: Optional[datetime] = None,
        max_last_activity: Optional[datetime] = None,
        includes: Optional[List[str]] = None,
        session: Optional[AsyncSession] = None
    ) -> List[UserStatsRead]:
        """
        Busca múltiples registros con carga optimizada de relaciones.
        
        Args:
            - limit: Límite de registros a retornar
            - offset: Número de registros a saltar
            - order_by: Lista de nombres de columnas para ordenar los resultados
            - order: ASC/DESC (por defecto ASC). Solo se aplica si se especifica order_by.
            - username: Filtrar por username
            - email: Filtrar por email
            - total_chats: Filtrar por total_chats
            - min_total_chats: Filtrar por fecha mínima (incluída)
            - max_total_chats: Filtrar por fecha máxima (incluída)
            - active_chats: Filtrar por active_chats
            - min_active_chats: Filtrar por fecha mínima (incluída)
            - max_active_chats: Filtrar por fecha máxima (incluída)
            - total_messages: Filtrar por total_messages
            - min_total_messages: Filtrar por fecha mínima (incluída)
            - max_total_messages: Filtrar por fecha máxima (incluída)
            - min_created_at: Filtrar por valor mínimo de created_at (incluído)
            - max_created_at: Filtrar por valor máximo de created_at (incluído)
            - min_last_activity: Filtrar por valor mínimo de last_activity (incluído)
            - max_last_activity: Filtrar por valor máximo de last_activity (incluído)
            - includes: Lista de relaciones a incluir (formato: 'relation' o 'relation.nested')
            - session: Sesión existente (opcional)
            
        Returns:
            Lista de instancias del modelo
            
        Examples:
            Búsqueda simple con relaciones

            await dao.find_many(limit=10, includes=['author'])
            
            Relaciones anidadas

            await dao.find_many(
                ..., 
                includes=['author', 'author.profile', 'comments']
            )
            
            Ordenamiento ascendente por columnas

            await dao.find_many(order_by=['created_at', 'name'], order='ASC')
            
            Ordenamiento descendente por columnas

            await dao.find_many(order_by=['created_at', 'name'], order='DESC')
            
            Paginación

            # Obtener los primeros 10 registros
            await dao.find_many(limit=10)
            
            # Obtener los últimos 5 registros ordenados por fecha
            await dao.find_many(limit=5, order_by=['created_at'], order='DESC')
            
            # Paginación con offset
            await dao.find_many(limit=10, offset=20)
            
        """
        logger.info(f"[chatbot] 🔍 Buscando múltiples UserStats:")
        logger.info(f"[chatbot]     limit={limit}")
        logger.info(f"[chatbot]     offset={offset}")
        logger.info(f"[chatbot]     order_by={order_by}")
        logger.info(f"[chatbot]     order={order}")
        logger.info(f"[chatbot]     includes={includes}")
        
        # Construir query base
        query = select(UserStats)

        # Filters
        filters = {}
        
        # Aplicar filtros de búsqueda
        if username is not None:
            filters['username'] = username
            if isinstance(username, str) and '%' in username:
                query = query.where(UserStats.username.ilike(username))
            else:
                query = query.where(UserStats.username == username)
        if email is not None:
            filters['email'] = email
            if isinstance(email, str) and '%' in email:
                query = query.where(UserStats.email.ilike(email))
            else:
                query = query.where(UserStats.email == email)
        if total_chats is not None:
            filters['total_chats'] = total_chats
            query = query.where(UserStats.total_chats == total_chats)
        if min_total_chats is not None:
            filters['min_total_chats'] = min_total_chats
            query = query.where(UserStats.total_chats >= min_total_chats)
        if max_total_chats is not None:
            filters['max_total_chats'] = max_total_chats
            query = query.where(UserStats.total_chats <= max_total_chats)
        if active_chats is not None:
            filters['active_chats'] = active_chats
            query = query.where(UserStats.active_chats == active_chats)
        if min_active_chats is not None:
            filters['min_active_chats'] = min_active_chats
            query = query.where(UserStats.active_chats >= min_active_chats)
        if max_active_chats is not None:
            filters['max_active_chats'] = max_active_chats
            query = query.where(UserStats.active_chats <= max_active_chats)
        if total_messages is not None:
            filters['total_messages'] = total_messages
            query = query.where(UserStats.total_messages == total_messages)
        if min_total_messages is not None:
            filters['min_total_messages'] = min_total_messages
            query = query.where(UserStats.total_messages >= min_total_messages)
        if max_total_messages is not None:
            filters['max_total_messages'] = max_total_messages
            query = query.where(UserStats.total_messages <= max_total_messages)
        if min_created_at is not None:
            filters['min_created_at'] = min_created_at
            query = query.where(UserStats.created_at >= min_created_at)
        if max_created_at is not None:
            filters['max_created_at'] = max_created_at
            query = query.where(UserStats.created_at <= max_created_at)
        if min_last_activity is not None:
            filters['min_last_activity'] = min_last_activity
            query = query.where(UserStats.last_activity >= min_last_activity)
        if max_last_activity is not None:
            filters['max_last_activity'] = max_last_activity
            query = query.where(UserStats.last_activity <= max_last_activity)
        
        # Log de parámetros aplicados
        if filters:
            logger.info(f"[chatbot]     filters={filters}")
        
        # Aplicar opciones de carga optimizada
        if includes:
            loading_options = get_loading_options(UserStats, includes)
            if loading_options:
                query = query.options(*loading_options)

        # Aplicar ordenamiento
        if order_by:
            for column_name in order_by:
                if hasattr(UserStats, column_name):
                    column = getattr(UserStats, column_name)
                    if order.upper() == "DESC":
                        query = query.order_by(column.desc())
                    elif order.upper() == "ASC":
                        query = query.order_by(column.asc())
                else:
                    logger.warning(f"[chatbot] ⚠️ Columna '{column_name}' no existe en modelo UserStats, ignorando en order_by")
        
        # Aplicar límite (solo valores positivos)
        if limit is not None and limit > 0:
            query = query.limit(limit)

        # Aplicar paginación
        if offset is not None:
            query = query.offset(offset)

        # Ejecutar query
        async def execute_query(session: AsyncSession) -> List[UserStatsRead]:
            results = await session.execute(query)
            instances = results.scalars().all()
            
            logger.info(f"[chatbot] ✅ Encontrados {len(instances)} registros UserStats")
            
            return [
                UserStatsRead.from_instance(
                    instance, 
                    includes=includes, 
                    max_depth=5
                ) 
                for instance in instances
            ]
        
        if session is not None:
            return await execute_query(session)
        else:
            async with self.session_manager.get_session() as session:
                return await execute_query(session)
    

class TokenConsumptionStatsAsyncDAO:
    """
    Clase DAO asíncrona para el modelo TokenConsumptionStats.
    
    Proporciona operaciones completas de Create, Read, Update y Delete
    para el modelo TokenConsumptionStats con soporte para gestión automática
    y manual de sesiones SQLAlchemy.
    
    Características principales:
    - Soporte dual: sesiones automáticas o compartidas
    - Type hints completos para mejor experiencia de desarrollo
    - Manejo robusto de errores con rollback automático
    - Operaciones optimizadas con flush para obtener IDs
    - Filtros flexibles en todas las operaciones de búsqueda
    
    Métodos de lectura:
        find(**filters, session=None): Busca un único registro
        find_many(limit, offset, order_by, order, **filters, session=None): Busca múltiples registros
        count(**filters, session=None): Cuenta registros

    Parámetros de sesión:
        Todos los métodos aceptan un parámetro opcional 'session':
        - Si session=None: Se crea una sesión automática con commit
        - Si session=AsyncSession: Se usa la sesión proporcionada (para transacciones)
    
    Ejemplos de uso:
        ```python
        # Operaciones simples (sesión automática)
        crud = TokenConsumptionStatsDAO(session_manager)
        record = await crud.create(username="valor")
        found = await crud.find_by_id(1)
        
        # Operaciones transaccionales (sesión compartida)
        async with session_manager.transaction() as session:
            record1 = await crud.create(data="valor1", session=session)
            record2 = await crud.create(data="valor2", session=session)
            # Ambos se crean en la misma transacción
        ```
    """
    
    def __init__(self, session_manager: AsyncSessionManager):
        """
        Inicializa el AsyncDAO con un gestor de sesiones.
        
        Args:
            session_manager: Gestor de sesiones asíncronas
        """
        self.session_manager = session_manager
    

    @error_handler
    async def find_many(
        self,
        limit: Optional[int] = None, 
        offset: Optional[int] = None,
        order_by: Optional[List[str]] = None,
        order: Literal["ASC", "DESC"] = "ASC",
        username: Optional[str] = None,
        min_date: Optional[datetime] = None,
        max_date: Optional[datetime] = None,
        total_prompt_tokens: Optional[int] = None,
        min_total_prompt_tokens: Optional[int] = None,
        max_total_prompt_tokens: Optional[int] = None,
        total_completion_tokens: Optional[int] = None,
        min_total_completion_tokens: Optional[int] = None,
        max_total_completion_tokens: Optional[int] = None,
        total_tokens: Optional[int] = None,
        min_total_tokens: Optional[int] = None,
        max_total_tokens: Optional[int] = None,
        min_total_cost_usd: Optional[float] = None,
        max_total_cost_usd: Optional[float] = None,
        chat_count: Optional[int] = None,
        min_chat_count: Optional[int] = None,
        max_chat_count: Optional[int] = None,
        most_used_model: Optional[str] = None,
        most_used_provider: Optional[str] = None,
        includes: Optional[List[str]] = None,
        session: Optional[AsyncSession] = None
    ) -> List[TokenConsumptionStatsRead]:
        """
        Busca múltiples registros con carga optimizada de relaciones.
        
        Args:
            - limit: Límite de registros a retornar
            - offset: Número de registros a saltar
            - order_by: Lista de nombres de columnas para ordenar los resultados
            - order: ASC/DESC (por defecto ASC). Solo se aplica si se especifica order_by.
            - username: Filtrar por username
            - min_date: Filtrar por valor mínimo de date (incluído)
            - max_date: Filtrar por valor máximo de date (incluído)
            - total_prompt_tokens: Filtrar por total_prompt_tokens
            - min_total_prompt_tokens: Filtrar por fecha mínima (incluída)
            - max_total_prompt_tokens: Filtrar por fecha máxima (incluída)
            - total_completion_tokens: Filtrar por total_completion_tokens
            - min_total_completion_tokens: Filtrar por fecha mínima (incluída)
            - max_total_completion_tokens: Filtrar por fecha máxima (incluída)
            - total_tokens: Filtrar por total_tokens
            - min_total_tokens: Filtrar por fecha mínima (incluída)
            - max_total_tokens: Filtrar por fecha máxima (incluída)
            - min_total_cost_usd: Filtrar por valor mínimo de total_cost_usd (incluído)
            - max_total_cost_usd: Filtrar por valor máximo de total_cost_usd (incluído)
            - chat_count: Filtrar por chat_count
            - min_chat_count: Filtrar por fecha mínima (incluída)
            - max_chat_count: Filtrar por fecha máxima (incluída)
            - most_used_model: Filtrar por most_used_model
            - most_used_provider: Filtrar por most_used_provider
            - includes: Lista de relaciones a incluir (formato: 'relation' o 'relation.nested')
            - session: Sesión existente (opcional)
            
        Returns:
            Lista de instancias del modelo
            
        Examples:
            Búsqueda simple con relaciones

            await dao.find_many(limit=10, includes=['author'])
            
            Relaciones anidadas

            await dao.find_many(
                ..., 
                includes=['author', 'author.profile', 'comments']
            )
            
            Ordenamiento ascendente por columnas

            await dao.find_many(order_by=['created_at', 'name'], order='ASC')
            
            Ordenamiento descendente por columnas

            await dao.find_many(order_by=['created_at', 'name'], order='DESC')
            
            Paginación

            # Obtener los primeros 10 registros
            await dao.find_many(limit=10)
            
            # Obtener los últimos 5 registros ordenados por fecha
            await dao.find_many(limit=5, order_by=['created_at'], order='DESC')
            
            # Paginación con offset
            await dao.find_many(limit=10, offset=20)
            
        """
        logger.info(f"[chatbot] 🔍 Buscando múltiples TokenConsumptionStats:")
        logger.info(f"[chatbot]     limit={limit}")
        logger.info(f"[chatbot]     offset={offset}")
        logger.info(f"[chatbot]     order_by={order_by}")
        logger.info(f"[chatbot]     order={order}")
        logger.info(f"[chatbot]     includes={includes}")
        
        # Construir query base
        query = select(TokenConsumptionStats)

        # Filters
        filters = {}
        
        # Aplicar filtros de búsqueda
        if username is not None:
            filters['username'] = username
            if isinstance(username, str) and '%' in username:
                query = query.where(TokenConsumptionStats.username.ilike(username))
            else:
                query = query.where(TokenConsumptionStats.username == username)
        if min_date is not None:
            filters['min_date'] = min_date
            query = query.where(TokenConsumptionStats.date >= min_date)
        if max_date is not None:
            filters['max_date'] = max_date
            query = query.where(TokenConsumptionStats.date <= max_date)
        if total_prompt_tokens is not None:
            filters['total_prompt_tokens'] = total_prompt_tokens
            query = query.where(TokenConsumptionStats.total_prompt_tokens == total_prompt_tokens)
        if min_total_prompt_tokens is not None:
            filters['min_total_prompt_tokens'] = min_total_prompt_tokens
            query = query.where(TokenConsumptionStats.total_prompt_tokens >= min_total_prompt_tokens)
        if max_total_prompt_tokens is not None:
            filters['max_total_prompt_tokens'] = max_total_prompt_tokens
            query = query.where(TokenConsumptionStats.total_prompt_tokens <= max_total_prompt_tokens)
        if total_completion_tokens is not None:
            filters['total_completion_tokens'] = total_completion_tokens
            query = query.where(TokenConsumptionStats.total_completion_tokens == total_completion_tokens)
        if min_total_completion_tokens is not None:
            filters['min_total_completion_tokens'] = min_total_completion_tokens
            query = query.where(TokenConsumptionStats.total_completion_tokens >= min_total_completion_tokens)
        if max_total_completion_tokens is not None:
            filters['max_total_completion_tokens'] = max_total_completion_tokens
            query = query.where(TokenConsumptionStats.total_completion_tokens <= max_total_completion_tokens)
        if total_tokens is not None:
            filters['total_tokens'] = total_tokens
            query = query.where(TokenConsumptionStats.total_tokens == total_tokens)
        if min_total_tokens is not None:
            filters['min_total_tokens'] = min_total_tokens
            query = query.where(TokenConsumptionStats.total_tokens >= min_total_tokens)
        if max_total_tokens is not None:
            filters['max_total_tokens'] = max_total_tokens
            query = query.where(TokenConsumptionStats.total_tokens <= max_total_tokens)
        if min_total_cost_usd is not None:
            filters['min_total_cost_usd'] = min_total_cost_usd
            query = query.where(TokenConsumptionStats.total_cost_usd >= min_total_cost_usd)
        if max_total_cost_usd is not None:
            filters['max_total_cost_usd'] = max_total_cost_usd
            query = query.where(TokenConsumptionStats.total_cost_usd <= max_total_cost_usd)
        if chat_count is not None:
            filters['chat_count'] = chat_count
            query = query.where(TokenConsumptionStats.chat_count == chat_count)
        if min_chat_count is not None:
            filters['min_chat_count'] = min_chat_count
            query = query.where(TokenConsumptionStats.chat_count >= min_chat_count)
        if max_chat_count is not None:
            filters['max_chat_count'] = max_chat_count
            query = query.where(TokenConsumptionStats.chat_count <= max_chat_count)
        if most_used_model is not None:
            filters['most_used_model'] = most_used_model
            if isinstance(most_used_model, str) and '%' in most_used_model:
                query = query.where(TokenConsumptionStats.most_used_model.ilike(most_used_model))
            else:
                query = query.where(TokenConsumptionStats.most_used_model == most_used_model)
        if most_used_provider is not None:
            filters['most_used_provider'] = most_used_provider
            if isinstance(most_used_provider, str) and '%' in most_used_provider:
                query = query.where(TokenConsumptionStats.most_used_provider.ilike(most_used_provider))
            else:
                query = query.where(TokenConsumptionStats.most_used_provider == most_used_provider)
        
        # Log de parámetros aplicados
        if filters:
            logger.info(f"[chatbot]     filters={filters}")
        
        # Aplicar opciones de carga optimizada
        if includes:
            loading_options = get_loading_options(TokenConsumptionStats, includes)
            if loading_options:
                query = query.options(*loading_options)

        # Aplicar ordenamiento
        if order_by:
            for column_name in order_by:
                if hasattr(TokenConsumptionStats, column_name):
                    column = getattr(TokenConsumptionStats, column_name)
                    if order.upper() == "DESC":
                        query = query.order_by(column.desc())
                    elif order.upper() == "ASC":
                        query = query.order_by(column.asc())
                else:
                    logger.warning(f"[chatbot] ⚠️ Columna '{column_name}' no existe en modelo TokenConsumptionStats, ignorando en order_by")
        
        # Aplicar límite (solo valores positivos)
        if limit is not None and limit > 0:
            query = query.limit(limit)

        # Aplicar paginación
        if offset is not None:
            query = query.offset(offset)

        # Ejecutar query
        async def execute_query(session: AsyncSession) -> List[TokenConsumptionStatsRead]:
            results = await session.execute(query)
            instances = results.scalars().all()
            
            logger.info(f"[chatbot] ✅ Encontrados {len(instances)} registros TokenConsumptionStats")
            
            return [
                TokenConsumptionStatsRead.from_instance(
                    instance, 
                    includes=includes, 
                    max_depth=5
                ) 
                for instance in instances
            ]
        
        if session is not None:
            return await execute_query(session)
        else:
            async with self.session_manager.get_session() as session:
                return await execute_query(session)
    

class ChatActivityAsyncDAO:
    """
    Clase DAO asíncrona para el modelo ChatActivity.
    
    Proporciona operaciones completas de Create, Read, Update y Delete
    para el modelo ChatActivity con soporte para gestión automática
    y manual de sesiones SQLAlchemy.
    
    Características principales:
    - Soporte dual: sesiones automáticas o compartidas
    - Type hints completos para mejor experiencia de desarrollo
    - Manejo robusto de errores con rollback automático
    - Operaciones optimizadas con flush para obtener IDs
    - Filtros flexibles en todas las operaciones de búsqueda
    
    Métodos de lectura:
        find(**filters, session=None): Busca un único registro
        find_many(limit, offset, order_by, order, **filters, session=None): Busca múltiples registros
        count(**filters, session=None): Cuenta registros

    Parámetros de sesión:
        Todos los métodos aceptan un parámetro opcional 'session':
        - Si session=None: Se crea una sesión automática con commit
        - Si session=AsyncSession: Se usa la sesión proporcionada (para transacciones)
    
    Ejemplos de uso:
        ```python
        # Operaciones simples (sesión automática)
        crud = ChatActivityDAO(session_manager)
        record = await crud.create(chat_id="valor")
        found = await crud.find_by_id(1)
        
        # Operaciones transaccionales (sesión compartida)
        async with session_manager.transaction() as session:
            record1 = await crud.create(data="valor1", session=session)
            record2 = await crud.create(data="valor2", session=session)
            # Ambos se crean en la misma transacción
        ```
    """
    
    def __init__(self, session_manager: AsyncSessionManager):
        """
        Inicializa el AsyncDAO con un gestor de sesiones.
        
        Args:
            session_manager: Gestor de sesiones asíncronas
        """
        self.session_manager = session_manager
    

    @error_handler
    async def find_many(
        self,
        limit: Optional[int] = None, 
        offset: Optional[int] = None,
        order_by: Optional[List[str]] = None,
        order: Literal["ASC", "DESC"] = "ASC",
        chat_id: Optional[str] = None,
        chat_title: Optional[str] = None,
        username: Optional[str] = None,
        message_count: Optional[int] = None,
        min_message_count: Optional[int] = None,
        max_message_count: Optional[int] = None,
        min_last_message_timestamp: Optional[datetime] = None,
        max_last_message_timestamp: Optional[datetime] = None,
        total_tokens_consumed: Optional[int] = None,
        min_total_tokens_consumed: Optional[int] = None,
        max_total_tokens_consumed: Optional[int] = None,
        is_active: Optional[bool] = None,
        includes: Optional[List[str]] = None,
        session: Optional[AsyncSession] = None
    ) -> List[ChatActivityRead]:
        """
        Busca múltiples registros con carga optimizada de relaciones.
        
        Args:
            - limit: Límite de registros a retornar
            - offset: Número de registros a saltar
            - order_by: Lista de nombres de columnas para ordenar los resultados
            - order: ASC/DESC (por defecto ASC). Solo se aplica si se especifica order_by.
            - chat_id: Filtrar por chat_id
            - chat_title: Filtrar por chat_title
            - username: Filtrar por username
            - message_count: Filtrar por message_count
            - min_message_count: Filtrar por fecha mínima (incluída)
            - max_message_count: Filtrar por fecha máxima (incluída)
            - min_last_message_timestamp: Filtrar por valor mínimo de last_message_timestamp (incluído)
            - max_last_message_timestamp: Filtrar por valor máximo de last_message_timestamp (incluído)
            - total_tokens_consumed: Filtrar por total_tokens_consumed
            - min_total_tokens_consumed: Filtrar por fecha mínima (incluída)
            - max_total_tokens_consumed: Filtrar por fecha máxima (incluída)
            - is_active: Filtrar por is_active
            - includes: Lista de relaciones a incluir (formato: 'relation' o 'relation.nested')
            - session: Sesión existente (opcional)
            
        Returns:
            Lista de instancias del modelo
            
        Examples:
            Búsqueda simple con relaciones

            await dao.find_many(limit=10, includes=['author'])
            
            Relaciones anidadas

            await dao.find_many(
                ..., 
                includes=['author', 'author.profile', 'comments']
            )
            
            Ordenamiento ascendente por columnas

            await dao.find_many(order_by=['created_at', 'name'], order='ASC')
            
            Ordenamiento descendente por columnas

            await dao.find_many(order_by=['created_at', 'name'], order='DESC')
            
            Paginación

            # Obtener los primeros 10 registros
            await dao.find_many(limit=10)
            
            # Obtener los últimos 5 registros ordenados por fecha
            await dao.find_many(limit=5, order_by=['created_at'], order='DESC')
            
            # Paginación con offset
            await dao.find_many(limit=10, offset=20)
            
        """
        logger.info(f"[chatbot] 🔍 Buscando múltiples ChatActivity:")
        logger.info(f"[chatbot]     limit={limit}")
        logger.info(f"[chatbot]     offset={offset}")
        logger.info(f"[chatbot]     order_by={order_by}")
        logger.info(f"[chatbot]     order={order}")
        logger.info(f"[chatbot]     includes={includes}")
        
        # Construir query base
        query = select(ChatActivity)

        # Filters
        filters = {}
        
        # Aplicar filtros de búsqueda
        if chat_id is not None:
            filters['chat_id'] = chat_id
            if isinstance(chat_id, str) and '%' in chat_id:
                query = query.where(ChatActivity.chat_id.ilike(chat_id))
            else:
                query = query.where(ChatActivity.chat_id == chat_id)
        if chat_title is not None:
            filters['chat_title'] = chat_title
            if isinstance(chat_title, str) and '%' in chat_title:
                query = query.where(ChatActivity.chat_title.ilike(chat_title))
            else:
                query = query.where(ChatActivity.chat_title == chat_title)
        if username is not None:
            filters['username'] = username
            if isinstance(username, str) and '%' in username:
                query = query.where(ChatActivity.username.ilike(username))
            else:
                query = query.where(ChatActivity.username == username)
        if message_count is not None:
            filters['message_count'] = message_count
            query = query.where(ChatActivity.message_count == message_count)
        if min_message_count is not None:
            filters['min_message_count'] = min_message_count
            query = query.where(ChatActivity.message_count >= min_message_count)
        if max_message_count is not None:
            filters['max_message_count'] = max_message_count
            query = query.where(ChatActivity.message_count <= max_message_count)
        if min_last_message_timestamp is not None:
            filters['min_last_message_timestamp'] = min_last_message_timestamp
            query = query.where(ChatActivity.last_message_timestamp >= min_last_message_timestamp)
        if max_last_message_timestamp is not None:
            filters['max_last_message_timestamp'] = max_last_message_timestamp
            query = query.where(ChatActivity.last_message_timestamp <= max_last_message_timestamp)
        if total_tokens_consumed is not None:
            filters['total_tokens_consumed'] = total_tokens_consumed
            query = query.where(ChatActivity.total_tokens_consumed == total_tokens_consumed)
        if min_total_tokens_consumed is not None:
            filters['min_total_tokens_consumed'] = min_total_tokens_consumed
            query = query.where(ChatActivity.total_tokens_consumed >= min_total_tokens_consumed)
        if max_total_tokens_consumed is not None:
            filters['max_total_tokens_consumed'] = max_total_tokens_consumed
            query = query.where(ChatActivity.total_tokens_consumed <= max_total_tokens_consumed)
        if is_active is not None:
            filters['is_active'] = is_active
            query = query.where(ChatActivity.is_active == is_active)
        
        # Log de parámetros aplicados
        if filters:
            logger.info(f"[chatbot]     filters={filters}")
        
        # Aplicar opciones de carga optimizada
        if includes:
            loading_options = get_loading_options(ChatActivity, includes)
            if loading_options:
                query = query.options(*loading_options)

        # Aplicar ordenamiento
        if order_by:
            for column_name in order_by:
                if hasattr(ChatActivity, column_name):
                    column = getattr(ChatActivity, column_name)
                    if order.upper() == "DESC":
                        query = query.order_by(column.desc())
                    elif order.upper() == "ASC":
                        query = query.order_by(column.asc())
                else:
                    logger.warning(f"[chatbot] ⚠️ Columna '{column_name}' no existe en modelo ChatActivity, ignorando en order_by")
        
        # Aplicar límite (solo valores positivos)
        if limit is not None and limit > 0:
            query = query.limit(limit)

        # Aplicar paginación
        if offset is not None:
            query = query.offset(offset)

        # Ejecutar query
        async def execute_query(session: AsyncSession) -> List[ChatActivityRead]:
            results = await session.execute(query)
            instances = results.scalars().all()
            
            logger.info(f"[chatbot] ✅ Encontrados {len(instances)} registros ChatActivity")
            
            return [
                ChatActivityRead.from_instance(
                    instance, 
                    includes=includes, 
                    max_depth=5
                ) 
                for instance in instances
            ]
        
        if session is not None:
            return await execute_query(session)
        else:
            async with self.session_manager.get_session() as session:
                return await execute_query(session)
    

