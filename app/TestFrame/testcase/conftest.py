import os
import signal
import subprocess

import pytest


def pytest_collection_modifyitems(items):
    '''
    测试用例收集完成后,讲收集到的item的name和nodeid的中文显示在控制台中
    :param items:
    :return:
    '''
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


@pytest.fixture(scope='class', autouse=True)
def record():
    '''
    录制执行视频
    :return:
    '''
    cmd = 'scrcpy --record ../tmp/tmp.mp4'
    # 执行录制命令:stdout:标准输出通道;stderr:错误输出通道
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    yield
    # 结束录制:发送终止信号"crrl+c"
    os.kill(p.pid, signal.CTRL_C_EVENT)
