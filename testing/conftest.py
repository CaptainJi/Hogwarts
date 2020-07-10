import pytest


@pytest.fixture(scope='function', autouse=True)
def setup():
    print("\n[开始计算]")
    yield
    print('\n[计算结束]')
# @pytest.fixture(scope='module', autouse=True)
# def teardown():
#     print('\n[计算结束]')
