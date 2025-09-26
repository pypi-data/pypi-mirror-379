"""
JetTask API 应用初始化
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    """创建并配置 FastAPI 应用"""
    
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        """应用生命周期管理"""
        # 启动时初始化
        try:
            import os
            # 检查是否使用Nacos配置
            use_nacos = os.getenv('USE_NACOS', 'false').lower() == 'true'
            
            # 初始化数据库管理器
            from jettask.core.db_manager import init_db_manager
            await init_db_manager(use_nacos=use_nacos)
            
            # 延迟导入，避免循环依赖
            from jettask.backend.data_access import JetTaskDataAccess
            from jettask.backend.namespace_data_access import get_namespace_data_access
            from jettask.backend.config import task_center_config
            
            # 创建数据访问实例
            data_access = JetTaskDataAccess()
            namespace_data_access = get_namespace_data_access()
            
            # 存储在app.state中供路由使用
            app.state.data_access = data_access
            app.state.namespace_data_access = namespace_data_access
            
            # 初始化JetTask数据访问
            await data_access.initialize()
            
            # 记录任务中心配置
            logger.info("=" * 60)
            logger.info("任务中心配置:")
            logger.info(f"  配置模式: {'Nacos' if use_nacos else '环境变量'}")
            logger.info(f"  元数据库: {task_center_config.meta_db_host}:{task_center_config.meta_db_port}/{task_center_config.meta_db_name}")
            logger.info(f"  API服务: {task_center_config.api_host}:{task_center_config.api_port}")
            logger.info(f"  基础URL: {task_center_config.base_url}")
            logger.info("=" * 60)
            
            logger.info("JetTask Monitor API 启动成功")
        except Exception as e:
            logger.error(f"启动失败: {e}")
            import traceback
            traceback.print_exc()
            raise
        
        yield
        
        # 关闭时清理资源
        try:
            await app.state.data_access.close()
            
            # 关闭数据库管理器
            from jettask.core.db_manager import close_db_manager
            await close_db_manager()
            
            logger.info("JetTask Monitor API 关闭完成")
        except Exception as e:
            logger.error(f"关闭时出错: {e}")
            import traceback
            traceback.print_exc()
    
    # 创建 FastAPI 应用
    app = FastAPI(
        title="JetTask Monitor API", 
        version="1.0.0",
        lifespan=lifespan
    )
    
    # 配置CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # 生产环境应该配置具体的前端地址
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # 注册路由
    from jettask.api.v1 import api_router
    
    app.include_router(api_router)
    
    return app


# 创建默认应用实例
app = create_app()