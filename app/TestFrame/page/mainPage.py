from appium.webdriver.common.mobileby import MobileBy

from basepage.basePage import BasePage
from page.marketPage import MarketPage


# market = (MobileBy.XPATH, '//*[@resource-id="android:id/tabs"]//*[@text="行情"]')
# steps_path='../steps/main.yml'

class MainPage(BasePage):

    def goto_market(self, stock_name):
        '''
        进入行情页面
        :param stock_name: 用此参数的值替换步骤yaml中${stock_name}的内容以实现数据驱动
        :return:
        '''
        # steps=self.load_steps(steps_path='../steps/main.yml')
        # for step in steps:
        #     if 'action' in step.keys():
        #         action = step['action']
        #         if 'click' == action:
        #             self.find(step['by'],step['locator']).click()

        self._params['stock_name'] = stock_name
        self.action_steps(steps_path='../steps/main.yml', name='goto_main')
        return MarketPage(self.driver)
