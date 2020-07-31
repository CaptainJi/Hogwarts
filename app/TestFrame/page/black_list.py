from appium.webdriver.common.mobileby import MobileBy

black_list = [(MobileBy.XPATH, '//*[contains(@text,"跳过")]')]
max_error_num = 2
error_num = 0


def black_handle(fun):
    def find_black(*args, **kwargs):
        print('装饰器调用')
        try:
            print('尝试执行装饰器内方法')
            fun(*args, **kwargs)
        except Exception as f:
            raise f

    return find_black
