from appium.webdriver.common.mobileby import MobileBy

from app.basePage.basePage import BasePage
from app.common.contact import Contact


class Index(BasePage):

    def goto_contact(self):
        self.find(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        return Contact(self.driver)
