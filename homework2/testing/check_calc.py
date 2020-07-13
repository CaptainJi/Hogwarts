import pytest
import yaml
import sys

sys.path.append('..')
from pythoncode.caic import Calculator


# 定义测试类
class TestCalc():
    cal = Calculator()

    # 参数化用例
    # @pytest.mark.parametrize('a', yaml.safe_load(open('data.yaml')), ids=['整数', '负数', '零', '浮点数', '大整数',
    #                                                                       '字符'])
    # @pytest.mark.parametrize('b', yaml.safe_load(open('data.yaml')), ids=['整数', '负数', '零', '浮点数', '大整数',
    #                                                                       '字符'])

    @pytest.mark.dependency(name='test_add')
    @pytest.mark.run(order=0)
    # 加法测试用例
    def test_add(self, cmdoption):
        # 获取yaml字典中相应的key值
        _, datas = cmdoption
        print(datas)
        a = datas['data'][0]
        b = datas['data'][1]
        # 尝试捕获异常
        try:
            result = a + b
            print(f'\na:{a}')
            print(f'\nb:{b}')
            print(f'\n运算结果={result}')
        # 如果与计算器程序中捕获的异常一致则认为测试通过，否则测试不通过
        except Exception as msg:
            print(f'\n用例反馈异常内容："{msg}"')
            err_msg = self.cal.add(a, b)
            print(f'\n程序反馈异常内容："{err_msg}"')
            if str(msg) == str(err_msg):
                print(f'异常检测成功')
                assert True
            else:
                print(f'异常检测失败')
                assert False
        else:
            assert result == self.cal.add(a, b)

    # 减法测试用例
    @pytest.mark.parametrize('a', yaml.safe_load(open('data.yaml')), ids=['整数', '负数', '零', '浮点数', '大整数',
                                                                          '字符'])
    @pytest.mark.parametrize('b', yaml.safe_load(open('data.yaml')), ids=['整数', '负数', '零', '浮点数', '大整数',
                                                                          '字符'])
    @pytest.mark.dependency(depends=['test_add'])
    @pytest.mark.run(order=1)
    def check_sub(self, a, b):
        a = a['a']
        b = b['b']
        try:
            result = a - b
            print(f'\na:{a}')
            print(f'\nb:{b}')
            print(f'\n运算结果={result}')
        except Exception as msg:
            print(f'\n用例反馈异常内容："{msg}"')
            err_msg = self.cal.sub(a, b)
            print(f'\n程序反馈异常内容："{err_msg}"')
            if str(msg) == str(err_msg):
                print(f'异常检测成功')
                assert True
            else:
                print(f'异常检测失败')
                assert False
        else:
            assert result == self.cal.sub(a, b)

    # 乘法测试用例

    @pytest.mark.parametrize('a', yaml.safe_load(open('data.yaml')), ids=['整数', '负数', '零', '浮点数', '大整数',
                                                                          '字符'])
    @pytest.mark.parametrize('b', yaml.safe_load(open('data.yaml')), ids=['整数', '负数', '零', '浮点数', '大整数',
                                                                          '字符'])
    @pytest.mark.dependency(name='check_mul')
    @pytest.mark.run(order=2)
    def check_mul(self, a, b):
        a = a['a']
        b = b['b']
        try:
            result = a * b
            print(f'\na:{a}')
            print(f'\nb:{b}')
            print(f'\n运算结果={result}')
        except Exception as msg:
            print(f'\n用例反馈异常内容："{msg}"')
            err_msg = self.cal.mul(a, b)
            print(f'\n程序反馈异常内容："{err_msg}"')
            if str(msg) == str(err_msg):
                print(f'异常检测成功')
                assert True
            else:
                print(f'异常检测失败')
                assert False
        else:
            assert result == self.cal.mul(a, b)

    # 除法测试用例
    @pytest.mark.parametrize('a', yaml.safe_load(open('data.yaml')), ids=['整数', '负数', '零', '浮点数', '大整数',
                                                                          '字符'])
    @pytest.mark.parametrize('b', yaml.safe_load(open('data.yaml')), ids=['整数', '负数', '零', '浮点数', '大整数',
                                                                          '字符'])
    @pytest.mark.dependency(depends=['check_mul'])
    @pytest.mark.run(order=3)
    def check_div(self, a, b):
        a = a['a']
        b = b['b']
        try:
            result = a / b
            print(f'\na:{a}')
            print(f'\nb:{b}')
            print(f'\n运算结果={result}')
        except Exception as msg:
            print(f'\n用例反馈异常内容："{msg}"')
            err_msg = self.cal.div(a, b)
            print(f'\n程序反馈异常内容："{err_msg}"')
            if str(msg) == str(err_msg):
                print(f'异常检测成功')
                assert True
            else:
                print(f'异常检测失败')
                assert False
        else:
            assert result == self.cal.div(a, b)
