import pytest

from index import Index


class TestContact():
    def setup(self):
        self.index = Index()
    # 添加联系人用例
    @pytest.mark.parametrize('username', ['Cola'])
    def test_add_contact(self,username):
        result = self.index.goto_contact().add_contact(username)
        assert result
    # 删除联系人用例
    @pytest.mark.parametrize('username', ['Cola'])
    def test_del_contact(self,username):
        result = self.index.goto_contact().del_contact(username)
        assert result

