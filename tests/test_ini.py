from pathlib import Path

import pytest

pytest_plugins = 'pytester'  # 我是测试开发


@pytest.mark.parametrize(
    'send_when',
    ['every', 'on_fail']
)
def test_send_when(send_when, pytester: pytest.Pytester, tmp_path: Path):
    config_path = tmp_path.joinpath('pytest.ini')
    config_path.write_text(f'''
[pytest]
send_when = {send_when}
send_api = https://baidu.com
    ''')

    # 断言：配置加载成功
    config = pytester.parseconfig(config_path)
    assert config.getini('send_when') == send_when

    pytester.makepyfile(  # 构造场景，用力全部测试通过
        """
        def test_pass():
            ...
        """
    )

    pytester.runpytest('-c ', str(config_path))

@pytest.mark.parametrize(
    'send_api',
    ['http://baidu.com']
)
def test_send_api(send_api, pytester: pytest.Pytester, tmp_path):
    ...
