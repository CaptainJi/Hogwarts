from appium.webdriver.common.mobileby import MobileBy

from basepage.basePage import BasePage

search_input_element = (MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']")


class SearchPage(BasePage):
    def search(self, stock_name):
        # 设置变量名
        self._params['stock_name'] = stock_name
        self.action_steps(steps_path='../steps/search.yml', name='search')
