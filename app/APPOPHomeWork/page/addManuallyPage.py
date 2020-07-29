from appium.webdriver.common.mobileby import MobileBy

from APPOPHomeWork.page.basePage import BasePage


class AddManuallyPage(BasePage):
    name_element = (MobileBy.XPATH, "//*[contains(@text, '姓名')]/../*[@class='android.widget.EditText']")
    gender_element = (MobileBy.XPATH, "//*[contains(@text, '性别')]/..//*[@text='男']")
    male_ele = (MobileBy.XPATH, "//*[@text='男']")
    female_ele = (MobileBy.XPATH, "//*[@text='女']")
    phonenum_ele = (MobileBy.XPATH, "//*[@text='手机号']")
    save_ele = (MobileBy.XPATH, "//*[@text='保存']")

    def set_name(self, name):
        self.find_and_sendkeys(self.name_element, name)
        return self

    def set_gander(self, gender):
        self.webdriver_wait(self.male_ele)
        self.find_and_click(self.gender_element)
        if gender == '男':
            # self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
            self.find_and_click(self.male_ele)
        else:
            self.find_and_click(self.female_ele)
            # self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()

        return self

    def set_phonenum(self, phonenum):
        self.find_and_sendkeys(self.phonenum_ele, phonenum)
        return self

    def click_save(self):
        self.find_and_click(self.save_ele)
        from APPOPHomeWork.page.addContactPage import AddContactPage
        return AddContactPage(self.driver)
