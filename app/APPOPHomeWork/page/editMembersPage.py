from appium.webdriver.common.mobileby import MobileBy

from basePage import BasePage

del_element = (MobileBy.XPATH, '//*[@text="删除成员"]')
del_member = '删除成员'
confirm_del_element = (MobileBy.XPATH, '//*[@text="确定"]')


class EditMembersPage(BasePage):
    def del_member(self):
        self.webdriver_wait(del_element)
        self.find_by_scroll(del_member).click()
        self.webdriver_wait(confirm_del_element)
        self.find_and_click(confirm_del_element)
        from page.contactListPage import ContactListPage
        return ContactListPage(self.driver)
