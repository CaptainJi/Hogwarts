from page.app import App


class TestMarket:
    def setup(self):
        self.app = App()

    def test_market(self):
        self.app.start().goto_main().goto_market().goto_search().search()
