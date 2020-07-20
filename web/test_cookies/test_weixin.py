import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestWorkWeiXin():

    def test_lonin(self):
        chrome_options = Options()
        # shell:chrome - -remote - debugging - port = 9222
        chrome_options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_options)

    def test_click_addres(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#apps')
        time.sleep(10)
        self.driver.find_element_by_css_selector('#menu_contacts > span').click()
