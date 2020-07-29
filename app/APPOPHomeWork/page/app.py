from appium import webdriver

from APPOPHomeWork.page.basePage import BasePage
from APPOPHomeWork.page.mainPage import MainPage


class App(BasePage):
    def start(self):
        '''
        启动app
        '''
        if self.driver == None:
            # 第一次调用start（）方法的时候driver 为None
            caps = {}
            caps["platformName"] = "android"
            # caps["deviceName"] = "127.0.0.1:7555"
            caps["deviceName"] = "27dc7322"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "true"
            caps['skipServerInstallation'] = 'true'  # 跳过 uiautomator2 server的安装
            caps['skipDeviceInitialization'] = 'true'  # 跳过设备初始化
            # caps['dontStopAppOnReset'] = 'true'    # 启动之前不停止app
            caps['settings[waitForIdleTimeout]'] = 120

            # 与server 建立连接,初始化一个driver 创建session,返回一个sessionid
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            # launch_app() 这个方法不需要传入任何参数， 会自动启动起来DesireCapa里面定义的activity
            # start_activity(packagename, activityname) 可以启动其它的应用的页面
            self.driver.launch_app()
        self.driver.implicitly_wait(20)
        return self

    def restart(self):
        '''
                重启app
                '''
        self.driver.close()
        self.driver.launch_app()
        return self

    def stop(self):
        '''
                停止 app
                '''
        self.driver.quit()

    def goto_main(self):
        '''
                进入首页
                '''
        return MainPage(self.driver)
