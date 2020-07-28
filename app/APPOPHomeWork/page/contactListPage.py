from appium.webdriver.common.mobileby import MobileBy

from basePage import BasePage
from page.addContactPage import AddContactPage
from page.personInfoPage import PersonInfoPage
from page.searchNamePage import SearchNamePage


class ContactListPage(BasePage):
    addmember_text = "添加成员"
    search_element = (MobileBy.ID, "com.tencent.wework:id/h9z")
    search_member = (MobileBy.ID, 'com.tencent.wework:id/h9l')

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
            self.webdriver_until_not(locator)
        except:
            return True
        else:
            return False
        # self.find_and_click(self.search_element)
        # self.find_and_sendkeys(self.search_member)
