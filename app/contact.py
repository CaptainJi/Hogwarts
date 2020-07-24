from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from basePage import BasePage


class Contact(BasePage):
    def __init__(self, driver: webdriver):
        self.driver = driver

    def add_contact(self, username, mobilephone):
        '''
        添加联系人:
        点击添加成员
        输入内容
        :return:
        '''
        print(f'开始添加联系人{username}')
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath('//*[@text="添加成员"]'))
        self.find(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable'
                                                '(new UiSelector().'
                                                'scrollable(true).'
                                                'instance(0)).'
                                                'scrollIntoView('
                                                'new UiSelector().'
                                                'text("添加成员").instance(0));').click()
        self.find(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        self.find(MobileBy.ID, 'com.tencent.wework:id/awt').send_keys(f'{username}')
        self.find(MobileBy.ID, 'com.tencent.wework:id/f1e').send_keys(f'{mobilephone}')
        self.find(MobileBy.XPATH, '//*[@text="设置部门"]').click()
        self.find(MobileBy.XPATH, "//*[contains(@text, '确定')]").click()
        # self.find(MobileBy.ID,'com.tencent.wework:id/g09').click()
        self.find(MobileBy.XPATH, '//*[@text="保存"]').click()
        # self.WebDriverWait(self.driver, 10).until(self.find(MobileBy.XPATH, "//*[@text='添加成功']"))
        try:
            toast = self.find(MobileBy.XPATH, "//*[@text='添加成功']").text
        except:
            print('添加失败')
            return False
        else:
            print(toast)
            return True

    def del_contact(self, username):
        '''
        删除联系人:
        点击联系人
        点击右上角更多
        点击编辑成员滑动查找删除成员

        :param self:
        :return:
        '''
        print(f'开始删除联系人{username}')
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(f'//*[@text="{username}"]'))
        self.find(MobileBy.XPATH, f"//*[@text='{username}']").click()
        self.find(MobileBy.ID, 'com.tencent.wework:id/h9p').click()
        self.find(MobileBy.XPATH, "//*[@text='编辑成员']").click()
        self.find(MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable'
                                                '(new UiSelector().'
                                                'scrollable(true).'
                                                'instance(0)).'
                                                'scrollIntoView('
                                                'new UiSelector().'
                                                'text("删除成员").instance(0));').click()
        # WebDriverWait(self.driver, 10).until(self.find(MobileBy.ID, 'com.tencent.wework:id/bci'))
        self.find(MobileBy.ID, 'com.tencent.wework:id/bci').click()
        try:
            self.find(MobileBy.XPATH, f"//*[@text='{username}']").click()
        except:
            print('删除成功')
            return True
        else:
            return False
