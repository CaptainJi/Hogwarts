from appium.webdriver.common.mobileby import MobileBy

from basepage.basePage import BasePage
from page.searchPage import SearchPage

action_search_element = (MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']")


class MarketPage(BasePage):
    def goto_search(self):
        self.find_and_click(action_search_element)
        return SearchPage(self.driver)
