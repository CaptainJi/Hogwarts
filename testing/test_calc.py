import pytest
import yaml

from pythoncode.caic import Calculator


class TestCalc():
    cal = Calculator()

    @pytest.mark.parametrize(('a', 'b'), yaml.safe_load(open('data.yaml')))
    def test_add(self, a, b):
        self.cal = Calculator()
        result = a + b
        assert result == self.cal.add(a, b)

    @pytest.mark.parametrize(('a', 'b'), yaml.safe_load(open('data.yaml')))
    def test_min(self, a, b):
        result = a - b
        assert result == self.cal.min(a, b)

    @pytest.mark.parametrize(('a', 'b'), yaml.safe_load(open('data.yaml')))
    def test_mul(self, a, b):
        result = a * b
        assert result == self.cal.mul(a, b)

    @pytest.mark.parametrize(('a', 'b'), yaml.safe_load(open('data.yaml')))
    def test_div(self, a, b):
        result = a / b
        assert result == self.cal.div(a, b)
