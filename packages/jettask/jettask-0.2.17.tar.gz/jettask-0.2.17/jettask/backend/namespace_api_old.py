"""
命名空间管理API - 重构版本
使用数据库持久化命名空间数据
"""
from fastapi import APIRouter, HTTPException, Query
from typing import Dict, Any, Optional, List
from datetime import datetime
import json
from sqlalchemy import text
import logging
from jettask.schemas import NamespaceCreate, NamespaceUpdate, NamespaceResponse

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/namespaces", tags=["namespaces"])

# 使用任务中心专用的元数据库连接
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from jettask.backend.config import task_center_config

# 创建异步引擎 - 连接到任务中心元数据库
# 注意：这是任务中心自己的数据库，不是JetTask应用的数据库
engine = create_async_engine(task_center_config.meta_database_url, echo=False)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


# 模型已从 schemas 模块导入


@router.get("", response_model=List[NamespaceResponse])
async def list_namespaces(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    is_active: Optional[bool] = None
):
    """列出所有命名空间"""
    try:
        async with AsyncSessionLocal() as session:
            query = """
                SELECT id, name, description, redis_config, pg_config, 
                       is_active, version, created_at, updated_at
                FROM namespaces
            """
            params = {}
            
            if is_active is not None:
                query += " WHERE is_active = :is_active"
                params['is_active'] = is_active
            
            query += " ORDER BY created_at DESC"
            query += " LIMIT :limit OFFSET :offset"
            params['limit'] = page_size
            params['offset'] = (page - 1) * page_size
            
            result = await session.execute(text(query), params)
            rows = result.fetchall()
            
            namespaces = []
            for row in rows:
                namespaces.append(NamespaceResponse(
                    id=row.id,
                    name=row.name,
                    description=row.description,
                    redis_config=row.redis_config,
                    pg_config=row.pg_config,
                    is_active=row.is_active,
                    version=row.version,
                    created_at=row.created_at,
                    updated_at=row.updated_at,
                    connection_url=f"/api/namespaces/{row.name}"  # 使用名称
                ))
            
            return namespaces
    except Exception as e:
        logger.error(f"Failed to list namespaces: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("", response_model=NamespaceResponse, status_code=201)
async def create_namespace(namespace: NamespaceCreate):
    """创建新的命名空间"""
    try:
        async with AsyncSessionLocal() as session:
            # 检查名称是否已存在
            check_query = text("SELECT COUNT(*) FROM namespaces WHERE name = :name")
            result = await session.execute(check_query, {'name': namespace.name})
            if result.scalar() > 0:
                raise HTTPException(status_code=400, detail=f"命名空间 '{namespace.name}' 已存在")
            
            # 创建命名空间（使用自增ID）
            insert_query = text("""
                INSERT INTO namespaces (name, description, redis_config, pg_config, version)
                VALUES (:name, :description, :redis_config, :pg_config, 1)
                RETURNING id, name, description, redis_config, pg_config, 
                          is_active, version, created_at, updated_at
            """)
            
            result = await session.execute(insert_query, {
                'name': namespace.name,
                'description': namespace.description,
                'redis_config': json.dumps(namespace.redis_config),
                'pg_config': json.dumps(namespace.pg_config)
            })
            
            row = result.fetchone()
            await session.commit()
            
            return NamespaceResponse(
                id=str(row.id),
                name=row.name,
                description=row.description,
                redis_config=row.redis_config,
                pg_config=row.pg_config,
                is_active=row.is_active,
                version=row.version,
                created_at=row.created_at,
                updated_at=row.updated_at,
                connection_url=f"/api/namespaces/{str(row.id)}"
            )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to create namespace: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{namespace_id}", response_model=NamespaceResponse)
async def get_namespace(namespace_id: str):
    """获取指定命名空间的详细信息"""
    try:
        async with AsyncSessionLocal() as session:
            query = text("""
                SELECT id, name, description, redis_config, pg_config, 
                       is_active, version, created_at, updated_at
                FROM namespaces
                WHERE id = :id
            """)
            
            result = await session.execute(query, {'id': namespace_id})
            row = result.fetchone()
            
            if not row:
                raise HTTPException(status_code=404, detail="命名空间不存在")
            
            return NamespaceResponse(
                id=str(row.id),
                name=row.name,
                description=row.description,
                redis_config=row.redis_config,
                pg_config=row.pg_config,
                is_active=row.is_active,
                version=row.version,
                created_at=row.created_at,
                updated_at=row.updated_at,
                connection_url=f"/api/namespaces/{str(row.id)}"
            )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to get namespace: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{namespace_id}", response_model=NamespaceResponse)
async def update_namespace(namespace_id: str, namespace: NamespaceUpdate):
    """更新命名空间"""
    try:
        async with AsyncSessionLocal() as session:
            # 检查是否存在并获取名称
            check_query = text("SELECT name FROM namespaces WHERE id = :id")
            result = await session.execute(check_query, {'id': namespace_id})
            row = result.fetchone()
            
            if not row:
                raise HTTPException(status_code=404, detail="命名空间不存在")
            
            # 检查是否是默认命名空间
            if row.name == 'default':
                raise HTTPException(status_code=400, detail="默认命名空间不能编辑")
            
            # 构建更新语句
            updates = []
            params = {'id': namespace_id}
            
            if namespace.description is not None:
                updates.append("description = :description")
                params['description'] = namespace.description
            
            if namespace.redis_config is not None:
                updates.append("redis_config = :redis_config")
                params['redis_config'] = json.dumps(namespace.redis_config)
            
            if namespace.pg_config is not None:
                updates.append("pg_config = :pg_config")
                params['pg_config'] = json.dumps(namespace.pg_config)
            
            if namespace.is_active is not None:
                updates.append("is_active = :is_active")
                params['is_active'] = namespace.is_active
            
            if not updates:
                raise HTTPException(status_code=400, detail="没有要更新的字段")
            
            # 如果更新了redis_config或pg_config，递增版本号
            if 'redis_config' in params or 'pg_config' in params:
                updates.append("version = version + 1")
            
            update_query = text(f"""
                UPDATE namespaces
                SET {', '.join(updates)}
                WHERE id = :id
                RETURNING id, name, description, redis_config, pg_config, 
                          is_active, version, created_at, updated_at
            """)
            
            result = await session.execute(update_query, params)
            row = result.fetchone()
            await session.commit()
            
            return NamespaceResponse(
                id=str(row.id),
                name=row.name,
                description=row.description,
                redis_config=row.redis_config,
                pg_config=row.pg_config,
                is_active=row.is_active,
                version=row.version,
                created_at=row.created_at,
                updated_at=row.updated_at,
                connection_url=f"/api/namespaces/{str(row.id)}"
            )
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to update namespace: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/{namespace_id}")
async def delete_namespace(namespace_id: str):
    """删除命名空间"""
    try:
        async with AsyncSessionLocal() as session:
            # 检查是否为默认命名空间
            check_query = text("SELECT name FROM namespaces WHERE id = :id")
            result = await session.execute(check_query, {'id': namespace_id})
            row = result.fetchone()
            
            if not row:
                raise HTTPException(status_code=404, detail="命名空间不存在")
            
            if row.name == 'default':
                raise HTTPException(status_code=400, detail="不能删除默认命名空间")
            
            # 删除命名空间
            delete_query = text("DELETE FROM namespaces WHERE id = :id")
            await session.execute(delete_query, {'id': namespace_id})
            await session.commit()
            
            return {"message": "命名空间已删除"}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to delete namespace: {e}")
        raise HTTPException(status_code=500, detail=str(e))

