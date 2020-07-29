from appium.webdriver.common.mobileby import MobileBy

from APPOPHomeWork.page.addContactPage import AddContactPage
from APPOPHomeWork.page.basePage import BasePage
from APPOPHomeWork.page.personInfoPage import PersonInfoPage
from APPOPHomeWork.page.searchNamePage import SearchNamePage


class ContactListPage(BasePage):
    addmember_text = "添加成员"
    search_element = (MobileBy.ID, "com.tencent.wework:id/h9z")
    search_member = (MobileBy.ID, 'com.tencent.wework:id/fxc')

    def goto_add_contact(self):
        self.find_by_scroll(self.addmember_text).click()
        return AddContactPage(self.driver)

    def goto_search_contact(self):
        self.find_and_click(self.search_element)
        return SearchNamePage(self.driver)

    def goto_choese_contact(self, name):
        self.find_by_scroll(name).click()
        return PersonInfoPage(self.driver)

    def get_del_res(self, name):
        locator = (MobileBy.XPATH, name)
        try:
            # self.webdriver_wait_until_not(locator)
            self.find_and_click(self.search_element)
            self.find_and_sendkeys(self.search_member, name)
            self.back()
            self.webdriver_wait_until_not(locator)
            self.find_by_scroll(name)
            self.webdriver_wait_until_not(locator)
        except:
            return False
        else:
            return True
        # self.find_and_click(self.search_element)
        # self.find_and_sendkeys(self.search_member)
