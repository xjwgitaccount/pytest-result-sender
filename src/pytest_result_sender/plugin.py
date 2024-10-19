
from datetime import datetime


def pytest_configure(config):
    # 配置加载完毕之后执行，所有测试用例执行前执行

    print(f"{datetime.now()} pytest开始执行了")


def pytest_unconfigure(config):
    # 配置卸载完毕之后执行，所有测试用例执行后执行

    print(f"{datetime.now()} pytest结束执行")