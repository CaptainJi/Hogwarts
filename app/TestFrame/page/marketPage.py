from appium.webdriver.common.mobileby import MobileBy

from basepage.basePage import BasePage
from page.searchPage import SearchPage

action_search_element = (MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']")


class MarketPage(BasePage):
    def goto_search(self):
        # self.find(action_search_element).click()
        self.action_steps(steps_path='../steps/market.yml', name='goto_market')
        return SearchPage(self.driver)
