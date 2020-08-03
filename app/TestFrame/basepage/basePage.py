import json
import logging.config
from os import path

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from blackhandle.black_handle import black_handle


class BasePage:
    '''
    基类
    '''

    # 配置log
    conflog_path = path.join(path.dirname(path.abspath(__file__)), '../config/log.conf')
    logging.config.fileConfig(conflog_path)
    log = logging.getLogger()
    # 定义变量池
    _params = {}

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    @black_handle
    def find(self, by, locator=None):
        '''
        查找功能,加入装饰器实现黑名单处理
        :param by: 元素定位方式或定位方式和信息组成的元组
        :param locator: 元素信息或默认为空
        :return:
        '''
        logging.info(f'查找: {by, locator}')
        if locator is None:
            result = self.driver.find_element(*by)
        else:
            result = self.driver.find_element(by, locator)
        return result

    def finds(self, by, locator=None):
        '''
        查找多个元素
        :param by: 元素定位方式或定位方式和信息组成的元组
        :param locator: 元素信息或默认为空
        :return:
        '''
        logging.info(f'查找多个包含: {by, locator}的元素')
        if locator is None:
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by, locator)

    def find_and_click(self, locator):
        '''
        查找并点击
        :param locator: 元素信息
        :return:
        '''
        logging.info(f'点击{locator}')
        self.find(locator).click()

    def find_and_sendkeys(self, locator, value):
        '''
        查找并填写数据
        :param locator: 元素信息
        :param text: 需要填写的数据
        :return:
        '''
        logging.info(f'填入 : "{value}"')
        self.find(locator).send_keys(value)

    def find_by_scroll(self, value):
        '''
        滚动查找
        :param value: 需要查找的元素信息
        :return:
        '''
        logging.info(f'滚动查找{value}')
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable(new UiSelector()'
                                        '.scrollable(true).instance(0))'
                                        '.scrollIntoView(new UiSelector()'
                                        f'.text("{value}").instance(0));')

    def webdriver_wait(self, locator, timeout=10):
        '''
        封装显示等待直到指定元素出现
        :param locator: 等待的元素信息
        :param timeout: 等待时间
        :return:
        '''
        logging.info(f'等待: {locator}出现')
        element = WebDriverWait(self.driver, timeout).until(
            lambda x: x.find_element(*locator))
        return element

    def webdriver_wait_until_not(self, locator, timeout=10):
        '''
        封装显示等待直到不出现指定元素
        :param locator: 等待的元素信息
        :param timeout: 等待时间
        :return:
        '''
        logging.info(f'等待: {locator}消失')
        element = WebDriverWait(self.driver, timeout).until_not(
            lambda x: x.find_element(*locator))
        return element

    def set_implicitly_wait(self, seconds):
        '''
        封装隐式等待
        :param seconds: 等待时间
        :return:
        '''
        logging.info(f'隐式等待:{seconds}秒')
        self.driver.implicitly_wait(seconds)

    # 封装返回
    def back(self, num=1):
        '''
        :param num: 返回次数
        :return:
        '''
        logging.info(f'返回:{num}次')
        logging.info(f'back: {num}')
        for i in range(num):
            self.driver.back()

    def action_steps(self, steps_path, name):
        '''
        封装执行步骤函数
        :param steps_path: yaml文件地址
               name:yaml内的步骤名
        :return: 执行结果
        '''
        # 打开yaml文件
        with open(steps_path, encoding='utf-8') as f:
            steps = yaml.safe_load(f)[name]

        raw = json.dumps(steps)
        # yaml内参数化处理
        for key, value in self._params.items():
            raw = raw.replace('${' + key + '}', value)  # 可加repr:强行转换成str格式
        steps = json.loads(raw)
        # 判断需要执行的步骤
        for step in steps:
            if 'action' in step.keys():
                action = step['action']
                # 执行点击
                if 'click' == action:
                    self.find_and_click((step['by'], step['locator']))
                # 执行传入文字
                if 'send' == action:
                    self.find_and_sendkeys((step['by'], step['locator']), step['value'])
                # 执行滚动并查找
                if 'find_by_scroll' == action:
                    self.find_by_scroll(step['text'])
                # 执行查找
                if 'find' == action:
                    result = self.find(step['by'], step['locator'])
                    return result
                # 执行查找多个元素
                if 'finds' == action:
                    result = self.finds(step['by'], step['locator'])
                    return result

    def load_data(self, data_path):
        '''
        读取测试数据
        :param data_path: 测试数据地址
        :return:测试数据
        '''
        with open(data_path, encoding='utf-8') as f:
            result = yaml.safe_load(f)
        return result

    def screenshot(self, path):
        '''
        截图功能
        :param path:截图保存地址
        :return:
        '''
        self.driver.save_screenshot(path)
