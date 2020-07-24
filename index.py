from test_workwx.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy


class Index(BasePage):

    def goto_contact(self):
        self.find(MobileBy.XPATH,'//*[@test="通讯录"]').click()
        return Contact(self.driver)

