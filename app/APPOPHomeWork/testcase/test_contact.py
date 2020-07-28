from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from basePage import BasePage
from page.app import App


class TestContact:

    def setup_class(self):
        self.app = App()
        self.app.start()

    # def setup(self):
    #     self.app.start()

    def test_add_contact(self):
        name = "Cola"
        gender = "女"
        phonenum = "13700000001"
        res = self.app.goto_main().goto_contactlist().goto_add_contact().goto_add_manually().set_name(name).set_gander(
            gender).set_phonenum(phonenum).click_save()
        text = res.get_toast()
        assert '成功' in text
        self.app.back()

    def test_del_contact(self):
        name = "Cola"
        res = self.app.goto_main().goto_contactlist().goto_choese_contact(
            name).goto_more().goto_edit_members().del_member().get_del_res(name)
        assert name not in res
