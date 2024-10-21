from datetime import datetime

import pytest
import requests

# 全局变量
data = {"passed": "", "failed": ""}


def pytest_configure(config: pytest.Config) -> None:
    # 配置加载完毕之后执行，所有测试用例执行前执行
    data["start_time"] = datetime.now()
    print(f"{datetime.now()} pytest开始执行了")
    # 配置文件中的内容获取
    print('测试这里是什么东西-----------' + config.getini("send_when"))
    data["send_when"] = config.getini("send_when")
    data["send_api"] = config.getini("send_api")


def pytest_unconfigure(config):
    # 配置卸载完毕之后执行，所有测试用例执行后执行
    data["end_time"] = datetime.now()
    print(f"{datetime.now()} pytest结束执行")

    data["duration"] = data["end_time"] - data["start_time"]
    print(data["duration"])

    send_result()

def send_result() -> None:
    if data["send_when"] == "on_fail" and data["failed"] == 0:
        return

    if not data["send_api"]:
        return

    url = data["send_api"]  # 动态指定结果发送位置

    content = f"""
    pytest自动化测试结果
    
    测试时间：{data['end_time']}
    用例数量：{data['total']}
    执行时长：{data['duration']}
    测试通过： < font color = 'green' > {data['passed']} < / font >
    测试失败： < font color = 'red' > {data['failed']} < / font >
    测试通过率：{data['pass_ratio']} % < br / >
    
    测试报告地址：http: // baidu.com
    """

    try:
        requests.post(
            url, json={"msgtype": "markdown", "markdown": {"content": content}}
        )
    except Exception:
        pass


def pytest_collection_finish(session: pytest.Session):
    # 用例加載完成之後，包含了所有用例
    data["total"] = len(session.items)


def pytest_addoption(parser):
    # 增加配置项
    parser.addini("send_when", help="什么时候发送结果")
    parser.addini("send_api", help="发送结果到何处")
