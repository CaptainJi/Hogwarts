import pytest


@pytest.fixture(scope='function', autouse=True)
def def_setup_tearDown():
    print("[开始计算]")
    yield
    print('\n[计算结束]')
