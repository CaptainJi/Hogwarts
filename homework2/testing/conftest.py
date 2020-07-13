import pytest
import yaml


# 测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        print(item.nodeid)
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.fixture(scope='function', autouse=True)
def setup():
    print("\n[开始计算]")
    yield
    print('\n[计算结束]')


# @pytest.fixture(scope='module', autouse=True)
# def teardown():
#     print('\n[计算结束]')


def pytest_addoption(parser):
    mygroup = parser.getgroup('Captain')
    mygroup.addoption('--env', default='test', dest='env', help='set your run env')


@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env", default='test')
    if myenv == 'test':
        datapath = 'datas/test/data.yaml'

    if myenv == 'dev':
        datapath = 'datas/dev/data.yaml'

    with open(datapath) as f:
        datas = yaml.safe_load(f)

    return myenv, datas
