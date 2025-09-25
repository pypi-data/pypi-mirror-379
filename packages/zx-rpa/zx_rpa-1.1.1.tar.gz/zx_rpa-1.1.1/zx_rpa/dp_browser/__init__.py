"""
DrissionPage通用工具封装
提供跨平台的浏览器自动化通用方法和验证码监控框架

from zx_rpa.dp_browser import CommonActions, CaptchaMonitor

# 基础通用操作
actions = CommonActions(tab)

# 验证码监控
monitor = CaptchaMonitor(browser=browser, platform="guangguang")

## 通用操作
- 等待元素处理：CommonActions.wait_element_appear(selector, timeout)

## 验证码监控
- 创建监控实例：CaptchaMonitor(browser, platform, base_wait, high_risk_additional)
- 包装tab对象：monitor.wrap_tab(tab, platform)
- 快速检测验证码：monitor.quick_check_captcha()
"""

from .common_actions import CommonActions
from .captcha_monitor import CaptchaMonitor

__all__ = [
    'CommonActions',
    'CaptchaMonitor',
]
