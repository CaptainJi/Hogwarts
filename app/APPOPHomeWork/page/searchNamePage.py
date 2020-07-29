from appium.webdriver.common.mobileby import MobileBy

from APPOPHomeWork.page.basePage import BasePage


class SearchNamePage(BasePage):
    search_element = (MobileBy.ID, "com.tencent.wework:id/fxc")

    def search_name(self, name):
        self.find_and_sendkeys(self.search_element, name)
        return self
