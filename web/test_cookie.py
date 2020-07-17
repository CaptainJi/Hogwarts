import shelve

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# 使用cookie方式操作
class TestCookies():
    def setup(self):
        # 复用浏览器获取cookie
        chrome_options = Options()
        # chrome_options.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=chrome_options)
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.maximize_window()

    # 获取cookies并存储到shelve数据库中
    # def test_get_cookies(self):
    #     # 获取cookies
    #     get_cookies = self.driver.get_cookies()
    #     # 创建或者打开一个数据库
    #     db = shelve.open("./data/cookies")
    #     # 将数据存储到 shelve 中
    #     db["./data/cookies"] = get_cookies
    #     print(db["./data/cookies"])

    def test_cookie(self):

        # 取出数据
        db = shelve.open("./data/cookies")
        cookies = db["./data/cookies"]
        # # 打印 cookie
        print(cookies)
        # 把字典加入到 driver 的 cookie 中
        for cookie in cookies:
            # 处理”ecpiry“键值已防止cookie过期
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        # 企业微信操作部分
        self.driver.find_element_by_css_selector(
            '#indexTop > div.index_top_inside > aside > a.index_top_operation_loginBtn').click()
        sleep(2)
        self.driver.find_element_by_css_selector('#menu_contacts > span').click()
        sleep(3)
        db.close()

    def teardown(self):
        self.driver.quit()
