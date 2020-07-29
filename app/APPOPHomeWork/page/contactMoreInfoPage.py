from appium.webdriver.common.mobileby import MobileBy

from APPOPHomeWork.page.basePage import BasePage
from APPOPHomeWork.page.editMembersPage import EditMembersPage

edit_element = (MobileBy.XPATH, "//*[@text='编辑成员']")


class ContactMoreInfoPage(BasePage):
    def goto_edit_members(self):
        self.find_and_click(edit_element)
        return EditMembersPage(self.driver)
