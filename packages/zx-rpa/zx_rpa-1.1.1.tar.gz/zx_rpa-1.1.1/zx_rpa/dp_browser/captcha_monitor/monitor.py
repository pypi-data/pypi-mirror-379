"""
验证码监控管理器

主要负责管理验证码监控的整体流程，包括tab代理、配置管理和检测协调
"""
import importlib
from typing import Optional, Dict, Any
from loguru import logger
from .config_manager import ConfigManager
from .detector import CaptchaDetector
from .tab_proxy import TabProxy


class CaptchaMonitor:
    """验证码监控管理器"""
    
    _instance = None
    _initialized = False
    
    def __new__(cls, *args, **kwargs):
        """单例模式实现"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, browser=None, platform: str = "default", 
                 base_wait: float = 0.65, high_risk_additional: float = 2.0,
                 config_path: Optional[str] = None):
        """初始化验证码监控管理器
        
        Args:
            browser: 浏览器实例（可选）
            platform (str): 默认平台名称
            base_wait (float): 基础等待时间
            high_risk_additional (float): 高危操作附加等待时间
            config_path (str, optional): 自定义配置文件路径
        """
        # 避免重复初始化
        if self._initialized:
            return
            
        self.browser = browser
        self.current_platform = platform
        self.current_tab = None
        
        # 初始化配置管理器
        self.config_manager = ConfigManager(config_path)
        
        # 初始化检测引擎
        self.detector = CaptchaDetector(self.config_manager)
        
        # 应用自定义配置
        self._apply_custom_config(base_wait, high_risk_additional)
        
        # 启动监控
        self._start_monitoring()
        
        self._initialized = True
        logger.debug("验证码监控管理器初始化完成，平台: {}", platform)
    
    def _apply_custom_config(self, base_wait: float, high_risk_additional: float):
        """应用自定义配置参数
        
        Args:
            base_wait (float): 基础等待时间
            high_risk_additional (float): 高危操作附加等待时间
        """
        # 动态更新当前平台的配置
        if self.current_platform in self.config_manager.configs:
            config = self.config_manager.configs[self.current_platform]
            if "timing" not in config:
                config["timing"] = {}
            config["timing"]["base_block_wait"] = base_wait
            config["timing"]["high_risk_additional"] = high_risk_additional
            logger.debug("应用自定义配置，基础等待: {}s, 高危附加: {}s", 
                        base_wait, high_risk_additional)
    
    def _start_monitoring(self):
        """启动监控，拦截平台工厂函数"""
        try:
            self._patch_platform_factories()
            logger.debug("验证码监控已启动")
        except Exception as e:
            logger.debug("启动监控失败: {}", str(e))
    
    def _patch_platform_factories(self):
        """拦截平台工厂函数"""
        # 拦截guangguang平台
        self._patch_module_factories("zx_rpa.apis.guangguang")
        
        # 可以扩展其他平台
        # self._patch_module_factories("zx_rpa.apis.alibaba")
    
    def _patch_module_factories(self, module_name: str):
        """拦截指定模块的工厂函数
        
        Args:
            module_name (str): 模块名称
        """
        try:
            module = importlib.import_module(module_name)
            
            # 获取模块的所有导出函数
            if hasattr(module, '__all__'):
                factory_names = module.__all__
            else:
                # 如果没有__all__，获取所有不以下划线开头的函数
                factory_names = [name for name in dir(module) 
                               if not name.startswith('_') and callable(getattr(module, name))]
            
            # 拦截每个工厂函数
            for factory_name in factory_names:
                if hasattr(module, factory_name):
                    original_factory = getattr(module, factory_name)
                    wrapped_factory = self._create_wrapped_factory(original_factory, module_name)
                    setattr(module, factory_name, wrapped_factory)
                    logger.debug("拦截工厂函数: {}.{}", module_name, factory_name)
                    
        except ImportError as e:
            logger.debug("模块导入失败: {}, 错误: {}", module_name, str(e))
        except Exception as e:
            logger.debug("拦截模块工厂函数失败: {}, 错误: {}", module_name, str(e))
    
    def _create_wrapped_factory(self, original_factory, module_name: str):
        """创建包装后的工厂函数
        
        Args:
            original_factory: 原始工厂函数
            module_name (str): 模块名称
            
        Returns:
            function: 包装后的工厂函数
        """
        def wrapped_factory(tab, *args, **kwargs):
            # 包装tab对象
            wrapped_tab = self.wrap_tab(tab, self._extract_platform_name(module_name))
            
            # 调用原始工厂函数
            return original_factory(wrapped_tab, *args, **kwargs)
        
        return wrapped_factory
    
    def _extract_platform_name(self, module_name: str) -> str:
        """从模块名称提取平台名称
        
        Args:
            module_name (str): 模块名称
            
        Returns:
            str: 平台名称
        """
        # 从 "zx_rpa.apis.guangguang" 提取 "guangguang"
        parts = module_name.split('.')
        return parts[-1] if len(parts) > 0 else "default"
    
    def wrap_tab(self, tab, platform: str = None) -> TabProxy:
        """包装tab对象为代理
        
        Args:
            tab: 原始DrissionPage tab对象
            platform (str, optional): 平台名称
            
        Returns:
            TabProxy: 包装后的tab代理对象
        """
        if platform:
            self.current_platform = platform
        self.current_tab = tab
        
        logger.debug("包装tab对象，平台: {}", self.current_platform)
        return TabProxy(tab, self)
    
    def is_guarded_action(self, action_type: str) -> bool:
        """检查是否为受监控的操作类型
        
        Args:
            action_type (str): 操作类型
            
        Returns:
            bool: 是否为受监控操作
        """
        monitoring_config = self.config_manager.get_monitoring_config(self.current_platform)
        guarded_actions = monitoring_config.get("guarded_actions", ["click", "input"])
        return action_type in guarded_actions
    
    def quick_check_captcha(self) -> tuple:
        """快速检测当前页面是否有验证码
        
        Returns:
            tuple: (是否检测到, 选择器, 处理器名称)
        """
        if self.current_tab is None:
            return False, None, None
            
        return self.detector.quick_check(self.current_tab, self.current_platform)
