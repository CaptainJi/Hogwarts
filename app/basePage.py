from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

class BasePage:
    driver = None

    def __init__(self,driver:webdriver = None):
        if driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "27dc7322"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "true"
            caps["noReset"] = "true"
            caps["automationName"] = "UiAutomator2"
            # caps['skipServerInstallation'] = 'true'  # 跳过 uiautomator2 server的安装
            # caps['skipDeviceInitialization'] = 'true'  # 跳过设备初始化
            # caps['dontStopAppOnReset'] = 'true'    # 启动之前不停止app
            caps['settings[waitForIdleTimeout]'] = 0
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(10)

        else:
            self.driver = driver
            self.driver.implicitly_wait(10)

    def find(self, by, locator):
        '''
        封装查找元素功能
        :param by: 查找方式参数
        :param locator: 元素信息参数
        :return:
        '''
        return self.driver.find_element(by, locator)
