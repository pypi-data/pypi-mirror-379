"""
DrissionPage元素代理包装器

拦截元素的click、input等操作，在操作后触发验证码检测
"""
from typing import Any, Optional
from loguru import logger


class ElementProxy:
    """DrissionPage元素代理包装器"""
    
    def __init__(self, original_element, monitor, selector: str):
        """初始化元素代理
        
        Args:
            original_element: 原始DrissionPage元素对象
            monitor: 监控管理器实例
            selector (str): 元素选择器
        """
        self._original_element = original_element
        self._monitor = monitor
        self._selector = selector
        logger.debug("创建元素代理，选择器: {}", selector)
    
    def click(self, *args, **kwargs) -> Any:
        """代理click操作"""
        logger.debug("拦截click操作，选择器: {}", self._selector)
        
        # 执行原始操作
        result = self._original_element.click(*args, **kwargs)
        
        # 触发验证码检测
        self._trigger_captcha_detection("click")
        
        return result
    
    def input(self, *args, **kwargs) -> Any:
        """代理input操作"""
        logger.debug("拦截input操作，选择器: {}", self._selector)
        
        # 执行原始操作
        result = self._original_element.input(*args, **kwargs)
        
        # 触发验证码检测
        self._trigger_captcha_detection("input")
        
        return result
    
    def _trigger_captcha_detection(self, action_type: str):
        """触发验证码检测
        
        Args:
            action_type (str): 操作类型
        """
        try:
            # 检查是否为受监控的操作
            if not self._monitor.is_guarded_action(action_type):
                logger.debug("操作不在监控范围: {}", action_type)
                return
            
            # 执行验证码检测
            detected, selector, handler = self._monitor.detector.detect_after_action(
                self._monitor.current_tab,
                self._monitor.current_platform,
                action_type,
                self._selector
            )
            
            if detected:
                logger.debug("检测到验证码，选择器: {}, 处理器: {}", selector, handler)
                # 这里可以扩展处理逻辑
                self._handle_captcha_detected(selector, handler)
            
        except Exception as e:
            logger.debug("验证码检测异常: {}", str(e))
    
    def _handle_captcha_detected(self, selector: str, handler: str):
        """处理检测到的验证码
        
        Args:
            selector (str): 验证码选择器
            handler (str): 处理器名称
        """
        # 目前只记录日志，后续可扩展自动处理逻辑
        logger.debug("验证码处理 - 选择器: {}, 处理器: {}", selector, handler)
        
        # 可以在这里调用具体的验证码处理器
        # self._monitor.handle_captcha(selector, handler)
    
    def __getattr__(self, name: str) -> Any:
        """代理其他属性和方法访问
        
        Args:
            name (str): 属性或方法名
            
        Returns:
            Any: 原始元素的属性或方法
        """
        # 对于其他属性和方法，直接转发给原始元素
        attr = getattr(self._original_element, name)
        
        # 如果是方法，需要检查是否需要特殊处理
        if callable(attr) and name in ['submit', 'send_keys']:
            # 对于其他可能触发验证码的操作，也进行拦截
            def wrapped_method(*args, **kwargs):
                result = attr(*args, **kwargs)
                self._trigger_captcha_detection(name)
                return result
            return wrapped_method
        
        return attr
    
    def __str__(self) -> str:
        """字符串表示"""
        return f"ElementProxy({self._selector})"
    
    def __repr__(self) -> str:
        """对象表示"""
        return f"ElementProxy(selector='{self._selector}', element={repr(self._original_element)})"
