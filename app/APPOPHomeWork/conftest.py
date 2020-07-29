import pytest


# 测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
def pytest_collection_modifyitems(items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        print(item.nodeid)
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
