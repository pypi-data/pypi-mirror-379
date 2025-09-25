"""
DrissionPage验证码监控框架

基于操作后阻塞检测的验证码监控框架，支持智能等待策略和平台化配置

from zx_rpa.dp_browser.captcha_monitor import CaptchaMonitor
from DrissionPage import Chromium

# 初始化监控
browser = Chromium()
monitor = CaptchaMonitor(
    browser=browser,
    platform="guangguang",
    base_wait=0.65,
    high_risk_additional=2.0
)

# 正常使用业务代码，自动监控验证码
tab = browser.new_tab("https://example.com")
xxx_tab = guangguang.talent_tab(tab)  # 自动被监控包装
xxx_tab.click_login_button()          # 自动检测验证码

## 核心功能
- 操作后阻塞检测：在click、input等操作后自动检测验证码
- 智能等待策略：基于操作风险级别的差异化等待时间
- 平台化配置：支持多平台的验证码检测规则配置
- 无缝集成：通过代理模式透明集成到现有业务代码
- Tab智能切换：自动跟随业务tab切换监控目标

## 对外方法
- 创建监控实例：CaptchaMonitor(browser, platform, base_wait, high_risk_additional)
- 包装tab对象：wrap_tab(tab, platform)
- 快速检测验证码：quick_check_captcha()
- 检查受监控操作：is_guarded_action(action_type)
"""

from .monitor import CaptchaMonitor
from .config_manager import ConfigManager
from .detector import CaptchaDetector
from .tab_proxy import TabProxy
from .element_proxy import ElementProxy

__all__ = [
    'CaptchaMonitor',
    'ConfigManager', 
    'CaptchaDetector',
    'TabProxy',
    'ElementProxy'
]
