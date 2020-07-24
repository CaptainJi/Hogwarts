from selenium.webdriver.common.by import By

from test_workwx.register import Register


class Login:
    '''
    登陆页面的PO
    '''

    def __init__(self, driver):
        self.driver = driver

    def scan(self):
        '''
        扫描二维码
        '''
        pass

    def goto_login(self):
        '''
        点击企业注册
        进入到注册PO
        :return:注册PO
        '''
        self.driver.find_element(By.CSS_SELECTOR, '.login_registerBar_link').click()
        return Register(self.driver)
