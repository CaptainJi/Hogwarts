from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Register:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def register(self):
        '''
        输入内容
        点击下拉框
        :return:
        '''
        self.driver.find_element(By.CSS_SELECTOR, '#corp_name').send_keys('哈哈哈哈')
        self.driver.find_element(By.CSS_SELECTOR, '#manager_name').send_keys('哈哈哈哈')
        return True
