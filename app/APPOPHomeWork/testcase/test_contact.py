import logging.config

import pytest
import yaml

from page.app import App


class TestContact:
    with open('../data/data.yml', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    def setup_class(self):
        logging.info('开始测试')
        self.app = App()
        self.app.start()


    def teardown_class(self):
        logging.info('测试完成')
        self.app.stop()

    @pytest.mark.parametrize('name,gender,phonenum', data)
    def test_add_contact(self, name, gender, phonenum):
        # name = "Cola"
        # gender = "女"
        # phonenum = "13700000001"
        res = self.app.goto_main().goto_contactlist().goto_add_contact().goto_add_manually().set_name(name).set_gander(
            gender).set_phonenum(phonenum).click_save()
        text = res.get_toast()
        assert '成功' in text
        self.app.back()

    @pytest.mark.parametrize('name,gender,phonenum', data)
    def test_del_contact(self, name, gender, phonenum):
        # name = "Cola"
        res = self.app.goto_main().goto_contactlist().goto_choese_contact(
            name).goto_more().goto_edit_members().del_member().get_del_res(name)
        # assert name not in res
        assert res
        self.app.back()
