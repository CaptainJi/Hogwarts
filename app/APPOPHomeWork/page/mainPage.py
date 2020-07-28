from appium.webdriver.common.mobileby import MobileBy

from basePage import BasePage
from page.contactListPage import ContactListPage


class MainPage(BasePage):
    contactlist = (MobileBy.XPATH, "//android.widget.TextView[@text='通讯录']")

    def goto_contactlist(self):
        self.find_and_click(self.contactlist)
        return ContactListPage(self.driver)
