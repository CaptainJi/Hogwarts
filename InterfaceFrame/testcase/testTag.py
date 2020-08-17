from api.util import Util
from api.wework import WeWork


class TestTag:
    def test_get_token(self):
        Util().get_token()

    def test_add_tag(self):
        assert 'created' == WeWork().add_tag('嘿嘿', '2')['errmsg']

    def test_update_tag(self):
        assert 'updated' == WeWork().update_tag('哈哈', '2')['errmsg']

    def test_get_tag(self):
        assert 'ok' == WeWork().get_tag('2')['errmsg']

    def test_remove_tag(self):
        assert 'deleted' == WeWork().remove_tag('2')['errmsg']
