from test_workwx.index import Index


class TestAddMember():
    def setup(self):
        self.index = Index()

    def test_add_member(self):
        result = self.index.goto_add_member().add_member()
        assert result
