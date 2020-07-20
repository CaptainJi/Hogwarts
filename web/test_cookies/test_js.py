import time

from test_cookies.base import Base


class TestJS(Base):
    # @pytest.mark.skip
    # def test_js_scroll(self):
    #     self.driver.get('http://www.baidu.com')
    #     self.driver.find_element_by_id('kw').send_keys('selenium')
    #     # 使用JS方式获取元素
    #     element = self.driver.execute_script('return document.getElementById("su")')
    #     element.click()
    #     time.sleep(2)
    #     self.driver.execute_script('document.documentElement.scrollTop=10000')
    #     time.sleep(2)
    #     self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
    #     time.sleep(3)
    #     # 获取性能数据并打印
    #     # for code in ['return document.title','return JSON.stringify(performance.timing)']:
    #     print(self.driver.execute_script('return document.title;return JSON.stringify(performance.timing)'))

    def test_datatime(self):
        self.driver.get('http://www.12306.cn')
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
        self.driver.execute_script("document.getElementById('train_date').removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")
        print(self.driver.execute_script("return document.getElementById('train_date').value"))

        # self.driver.execute_script("document.getElementById('train_date').value='2021-12-30'")
        time.sleep(1)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
        time.sleep(3)
