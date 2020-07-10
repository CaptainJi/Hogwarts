import pytest
import yaml
import sys

sys.path.append('..')
from pythoncode.caic import Calculator


class TestCalc():
    cal = Calculator()

    @pytest.mark.parametrize('a', yaml.safe_load(open('data.yaml')), ids=['int', 'minus', 'zero', 'float', 'bit_int',
                                                                          'str'])
    @pytest.mark.parametrize('b', yaml.safe_load(open('data.yaml')), ids=['int', 'minus', 'zero', 'float', 'bit_int',
                                                                          'str'])
    def test_add(self, a, b):
        result = a + b
        print(result)
        assert result == self.cal.add(a, b)

    @pytest.mark.parametrize('a', yaml.safe_load(open('data.yaml')), ids=['int', 'minus', 'zero', 'float', 'bit_int',
                                                                          'str'])
    @pytest.mark.parametrize('b', yaml.safe_load(open('data.yaml')), ids=['int', 'minus', 'zero', 'float', 'bit_int',
                                                                          'str'])
    def test_sub(self, a, b):
        result = a - b
        print(result)
        assert result == self.cal.sub(a, b)

    @pytest.mark.parametrize('a', yaml.safe_load(open('data.yaml')), ids=['int', 'minus', 'zero', 'float', 'bit_int',
                                                                          'str'])
    @pytest.mark.parametrize('b', yaml.safe_load(open('data.yaml')), ids=['int', 'minus', 'zero', 'float', 'bit_int',
                                                                          'str'])
    def test_mul(self, a, b):
        result = a * b
        print(result)
        assert result == self.cal.mul(a, b)

    @pytest.mark.parametrize('a', yaml.safe_load(open('data.yaml')), ids=['int', 'minus', 'zero', 'float', 'bit_int',
                                                                          'str'])
    @pytest.mark.parametrize('b', yaml.safe_load(open('data.yaml')), ids=['int', 'minus', 'zero', 'float', 'bit_int',
                                                                          'str'])
    def test_div(self, a, b):
        result = a / b
        print(result)
        assert result == self.cal.div(a, b)
