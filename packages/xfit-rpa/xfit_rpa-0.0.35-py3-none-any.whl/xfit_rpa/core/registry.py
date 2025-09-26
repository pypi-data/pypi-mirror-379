import logging
from typing import Dict, Type, Callable, Optional
from abc import ABCMeta


# 元类，自动注册业务结构类
class _ClassMeta(ABCMeta):
    """元类实现自动注册"""
    # _registry: Dict[str, Union[Type['XPage'], Type['XModule']]] = {}
    _registry: Dict[str, Type] = {}

    def __new__(mcls, name, bases, namespace, register_name: str = None):
        cls = super().__new__(mcls, name, bases, namespace)
        if register_name:
            mcls._registry[register_name] = cls
        return cls

    @classmethod
    def get_instance(cls, register_name: str, **kwargs) -> Optional[Type]:
        """按需创建实例"""
        # logging.info(f"Get instance of {register_name} with kwargs: {kwargs}")
        if register_name not in cls._registry:
            raise ValueError(f"Class {register_name} not registered")
        return cls._registry[register_name](**kwargs)

    @classmethod
    def get_registry(cls) -> Dict[str, Type]:
        """获取已注册的类名列表"""
        return cls._registry

    @classmethod
    def list_register_names(cls) -> list:
        """获取已注册的类名列表"""
        return list(cls._registry.keys())

    @classmethod
    def list_register_classes(cls) -> list:
        """获取已注册的类名列表"""
        return list(cls._registry.values())


# 插件管理器，管理动作函数注册
class PluginManager:
    _actions: Dict[str, Callable] = {}

    @classmethod
    def register_action(cls, name: str, func: Callable):
        if name in cls._actions:
            raise ValueError(f"Action '{name}' already registered")
        cls._actions[name] = func

    @classmethod
    def get_action(cls, name: str) -> Optional[Callable]:
        return cls._actions.get(name)

    @classmethod
    def list_actions(cls):
        return list(cls._actions.keys())


# 统一注册函数
def register_all():
    # App/Page/Module/Action通过元类自动注册，无需显式操作

    # 动作插件注册示例
    # import plugins.playwright.actions as pw_actions
    # PluginManager.register_action("playwright.click", pw_actions.click)
    # PluginManager.register_action("playwright.input", pw_actions.input_text)
    #
    # import plugins.uibot.actions as ub_actions
    # PluginManager.register_action("uibot.click", ub_actions.click)

    pass
