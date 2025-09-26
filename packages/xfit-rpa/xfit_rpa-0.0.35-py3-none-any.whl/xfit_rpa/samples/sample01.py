from xfit_rpa.core import XApp, XPage, XModule, XAction
from xfit_rpa.engine import XEngine
from xfit_rpa.executor.mock import MockPage, MockExecutor
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class LoginPage(XPage, register_name="sample01.login"):
    name = "sample01.login"
    description = "Sample01 Login Page"

    class LoginModule(XModule, register_name="sample01.login.login_form"):
        name = "login_form"
        description = "Sample01 Login Form"

        def _init_actions(self):
            self.add_action(
                XAction(
                    name="input_username",
                    action={type: 'fill'},
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


class Sample01App(XApp, register_name="sample01"):
    name = "sample01"


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
