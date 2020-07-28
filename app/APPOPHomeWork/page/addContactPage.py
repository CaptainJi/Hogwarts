from appium.webdriver.common.mobileby import MobileBy

from basePage import BasePage
from page.addManuallyPage import AddManuallyPage


class AddContactPage(BasePage):
    add_manual_element = (MobileBy.XPATH, "//android.widget.TextView[@text='手动输入添加']")
    toast_ele = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")

    def goto_add_manually(self):
        self.find_and_click(self.add_manual_element)
        return AddManuallyPage(self.driver)

    def get_toast(self):
        element = self.webdriver_wait(self.toast_ele)
        result = element.text
        return result
