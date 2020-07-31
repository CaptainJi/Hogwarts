from appium.webdriver.common.mobileby import MobileBy

from basepage.basePage import BasePage

search_input_element = (MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']")


class SearchPage(BasePage):
    def search(self):
        seartch_input = self.find(search_input_element)
        seartch_input.send_keys('阿里巴巴')
        seartch_input.click()
