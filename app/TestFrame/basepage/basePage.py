import logging.config
from os import path
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    conlog_path = path.join(path.dirname(path.abspath(__file__)), '../config/log.conf')
    logging.config.fileConfig(conlog_path)
    log = logging.getLogger()

    _black_list = [(MobileBy.XPATH, '//*[contains(@text,"跳过")]')]
    _max_error_num = 2
    _error_num = 0

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def black_handle(fun):
        '''
        自定义装饰器
        :return:
        '''

        def find_black(self, *args, **kwargs):
            try:
                # 尝试执行fun
                fun(self, *args, **kwargs)
            except Exception as f:
                # 出现异常时判断计数器是否超过上限
                if self._error_num > self._max_error_num:
                    self._error_num = 0
                    raise f
                self._error_num += 1
                # 遍历黑名单,并点击关闭或跳过按钮来跳过弹窗
                for ele in self._black_list:
                    eles = self.finds(ele)
                    if len(eles) > 0:
                        logging.info(f'close popup{ele}')
                        eles[0].click()
                        # 再次执行fun
                        return fun(self, *args, **kwargs)
                raise f
            else:
                return fun(self, *args, **kwargs)

        return find_black

    @black_handle
    def find(self, by, locator=None):
        if locator is None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by, locator)

    # def find(self, by, locator=None):
    #     try:
    #         if locator is None:
    #             result = self.driver.find_element(*by)
    #         else:
    #             result = self.driver.find_element(by, locator)
    #         self._error_num = 0
    #         return result
    #     except Exception as f:
    #         if self._error_num > self._max_error_num:
    #             self._error_num = 0
    #             raise f
    #         self._error_num += 1
    #         for ele in self._black_list:
    #             eles = self.finds(ele)
    #             if len(eles) > 0:
    #                 eles[0].click()
    #                 return self.find(by, locator)
    #         raise f

    def finds(self, by, locator=None):
        logging.info(f'finds: {by, locator}')
        if locator is None:
            return self.driver.find_elements(*by)
        else:
            return self.driver.find_elements(by, locator)

    def find_and_click(self, locator):
        logging.info(f'click{locator}')
        self.find(locator).click()

    def find_and_sendkeys(self, locator, text):
        logging.info(f'sendkeys : {text}')
        self.find(locator).send_keys(text)

    def find_by_scroll(self, text):
        logging.info('find_by_scroll')
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable(new UiSelector()'
                                        '.scrollable(true).instance(0))'
                                        '.scrollIntoView(new UiSelector()'
                                        f'.text("{text}").instance(0));')

    def webdriver_wait(self, locator, timeout=10):
        logging.info(f'webdriver_wait: {locator}, timeout: {timeout}')
        element = WebDriverWait(self.driver, timeout).until(
            lambda x: x.find_element(*locator))
        return element

    def webdriver_wait_until_not(self, locator, timeout=10):
        logging.info(f'webdriver_wait: {locator}, timeout: {timeout}')
        element = WebDriverWait(self.driver, timeout).until_not(
            lambda x: x.find_element(*locator))
        return element

    def back(self, num=1):
        logging.info(f'back: {num}')
        for i in range(num):
            self.driver.back()
