import logging

from xfit_rpa.core import XApp, XPage, XModule, XAction
from xfit_rpa.engine import XEngine
from xfit_rpa.executor.mock import MockPage, MockExecutor

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class LoginPage(XPage, register_name="sample01.login"):
    name = "sample01.login"
    description = "Sample01 Login Page"

    def __post_init__(self):
        super().__post_init__()

        login_form = LoginModule(
            default_params={"retry": 3}
        )

        # 链式调用添加动作
        login_form.add_action(
            XAction(
                name="input_username",
                action="fill",
                selector="#username",
                default_params={"value": ""}
            )
        ).add_action(
            XAction(
                name="input_password",
                action="fill",
                selector="#password",
                default_params={"value": ""}
            )
        )

        self.add_task_module(login_form)


class LoginModule(XModule, register_name="sample01.login.login_form"):
    name = "login_form"
    description = "Sample01 Login Form"


class Sample01App(XApp, register_name="sample01"):
    name = "sample01"

    # def __post_init__(self):
    #     self._setup()
    #
    # def _setup(self):
    #     # 硬编码定义基本结构
    #     login_page = LoginPage(
    #         url="https://login.demo00.com",
    #         default_params={"timeout": 30}
    #     )
    #
    #     login_form = LoginPage.LoginModule(
    #         default_params={"retry": 3}
    #     )
    #
    #     # 链式调用添加动作
    #     login_form.add_action(
    #         XAction(
    #             name="input_username",
    #             action_type="fill",
    #             selector="#username",
    #             default_params={"value": ""}
    #         )
    #     ).add_action(
    #         XAction(
    #             name="input_password",
    #             action_type="fill",
    #             selector="#password",
    #             default_params={"value": ""}
    #         )
    #     )
    #
    #     # 链式调用添加模块和页面
    #     login_page.add_task_module(login_form)
    #     self.add_task_page(login_page)
    #     pass


def main():
    # 从配置文件创建引擎
    from pathlib import Path
    page = MockPage()
    executor = MockExecutor()
    engine = XEngine(page, executor)
    engine.run_from_yaml_config(Path('sample01.conf.yaml').resolve())


if __name__ == "__main__":
    try:
        main()
    finally:
        print("Done")
