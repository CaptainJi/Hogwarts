from test_workwx.index import Index


class TestRegister:
    def setup(self):
        self.index = Index()

    def test_register(self):
        result = self.index.goto_register().register()
        assert result
