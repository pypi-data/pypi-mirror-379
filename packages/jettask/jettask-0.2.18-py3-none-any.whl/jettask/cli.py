#!/usr/bin/env python
"""
JetTask CLI - 命令行接口
"""
import click
import sys
import os
import importlib
import importlib.util
import json
from pathlib import Path
from dotenv import load_dotenv

# 处理直接运行时的路径问题
if __name__ == '__main__':
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)

from jettask.config.nacos_config import config
from jettask.core.app_importer import import_app, AppImporter


@click.group()
@click.version_option(version='0.1.0', prog_name='JetTask')
def cli():
    """JetTask - 高性能分布式任务队列系统"""
    pass

@cli.command()
@click.option('--host', default='0.0.0.0', help='服务器监听地址')
@click.option('--port', default=8001, type=int, help='服务器监听端口')
@click.option('--jettask-pg-url', envvar='JETTASK_PG_URL', 
              help='PostgreSQL连接URL')
@click.option('--use-nacos', is_flag=True, default=False, 
              help='从Nacos配置中心读取配置')
@click.option('--nacos-server', envvar='NACOS_SERVER', 
              help='Nacos服务器地址')
@click.option('--nacos-namespace', envvar='NACOS_NAMESPACE',
              help='Nacos命名空间')
@click.option('--nacos-username', envvar='NACOS_USERNAME',
              help='Nacos用户名')
@click.option('--nacos-password', envvar='NACOS_PASSWORD',
              help='Nacos密码')
@click.option('--nacos-group', envvar='NACOS_GROUP',
              help='Nacos配置组')
@click.option('--nacos-data-id', envvar='NACOS_DATA_ID',
              help='Nacos配置ID')
@click.option('--reload', is_flag=True, default=False, help='启用自动重载')
@click.option('--log-level', default='info', 
              type=click.Choice(['debug', 'info', 'warning', 'error']),
              help='日志级别')
def api(host, port, jettask_pg_url, use_nacos, nacos_server, nacos_namespace, 
        nacos_username, nacos_password, nacos_group, nacos_data_id, 
        reload, log_level):
    """启动 API 服务和监控界面
    
    示例:
    \b
      # 使用默认配置启动
      jettask api
      
      # 指定端口和数据库
      jettask api --host 0.0.0.0 --port 8080 --jettask-pg-url postgresql://user:pass@host/db
      
      # 使用Nacos配置中心
      jettask api --use-nacos --nacos-server 127.0.0.1:8848
      
      # 通过环境变量配置Nacos
      export NACOS_SERVER=127.0.0.1:8848
      export NACOS_NAMESPACE=tamar_console_dev
      jettask api --use-nacos
      
      # 通过环境变量配置数据库
      export JETTASK_PG_URL=postgresql://jettask:123456@localhost:5432/jettask
      jettask api
      
      # 启用开发模式（自动重载）
      jettask api --reload --log-level debug
    """
    import os
    import uvicorn
    
    print(f'{use_nacos=} {jettask_pg_url=}')
    if not use_nacos and not jettask_pg_url:
        raise ValueError("必须提供 --jettask-pg-url 或启用 --use-nacos")
    # 如果使用Nacos，从Nacos获取配置
    if use_nacos:
        click.echo("正在从Nacos加载配置...")
        load_dotenv()
        # 设置Nacos环境变量
        if nacos_server:
            os.environ['NACOS_SERVER'] = nacos_server
        if nacos_namespace:
            os.environ['NACOS_NAMESPACE'] = nacos_namespace
        if nacos_username:
            os.environ['NACOS_USERNAME'] = nacos_username
        if nacos_password:
            os.environ['NACOS_PASSWORD'] = nacos_password
        if nacos_group:
            os.environ['NACOS_GROUP'] = nacos_group
        if nacos_data_id:
            os.environ['NACOS_DATA_ID'] = nacos_data_id
        
        nacos_server = os.environ['NACOS_SERVER']
        nacos_namespace = os.environ['NACOS_NAMESPACE']
        nacos_username = os.environ['NACOS_USERNAME']
        nacos_password = os.environ['NACOS_PASSWORD']
        nacos_group = os.environ['NACOS_GROUP']
        nacos_data_id = os.environ['NACOS_DATA_ID']
        # 尝试从配置中获取JETTASK_PG_URL
        nacos_pg_url = config.config.get('JETTASK_PG_URL')
        print(f'{nacos_pg_url=}')
        if not nacos_pg_url:
            # 如果没有直接的URL，尝试从独立的配置项构建
            pg_host = config.config.get('PG_DB_HOST', 'localhost')
            pg_port = config.config.get('PG_DB_PORT', 5432)
            pg_user = config.config.get('PG_DB_USERNAME', 'jettask')
            pg_password = config.config.get('PG_DB_PASSWORD', '123456')
            pg_database = config.config.get('PG_DB_DATABASE', 'jettask')
            nacos_pg_url = f'postgresql://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_database}'
        
        jettask_pg_url = nacos_pg_url
        click.echo(f"✓ 从Nacos加载配置成功")
        click.echo(f"  配置源: {nacos_server}/{nacos_namespace}/{nacos_group}/{nacos_data_id}")
        
        # 将其他Nacos配置也设置到环境变量中
        for key, value in config.config.items():
            if isinstance(value, (str, int, float, bool)):
                os.environ[key] = str(value)

    
    # 设置环境变量（供应用内部使用）
    os.environ['JETTASK_PG_URL'] = jettask_pg_url
    
    # 设置是否使用Nacos的标志
    os.environ['USE_NACOS'] = 'true' if use_nacos else 'false'
    
    # 使用标准应用模块
    app_module = "jettask.api:app"
    click.echo(f"Starting JetTask API Server on {host}:{port}")
    
    # 显示配置信息
    click.echo("=" * 60)
    click.echo("API Server Configuration")
    click.echo("=" * 60)
    click.echo(f"Host:        {host}")
    click.echo(f"Port:        {port}")
    click.echo(f"Auto-reload: {reload}")
    click.echo(f"Log level:   {log_level}")
    click.echo(f"Nacos:       {'Enabled' if use_nacos else 'Disabled'}")
    if use_nacos:
        click.echo(f"  Server:    {nacos_server}")
        click.echo(f"  Namespace: {nacos_namespace}")
        click.echo(f"  Data ID:   {nacos_data_id}")
    click.echo(f"Database:    {jettask_pg_url}")
    click.echo("=" * 60)
    click.echo(f"API Endpoint: http://{host}:{port}/api")
    click.echo(f"WebUI:        http://{host}:{port}/")
    click.echo("=" * 60)
    
    # 启动服务器
    try:
        uvicorn.run(
            app_module,
            host=host,
            port=port,
            log_level=log_level,
            reload=reload
        )
    except KeyboardInterrupt:
        click.echo("\nShutting down API Server...")
    except Exception as e:
        click.echo(f"Error starting API Server: {e}", err=True)
        sys.exit(1)


def load_module_from_path(module_path: str):
    """从文件路径加载 Python 模块"""
    path = Path(module_path).resolve()
    
    if not path.exists():
        raise FileNotFoundError(f"Module file not found: {module_path}")
    
    # 获取模块名
    module_name = path.stem
    
    # 加载模块
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None:
        raise ImportError(f"Cannot load module from {module_path}")
    
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    
    return module

def find_jettask_app(module):
    """在模块中查找 Jettask 实例"""
    from jettask import Jettask
    
    # 查找模块中的 Jettask 实例
    for name in dir(module):
        obj = getattr(module, name)
        if isinstance(obj, Jettask):
            return obj
    
    # 如果没有找到，尝试查找名为 'app' 的变量
    if hasattr(module, 'app'):
        obj = getattr(module, 'app')
        if isinstance(obj, Jettask):
            return obj
    
    return None

@cli.command()
@click.argument('app_str', required=False, default=None)
@click.option('--queues', '-q', help='队列名称（逗号分隔，如: queue1,queue2）')
@click.option('--executor', '-e', 
              type=click.Choice(['asyncio', 'multi_asyncio']),
              default='asyncio',
              help='执行器类型')
@click.option('--concurrency', '-c', type=int, default=4, help='并发数')
@click.option('--prefetch', '-p', type=int, default=100, help='预取倍数')
@click.option('--reload', '-r', is_flag=True, help='自动重载')
@click.option('--config', help='配置文件 (JSON格式)')
def worker(app_str, queues, executor, concurrency, prefetch, reload, config):
    """启动任务处理 Worker
    
    示例:
    \b
      # 显式指定 app
      jettask worker main:app --queues async_queue
      jettask worker tasks.py:app --queues queue1,queue2
      jettask worker myapp.tasks --queues high,normal,low
      
      # 自动发现 app（从当前目录的 app.py 或 main.py）
      jettask worker --queues async_queue
      
      # 使用环境变量
      export JETTASK_APP=myapp:app
      jettask worker --queues async_queue
    """
    
    # 如果提供了配置文件，从中加载配置
    if config:
        click.echo(f"Loading configuration from {config}")
        with open(config, 'r') as f:
            config_data = json.load(f)
        
        # 从配置文件读取参数（命令行参数优先）
        queues = queues or ','.join(config_data.get('queues', [])) if config_data.get('queues') else None
        executor = executor or config_data.get('executor', 'asyncio')
        concurrency = concurrency if concurrency != 4 else config_data.get('concurrency', 4)
        prefetch = prefetch if prefetch != 100 else config_data.get('prefetch', 100)
        reload = reload or config_data.get('reload', False)
    
    # 加载应用
    try:
        if app_str:
            click.echo(f"Loading app from: {app_str}")
            app = import_app(app_str)
        else:
            click.echo("Auto-discovering Jettask app...")
            click.echo("Searching in: app.py, main.py, server.py, worker.py")
            app = import_app()  # 自动发现
        
        # 显示应用信息
        app_info = AppImporter.get_app_info(app)
        click.echo(f"\nFound Jettask app:")
        click.echo(f"  Tasks: {app_info['tasks']} registered")
        if app_info.get('task_names') and app_info['tasks'] > 0:
            task_preview = app_info['task_names'][:3]
            click.echo(f"  Names: {', '.join(task_preview)}" + 
                      (f" (+{app_info['tasks'] - 3} more)" if app_info['tasks'] > 3 else ""))
    except ImportError as e:
        import traceback
        click.echo(f"Error: Failed to import app: {e}", err=True)
        
        # 始终显示完整的堆栈跟踪，帮助用户定位问题
        click.echo("\n" + "=" * 60, err=True)
        click.echo("Full traceback:", err=True)
        click.echo("=" * 60, err=True)
        traceback.print_exc()
        click.echo("=" * 60, err=True)
        
        click.echo("\nTips:", err=True)
        click.echo("  - Check if there are syntax errors in your code", err=True)
        click.echo("  - Verify all imports in your module are available", err=True)
        click.echo("  - Specify app location: jettask worker myapp:app", err=True)
        click.echo("  - Or set environment variable: export JETTASK_APP=myapp:app", err=True)
        click.echo("  - Or ensure app.py or main.py exists in current directory", err=True)
        sys.exit(1)
    except Exception as e:
        import traceback
        click.echo(f"Error loading app: {e}", err=True)
        
        # 对于所有异常都显示堆栈信息
        click.echo("\n" + "=" * 60, err=True)
        click.echo("Full traceback:", err=True)
        click.echo("=" * 60, err=True)
        traceback.print_exc()
        click.echo("=" * 60, err=True)
        
        click.echo("\nThis might be a bug in JetTask or your application.", err=True)
        click.echo("Please check the traceback above for details.", err=True)
        sys.exit(1)
    
    # 处理队列参数
    if queues:
        # 解析队列列表（支持逗号分隔）
        queue_list = [q.strip() for q in queues.split(',') if q.strip()]
    else:
        # 如果没有指定队列，尝试从 app 获取
        if hasattr(app, 'ep') and hasattr(app.ep, 'queues'):
            queue_list = list(app.ep.queues)
            if queue_list:
                click.echo(f"Using queues from app: {', '.join(queue_list)}")
        else:
            queue_list = []
    
    if not queue_list:
        click.echo("Error: No queues specified", err=True)
        click.echo("  Use --queues to specify queues, e.g.: --queues queue1,queue2", err=True)
        click.echo("  Or define queues in your app configuration", err=True)
        sys.exit(1)
    
    # 从 app 实例中获取实际配置
    redis_url = app.redis_url if hasattr(app, 'redis_url') else 'Not configured'
    redis_prefix = app.redis_prefix if hasattr(app, 'redis_prefix') else 'jettask'
    consumer_strategy = app.consumer_strategy if hasattr(app, 'consumer_strategy') else 'heartbeat'
    
    # 显示配置信息
    click.echo("=" * 60)
    click.echo("JetTask Worker Configuration")
    click.echo("=" * 60)
    click.echo(f"App:          {app_str}")
    click.echo(f"Redis URL:    {redis_url}")
    click.echo(f"Redis Prefix: {redis_prefix}")
    click.echo(f"Strategy:     {consumer_strategy}")
    click.echo(f"Queues:       {', '.join(queue_list)}")
    click.echo(f"Executor:     {executor}")
    click.echo(f"Concurrency:  {concurrency}")
    click.echo(f"Prefetch:     {prefetch}")
    click.echo(f"Auto-reload:  {reload}")
    click.echo("=" * 60)
    
    # 启动 Worker
    try:
        click.echo(f"Starting {executor} worker...")
        app.start(
            execute_type=executor,
            queues=queue_list,
            concurrency=concurrency,
            prefetch_multiplier=prefetch,
            reload=reload
        )
    except KeyboardInterrupt:
        click.echo("\nShutting down worker...")
    except Exception as e:
        click.echo(f"Error starting worker: {e}", err=True)
        sys.exit(1)

@cli.command('webui-consumer')
@click.option('--task-center', '-tc', envvar='JETTASK_CENTER_URL', required=True,
              help='任务中心URL，如: http://localhost:8001 或 http://localhost:8001/api/v1/namespaces/default')
@click.option('--check-interval', type=int, default=30,
              help='命名空间检测间隔（秒），默认30秒')
@click.option('--debug', is_flag=True, help='启用调试模式')
def webui_consumer(task_center, check_interval, debug):
    """启动数据消费者（自动识别单/多命名空间）
    
    根据URL格式自动判断运行模式:
    - 单命名空间: http://localhost:8001/api/v1/namespaces/{name}
    - 多命名空间: http://localhost:8001 或 http://localhost:8001/api
    
    示例:
    \b
      # 为所有命名空间启动消费者（自动检测）
      jettask webui-consumer --task-center http://localhost:8001
      jettask webui-consumer --task-center http://localhost:8001/api
      
      # 为单个命名空间启动消费者
      jettask webui-consumer --task-center http://localhost:8001/api/v1/namespaces/default
      
      # 自定义检测间隔
      jettask webui-consumer --task-center http://localhost:8001 --check-interval 60
      
      # 使用环境变量
      export JETTASK_CENTER_URL=http://localhost:8001
      jettask webui-consumer
    """
    import asyncio
    from jettask.unified_consumer_manager import UnifiedConsumerManager
    
    # 运行消费者管理器
    async def run_manager():
        """运行统一的消费者管理器"""
        manager = UnifiedConsumerManager(
            task_center_url=task_center,
            check_interval=check_interval,
            debug=debug
        )
        await manager.run()
    
    try:
        asyncio.run(run_manager())
    except KeyboardInterrupt:
        click.echo("\nShutdown complete")

@cli.command()
def monitor():
    """启动系统监控器"""
    click.echo("Starting JetTask Monitor")
    from jettask.run_monitor import main as monitor_main
    monitor_main()

@cli.command()
@click.option('--task-center', '-tc', envvar='JETTASK_CENTER_URL',
              help='任务中心URL，如: http://localhost:8001/api/v1/namespaces/default')
def init(task_center):
    """初始化数据库和配置
    
    示例:
    \b
      # 使用任务中心初始化
      jettask init --task-center http://localhost:8001/api/v1/namespaces/default
      jettask init -tc http://localhost:8001/api/v1/namespaces/production
      
      # 使用环境变量
      export JETTASK_CENTER_URL=http://localhost:8001/api/v1/namespaces/default
      jettask init
      
      # 不使用任务中心（仅使用本地环境变量）
      jettask init
    """
    click.echo("Initializing JetTask...")
    
    import os
    
    # 如果提供了任务中心URL，尝试从任务中心获取配置
    if task_center:
        os.environ['JETTASK_CENTER_URL'] = task_center
        click.echo(f"Using Task Center: {task_center}")
        
        # 尝试从任务中心获取数据库配置
        try:
            from jettask.task_center import TaskCenter
            tc = TaskCenter(task_center)
            if tc._connect_sync():
                p_config = tc.pg_config
                # 从任务中心获取的配置中提取数据库连接参数
                os.environ['JETTASK_PG_HOST'] = p_config['host']
                os.environ['JETTASK_PG_PORT'] = str(p_config['port'])
                os.environ['JETTASK_PG_DATABASE'] = p_config['database']
                os.environ['JETTASK_PG_USER'] = p_config['user']
                os.environ['JETTASK_PG_PASSWORD'] = p_config['password']
            else:
                click.echo("⚠ Failed to connect to Task Center, using local configuration", err=True)
        except Exception as e:
            click.echo(f"⚠ Could not get configuration from Task Center: {e}", err=True)
            click.echo("  Falling back to local environment variables")
    
    # 初始化数据库
    from jettask.db_init import init_database
    click.echo("\nInitializing database...")
    init_database()
    
    click.echo("\n✓ JetTask initialized successfully!")

@cli.command()
def status():
    """显示系统状态"""
    click.echo("JetTask System Status")
    click.echo("=" * 50)
    
    # 检查 Redis 连接
    try:
        import redis
        r = redis.Redis(host='localhost', port=6379, db=0)
        r.ping()
        click.echo("✓ Redis: Connected")
    except:
        click.echo("✗ Redis: Not connected")
    
    # 检查 PostgreSQL 连接
    try:
        import psycopg2
        conn = psycopg2.connect(
            dbname=os.getenv('JETTASK_PG_DB', 'jettask'),
            user=os.getenv('JETTASK_PG_USER', 'jettask'),
            password=os.getenv('JETTASK_PG_PASSWORD', '123456'),
            host=os.getenv('JETTASK_PG_HOST', 'localhost'),
            port=os.getenv('JETTASK_PG_PORT', '5432')
        )
        conn.close()
        click.echo("✓ PostgreSQL: Connected")
    except:
        click.echo("✗ PostgreSQL: Not connected")
    
    click.echo("=" * 50)

@cli.command()
@click.option('--task-center', '-tc', envvar='JETTASK_CENTER_URL', required=True,
              help='任务中心URL，如: http://localhost:8001 或 http://localhost:8001/api/v1/namespaces/default')
@click.option('--interval', '-i', type=float, default=0.1, 
              help='调度器扫描间隔（秒），默认0.1秒')
@click.option('--batch-size', '-b', type=int, default=100,
              help='每批处理的最大任务数，默认100')
@click.option('--check-interval', type=int, default=30,
              help='命名空间检测间隔（秒），仅多命名空间模式使用，默认30秒')
@click.option('--debug', is_flag=True, help='启用调试模式')
def scheduler(task_center, interval, batch_size, check_interval, debug):
    """启动定时任务调度器（自动识别单/多命名空间）
    
    根据URL格式自动判断运行模式:
    - 单命名空间: http://localhost:8001/api/v1/namespaces/{name}
    - 多命名空间: http://localhost:8001 或 http://localhost:8001/api
    
    示例:
    \b
      # 为所有命名空间启动调度器（自动检测）
      jettask scheduler --task-center http://localhost:8001
      jettask scheduler --task-center http://localhost:8001/api
      
      # 为单个命名空间启动调度器
      jettask scheduler --task-center http://localhost:8001/api/v1/namespaces/default
      
      # 自定义配置
      jettask scheduler --task-center http://localhost:8001 --check-interval 60 --interval 0.5
      
      # 使用环境变量
      export JETTASK_CENTER_URL=http://localhost:8001
      jettask scheduler
    """
    import asyncio
    from jettask.scheduler.unified_scheduler_manager import UnifiedSchedulerManager
    
    # 运行调度器管理器
    async def run_manager():
        """运行统一的调度器管理器"""
        manager = UnifiedSchedulerManager(
            task_center_url=task_center,
            scan_interval=interval,
            batch_size=batch_size,
            check_interval=check_interval,
            debug=debug
        )
        await manager.run()
    
    try:
        asyncio.run(run_manager())
    except KeyboardInterrupt:
        click.echo("\nShutdown complete")

@cli.command()
@click.option('--port', default=8080, help='前端服务器端口')
@click.option('--host', default='0.0.0.0', help='前端服务器监听地址')
@click.option('--api-url', default='http://localhost:8001', help='后端 API 服务器地址')
@click.option('--auto-install', is_flag=True, default=True, help='自动安装缺失的依赖')
@click.option('--force-install', is_flag=True, help='强制重新安装依赖')
@click.option('--build-only', is_flag=True, help='仅构建生产版本，不启动服务器')
def frontend(port, host, api_url, auto_install, force_install, build_only):
    """启动 WebUI 前端界面
    
    启动生产版本服务器：
    1. 检查 Node.js 和 npm 是否安装
    2. 在包目录安装依赖并构建
    3. 启动生产版本服务器
    
    示例：
      # 启动生产版本服务器（默认）
      jettask frontend
      
      # 指定端口
      jettask frontend --port 3000
      
      # 指定后端API地址
      jettask frontend --api-url http://192.168.1.100:8001
      
      # 仅构建生产版本
      jettask frontend --build-only
      
      # 强制重新安装依赖
      jettask frontend --force-install
    """
    import subprocess
    import shutil
    from pathlib import Path
    
    # 获取前端目录路径
    frontend_dir = Path(__file__).parent.parent / "webui" / "frontend"
    if not frontend_dir.exists():
        click.echo(f"错误：前端目录不存在: {frontend_dir}", err=True)
        sys.exit(1)
    
    # 检查 Node.js 是否安装
    node_cmd = shutil.which('node')
    if not node_cmd:
        click.echo("错误：未检测到 Node.js 环境", err=True)
        click.echo("\n请先安装 Node.js:")
        click.echo("  - Ubuntu/Debian: sudo apt-get install nodejs npm")
        click.echo("  - macOS: brew install node")
        click.echo("  - Windows: 从 https://nodejs.org 下载安装")
        click.echo("  - 或使用 nvm: curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash")
        sys.exit(1)
    
    # 检查 npm 是否安装
    npm_cmd = shutil.which('npm')
    if not npm_cmd:
        click.echo("错误：未检测到 npm", err=True)
        click.echo("\n请安装 npm:")
        click.echo("  - Ubuntu/Debian: sudo apt-get install npm")
        click.echo("  - 或重新安装 Node.js (包含 npm)")
        sys.exit(1)
    
    # 显示版本信息
    try:
        node_version = subprocess.check_output([node_cmd, '--version'], text=True).strip()
        npm_version = subprocess.check_output([npm_cmd, '--version'], text=True).strip()
        click.echo(f"检测到 Node.js {node_version}, npm {npm_version}")
    except subprocess.CalledProcessError:
        pass
    
    # 切换到前端目录
    os.chdir(frontend_dir)
    click.echo(f"前端目录: {frontend_dir}")
    
    # 检查 package.json 是否存在
    package_json = frontend_dir / "package.json"
    if not package_json.exists():
        click.echo("错误：package.json 文件不存在", err=True)
        sys.exit(1)
    
    # 检查 node_modules 是否存在
    node_modules = frontend_dir / "node_modules"
    need_install = not node_modules.exists() or force_install
    
    if need_install and auto_install:
        click.echo("\n正在安装依赖...")
        try:
            # 清理旧的 node_modules（如果强制安装）
            if force_install and node_modules.exists():
                click.echo("清理旧的 node_modules...")
                shutil.rmtree(node_modules)
            
            # 清理 package-lock.json（如果有问题）
            lock_file = frontend_dir / "package-lock.json"
            if force_install and lock_file.exists():
                lock_file.unlink()
            
            # 运行 npm install
            subprocess.run([npm_cmd, 'install'], check=True)
            click.echo("✓ 依赖安装完成")
        except subprocess.CalledProcessError as e:
            click.echo(f"错误：依赖安装失败 - {e}", err=True)
            click.echo("\n可以尝试:")
            click.echo("  1. 手动删除 node_modules 目录后重试")
            click.echo("  2. 使用 --force-install 参数强制重新安装")
            click.echo("  3. 检查网络连接和 npm 源设置")
            sys.exit(1)
    elif need_install and not auto_install:
        click.echo("警告：未检测到 node_modules，请运行 'npm install' 安装依赖")
        if not click.confirm("是否现在安装依赖？"):
            sys.exit(1)
    
    # 构建或启动
    try:
        # 构建生产版本
        # 注意：根据 vite.config.js，构建输出到 ../static/dist
        dist_dir = frontend_dir.parent / "static" / "dist"
        
        # 检查是否需要构建
        need_build = not dist_dir.exists() or build_only
        
        # 如果 dist 不存在或明确要求构建，则进行构建
        if need_build:
            click.echo("\n正在构建生产版本...")
            subprocess.run([npm_cmd, 'run', 'build'], check=True)
            
            if dist_dir.exists():
                # 统计文件
                files = list(dist_dir.rglob('*'))
                file_count = len([f for f in files if f.is_file()])
                total_size = sum(f.stat().st_size for f in files if f.is_file())
                click.echo(f"\n✓ 构建完成！")
                click.echo(f"  - 输出目录: {dist_dir}")
                click.echo(f"  - 文件数量: {file_count}")
                click.echo(f"  - 总大小: {total_size / 1024 / 1024:.2f} MB")
            else:
                click.echo("错误：构建失败，未生成输出目录", err=True)
                sys.exit(1)
        
        # 如果不是仅构建模式，启动生产服务器
        if not build_only:
            if not dist_dir.exists():
                click.echo("错误：未找到构建输出，请先运行构建", err=True)
                sys.exit(1)
            
            click.echo(f"\n正在启动生产版本服务器...")
            click.echo(f"  - 访问地址: http://localhost:{port}")
            if host != 'localhost':
                click.echo(f"  - 网络地址: http://{host}:{port}")
            click.echo(f"  - 静态文件: {dist_dir}")
            click.echo(f"  - API 地址: {api_url}")
            click.echo("\n按 Ctrl+C 停止服务器\n")
            
            # 使用 Python 内置的 HTTP 服务器提供静态文件
            import http.server
            import socketserver
            import urllib.request
            import urllib.parse
            import json
            
            class ProxyHandler(http.server.SimpleHTTPRequestHandler):
                def __init__(self, *args, **kwargs):
                    super().__init__(*args, directory=str(dist_dir), **kwargs)
                
                def proxy_request(self, method='GET', body=None):
                    """代理 API 请求到后端服务器"""
                    if self.path.startswith('/api/') or self.path.startswith('/ws/'):
                        # 构建目标 URL
                        target_url = api_url + self.path
                        
                        try:
                            # 准备请求
                            req = urllib.request.Request(target_url, method=method)
                            
                            # 复制请求头
                            for header, value in self.headers.items():
                                if header.lower() not in ['host', 'connection']:
                                    req.add_header(header, value)
                            
                            # 添加请求体
                            if body:
                                req.data = body
                            
                            # 发送请求
                            with urllib.request.urlopen(req, timeout=30) as response:
                                # 返回响应
                                self.send_response(response.getcode())
                                for header, value in response.headers.items():
                                    if header.lower() not in ['connection', 'transfer-encoding']:
                                        self.send_header(header, value)
                                self.end_headers()
                                self.wfile.write(response.read())
                            return True
                            
                        except urllib.error.HTTPError as e:
                            self.send_response(e.code)
                            self.end_headers()
                            self.wfile.write(e.read())
                            return True
                        except Exception as e:
                            self.send_error(502, f"Bad Gateway: {str(e)}")
                            return True
                    return False
                
                def do_GET(self):
                    # 先尝试代理 API 请求
                    if self.proxy_request('GET'):
                        return
                    
                    # 对于 index.html，注入 API URL
                    if self.path == '/' or self.path == '/index.html' or (
                        self.path != '/' and not Path(dist_dir / self.path[1:]).exists()
                    ):
                        # 读取 index.html
                        index_path = dist_dir / 'index.html'
                        if index_path.exists():
                            with open(index_path, 'r', encoding='utf-8') as f:
                                html_content = f.read()
                            
                            # 注入 API URL 配置（使用相对路径，因为我们会代理）
                            api_config = f'''
                            <script>
                                window.JETTASK_API_URL = '';  // 使用相对路径，由服务器代理
                                console.log('API requests will be proxied by server');
                            </script>
                            '''
                            
                            # 在 </head> 标签前注入配置
                            html_content = html_content.replace('</head>', api_config + '</head>')
                            
                            # 发送响应
                            self.send_response(200)
                            self.send_header('Content-type', 'text/html')
                            self.send_header('Content-Length', str(len(html_content.encode('utf-8'))))
                            self.end_headers()
                            self.wfile.write(html_content.encode('utf-8'))
                            return
                    
                    # 其他文件正常处理
                    return super().do_GET()
                
                def do_POST(self):
                    # 读取请求体
                    content_length = int(self.headers.get('Content-Length', 0))
                    body = self.rfile.read(content_length) if content_length > 0 else None
                    
                    # 代理 POST 请求
                    if self.proxy_request('POST', body):
                        return
                    
                    # 不支持的请求
                    self.send_error(405, "Method Not Allowed")
                
                def do_PUT(self):
                    content_length = int(self.headers.get('Content-Length', 0))
                    body = self.rfile.read(content_length) if content_length > 0 else None
                    if self.proxy_request('PUT', body):
                        return
                    self.send_error(405, "Method Not Allowed")
                
                def do_DELETE(self):
                    if self.proxy_request('DELETE'):
                        return
                    self.send_error(405, "Method Not Allowed")
                
                def log_message(self, format, *args):
                    # 自定义日志格式
                    click.echo(f"[{self.log_date_time_string()}] {format % args}")
            
            # 创建服务器
            class ReuseAddrTCPServer(socketserver.TCPServer):
                allow_reuse_address = True
                allow_reuse_port = True
            
            try:
                click.echo(f"正在绑定到 {host}:{port}...")
                httpd = ReuseAddrTCPServer((host, port), ProxyHandler)
                click.echo(f"✓ 服务器已启动，监听 {host}:{port}")
                click.echo(f"✓ API 请求将被代理到 {api_url}")
                httpd.serve_forever()
            except OSError as e:
                if e.errno == 98:  # Address already in use
                    click.echo(f"错误：端口 {port} 已被占用，请尝试其他端口", err=True)
                else:
                    click.echo(f"错误：{e}", err=True)
                sys.exit(1)
            except KeyboardInterrupt:
                pass
    except subprocess.CalledProcessError as e:
        click.echo(f"错误：命令执行失败 - {e}", err=True)
        sys.exit(1)
    except KeyboardInterrupt:
        click.echo("\n停止前端服务器")

def main():
    """主入口函数"""
    try:
        cli()
    except KeyboardInterrupt:
        click.echo("\nOperation cancelled by user")
        sys.exit(0)
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)

if __name__ == '__main__':
    main()