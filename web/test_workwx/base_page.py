from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _driver = None
    _base_url = ''

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            chrome_options = Options()
            # 浏览器复用命令 chrome --remote-debugging-port=9222
            chrome_options.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(options=chrome_options)
            self._driver.implicitly_wait(10)
        else:
            self._driver = driver

        if self._base_url != '':
            self._driver.get(self._base_url)

    def find(self, by, locator):
        '''
        封装查找元素功能
        :param by: 查找方式参数
        :param locator: 元素信息参数
        :return:
        '''
        return self._driver.find_element(by, locator)

    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)

    def wait_for_click(self, locator):
        '''
        显示等待元素可点击
        :param locator:等待条件
        :return:
        '''
        WebDriverWait(self._driver, 10).until(expected_conditions.element_to_be_clickable(locator))

    def wait_for_condition(self, condition):
        '''
        满足condition的显示等待
        :param condition: 等待条件
        :return:
        '''
        WebDriverWait(self._driver, 20).until(condition)
