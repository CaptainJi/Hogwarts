import pytest
import yaml

from page.app import App


class TestMarket:
    data = App().load_data('../data/search_datas.yml')

    def setup(self):
        self.app = App()

    @pytest.mark.parametrize('stock_name', data)
    def test_market(self, stock_name):
        search = self.app.start().goto_main().goto_market('行情').goto_search()
        search.search(stock_name)
