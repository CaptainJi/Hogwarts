import pytest


class TextContact():
    def setup(self):
        self.index = Index()

    def test_contact(self):
        result = self.index.goto_contact()
        assert result

if __name__ == '__main__':
    pytest.main()
