from appium.webdriver.common.mobileby import MobileBy

from page.basePage import BasePage
from page.contactMoreInfoPage import ContactMoreInfoPage

more_element = (MobileBy.ID, 'com.tencent.wework:id/h9p')


class PersonInfoPage(BasePage):
    def goto_more(self):
        self.find_and_click(more_element)
        return ContactMoreInfoPage(self.driver)
