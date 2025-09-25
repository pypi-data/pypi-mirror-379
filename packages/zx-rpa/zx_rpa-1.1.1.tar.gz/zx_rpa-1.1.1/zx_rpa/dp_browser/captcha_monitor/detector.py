"""
验证码检测引擎

负责执行验证码检测逻辑，支持多种检测策略和处理器
"""
import time
import random
from typing import Optional, Dict, Any, List, Tuple
from loguru import logger


class CaptchaDetector:
    """验证码检测引擎"""
    
    def __init__(self, config_manager):
        """初始化检测引擎
        
        Args:
            config_manager: 配置管理器实例
        """
        self.config_manager = config_manager
        logger.debug("验证码检测引擎初始化完成")
    
    def detect_after_action(self, tab, platform_name: str, action_type: str, 
                          selector: str) -> Tuple[bool, Optional[str], Optional[str]]:
        """在操作后执行验证码检测
        
        Args:
            tab: DrissionPage的tab对象
            platform_name (str): 平台名称
            action_type (str): 操作类型（click、input等）
            selector (str): 元素选择器
            
        Returns:
            Tuple[bool, Optional[str], Optional[str]]: 
                (是否检测到验证码, 匹配的选择器, 处理器名称)
        """
        logger.debug("开始验证码检测，平台: {}, 操作: {}, 选择器: {}", 
                    platform_name, action_type, selector)
        
        # 获取等待时间配置
        wait_time = self._calculate_wait_time(platform_name, selector)
        logger.debug("计算等待时间: {}秒", wait_time)
        
        # 执行阻塞检测
        return self._blocking_detection(tab, platform_name, wait_time)
    
    def _calculate_wait_time(self, platform_name: str, selector: str) -> float:
        """计算等待时间
        
        Args:
            platform_name (str): 平台名称
            selector (str): 元素选择器
            
        Returns:
            float: 等待时间（秒）
        """
        timing_config = self.config_manager.get_timing_config(platform_name)
        base_wait = timing_config.get("base_block_wait", 0.65)
        randomize_max = timing_config.get("randomize_max", 1.0)
        
        # 基础等待时间 + 随机化
        wait_time = base_wait + random.uniform(0, randomize_max - base_wait)
        
        # 检查是否为高危操作
        if self.config_manager.is_high_risk_action(platform_name, selector):
            high_risk_additional = timing_config.get("high_risk_additional", 2.0)
            wait_time += high_risk_additional
            logger.debug("高危操作，增加等待时间: {}秒", high_risk_additional)
        
        return wait_time
    
    def _blocking_detection(self, tab, platform_name: str, 
                          total_wait_time: float) -> Tuple[bool, Optional[str], Optional[str]]:
        """执行阻塞式检测
        
        Args:
            tab: DrissionPage的tab对象
            platform_name (str): 平台名称
            total_wait_time (float): 总等待时间
            
        Returns:
            Tuple[bool, Optional[str], Optional[str]]: 检测结果
        """
        timing_config = self.config_manager.get_timing_config(platform_name)
        scan_interval = timing_config.get("scan_interval", 0.10)
        
        handlers = self.config_manager.get_captcha_handlers(platform_name)
        if not handlers:
            logger.debug("平台无验证码处理器配置: {}", platform_name)
            time.sleep(total_wait_time)
            return False, None, None
        
        # 轮询检测
        elapsed_time = 0.0
        while elapsed_time < total_wait_time:
            # 检查每个处理器
            for handler_config in handlers:
                selector = handler_config.get("selector")
                handler_name = handler_config.get("handler")
                
                if self._check_captcha_element(tab, selector):
                    logger.debug("检测到验证码: {}, 处理器: {}", 
                               handler_config.get("name"), handler_name)
                    return True, selector, handler_name
            
            # 等待下一次检测
            time.sleep(scan_interval)
            elapsed_time += scan_interval
        
        logger.debug("验证码检测完成，未发现验证码")
        return False, None, None
    
    def _check_captcha_element(self, tab, selector: str) -> bool:
        """检查验证码元素是否存在
        
        Args:
            tab: DrissionPage的tab对象
            selector (str): 元素选择器
            
        Returns:
            bool: 元素是否存在且可见
        """
        try:
            if not selector:
                return False
                
            # 使用DrissionPage的元素检测
            element = tab.ele(selector, timeout=0.1)
            if element:
                # 检查元素是否可见
                return element.states.is_displayed
            return False
        except Exception as e:
            logger.debug("检测验证码元素异常: {}, 选择器: {}", str(e), selector)
            return False
    
    def quick_check(self, tab, platform_name: str) -> Tuple[bool, Optional[str], Optional[str]]:
        """快速检测验证码（不等待）
        
        Args:
            tab: DrissionPage的tab对象
            platform_name (str): 平台名称
            
        Returns:
            Tuple[bool, Optional[str], Optional[str]]: 检测结果
        """
        handlers = self.config_manager.get_captcha_handlers(platform_name)
        
        for handler_config in handlers:
            selector = handler_config.get("selector")
            handler_name = handler_config.get("handler")
            
            if self._check_captcha_element(tab, selector):
                logger.debug("快速检测到验证码: {}", handler_config.get("name"))
                return True, selector, handler_name
        
        return False, None, None
