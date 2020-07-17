from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options


class TestWorkWeiXin:
    # 浏览器复用：
    # 关闭浏览器后命令行输入：chrome - -remote - debugging - port = 9222
    def setup(self):
        chrome_options = Options()
        chrome_options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_options)
        # self.driver.maximize_window()

    def test_address(self):
        self.driver.get('https://work.weixin.qq.com/')
        sleep(2)
        self.driver.find_element_by_css_selector(
            '#indexTop > div.index_top_inside > aside > a.index_top_operation_loginBtn.one-pan-link-mark').click()
        sleep(2)
        self.driver.find_element_by_css_selector('#menu_contacts > span').click()
        sleep(3)

    def teardown(self):
        self.driver.quit()
