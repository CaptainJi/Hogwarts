# 计算器
class Calculator:
    # 加法
    def add(self, a, b):
        try:
            res = a + b
        except Exception as msg:
            return msg
        else:
            return res

    # 减法
    def sub(self, a, b):
        try:
            res = a - b
        except Exception as msg:
            return msg
        else:
            return res

    # 乘法
    def mul(self, a, b):
        try:
            res = a * b
        except Exception as msg:

            return msg
        else:
            return res

    # 除法
    def div(self, a, b):
        try:
            res = a / b
        except Exception as msg:
            return msg
        else:
            return res


if __name__ == '__main__':
    a = 1
    b = 'a'
    cal = Calculator()
    res = cal.add(a, b)
    # res = res.strip('\n')
    if str(res) == "unsupported operand type(s) for +: 'int' and 'str'":
        print('True')
    else:
        print('False')
