from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

class BasePage:

    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "27dc7322"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps["noReset"] = "true"
        caps['skipServerInstallation'] = 'true'  # 跳过 uiautomator2 server的安装
        caps['skipDeviceInitialization'] = 'true'  # 跳过设备初始化
        # caps['dontStopAppOnReset'] = 'true'    # 启动之前不停止app
        caps['settings[waitForIdleTimeout]'] = 0

        # 与server 建立连接,初始化一个driver 创建session,返回一个sessionid
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        # 消毁session
        self.driver.quit()

    def find(self, by, locator):
        '''
        封装查找元素功能
        :param by: 查找方式参数
        :param locator: 元素信息参数
        :return:
        '''
        return self._driver.find_element(by, locator)
