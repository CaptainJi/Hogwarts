from appium.webdriver.common.mobileby import MobileBy

from APPOPHomeWork.page.addContactPage import AddContactPage
from APPOPHomeWork.page.basePage import BasePage
from APPOPHomeWork.page.searchNamePage import SearchNamePage


class ContactListPage(BasePage):
    addmember_text = "添加成员"
    search = (MobileBy.ID, "com.tencent.wework:id/h9z")

    def goto_add_contact(self):
        self.find_by_scroll(self.addmember_text).click()
        return AddContactPage(self.driver)

    def goto_search_contact(self):
        self.find_and_click(self.search)
        return SearchNamePage()
