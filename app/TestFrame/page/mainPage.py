from appium.webdriver.common.mobileby import MobileBy

from basepage.basePage import BasePage
from page.marketPage import MarketPage

market = (MobileBy.XPATH, '//*[@resource-id="android:id/tabs"]//*[@text="行情"]')


class MainPage(BasePage):

    def goto_market(self):
        self.find(market).click()
        return MarketPage(self.driver)
