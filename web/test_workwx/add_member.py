from selenium.webdriver.common.by import By

from test_workwx.base_page import BasePage


class AddMember(BasePage):

    def add_member(self):
        self.find(By.ID, 'username').send_keys('哈哈')
        self.find(By.ID, 'memberAdd_acctid').send_keys('123')
        self.find(By.ID, 'memberAdd_phone').send_keys('12345678901')
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        return True
