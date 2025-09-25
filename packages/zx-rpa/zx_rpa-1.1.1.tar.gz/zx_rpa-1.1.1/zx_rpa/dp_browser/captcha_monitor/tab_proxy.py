"""
DrissionPage Tab代理包装器

拦截tab的ele()方法，返回包装后的元素代理对象
"""
from typing import Any
from loguru import logger
from .element_proxy import ElementProxy


class TabProxy:
    """DrissionPage Tab代理包装器"""
    
    def __init__(self, original_tab, monitor):
        """初始化Tab代理
        
        Args:
            original_tab: 原始DrissionPage tab对象
            monitor: 监控管理器实例
        """
        self._original_tab = original_tab
        self._monitor = monitor
        logger.debug("创建Tab代理，tab_id: {}", id(original_tab))
    
    def ele(self, locator, *args, **kwargs):
        """代理ele方法，返回包装后的元素代理
        
        Args:
            locator: 元素定位符
            *args: 其他位置参数
            **kwargs: 其他关键字参数
            
        Returns:
            ElementProxy: 包装后的元素代理对象
        """
        logger.debug("拦截ele方法，定位符: {}", locator)
        
        # 调用原始tab的ele方法获取元素
        original_element = self._original_tab.ele(locator, *args, **kwargs)
        
        # 如果元素不存在，直接返回None
        if original_element is None:
            return None
        
        # 包装成元素代理并返回
        return ElementProxy(original_element, self._monitor, str(locator))
    
    def eles(self, locator, *args, **kwargs):
        """代理eles方法，返回包装后的元素代理列表
        
        Args:
            locator: 元素定位符
            *args: 其他位置参数
            **kwargs: 其他关键字参数
            
        Returns:
            list: 包装后的元素代理对象列表
        """
        logger.debug("拦截eles方法，定位符: {}", locator)
        
        # 调用原始tab的eles方法获取元素列表
        original_elements = self._original_tab.eles(locator, *args, **kwargs)
        
        # 包装每个元素
        wrapped_elements = []
        for i, element in enumerate(original_elements):
            if element is not None:
                selector = f"{locator}[{i}]"
                wrapped_elements.append(ElementProxy(element, self._monitor, selector))
        
        return wrapped_elements
    
    def wait(self):
        """代理wait属性，返回原始tab的wait对象"""
        return self._original_tab.wait
    
    def __getattr__(self, name: str) -> Any:
        """代理其他属性和方法访问
        
        Args:
            name (str): 属性或方法名
            
        Returns:
            Any: 原始tab的属性或方法
        """
        # 对于其他属性和方法，直接转发给原始tab
        attr = getattr(self._original_tab, name)
        
        # 如果是方法且可能影响页面状态，记录日志
        if callable(attr) and name in ['get', 'refresh', 'back', 'forward']:
            def wrapped_method(*args, **kwargs):
                logger.debug("Tab操作: {}", name)
                result = attr(*args, **kwargs)
                # 页面状态改变后，可能需要重新检测验证码
                return result
            return wrapped_method
        
        return attr
    
    @property
    def url(self) -> str:
        """获取当前页面URL"""
        return self._original_tab.url
    
    @property
    def title(self) -> str:
        """获取当前页面标题"""
        return self._original_tab.title
    
    def __str__(self) -> str:
        """字符串表示"""
        return f"TabProxy(url={self.url})"
    
    def __repr__(self) -> str:
        """对象表示"""
        return f"TabProxy(tab_id={id(self._original_tab)}, url='{self.url}')"
