import logging.config
from os import path
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    conlog_path = path.join(path.dirname(path.abspath(__file__)), '../config/log.conf')
    logging.config.fileConfig(conlog_path)
    log = logging.getLogger()

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        # logging.info(f'find: {locator}')
        # print(locator)
        return self.driver.find_element(*locator)

    def find_and_click(self, locator):
        logging.info('click')
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
