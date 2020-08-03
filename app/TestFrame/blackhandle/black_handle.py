import logging.config

import allure
from appium.webdriver.common.mobileby import MobileBy


def black_handle(fun):
    '''
    自定义装饰器
    :return:
    '''

    def wrapper(*args, **kwargs):
        '''
        装饰器功能
        :param args: 解元组
        :param kwargs: 解字典
        :return: wrapper自身
        '''
        # 定义黑名单
        _black_list = [(MobileBy.XPATH, '//*[contains(@text,"跳过")]'),
                       (MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/ib_close"]')]
        # 最大查找次数
        _max_error_num = 3
        # 当前查找次数
        _error_num = 0
        from basepage.basePage import BasePage
        # 装饰器特性：传入的第0个参数为self，所以可以使用以下方法获取self参数
        instance: BasePage = args[0]

        try:
            # 尝试执行fun
            element = fun(*args, **kwargs)
            # 如果fun执行成功error则清零
            _error_num = 0
            instance.set_implicitly_wait(3)
            return element

        except Exception as f:
            # 加入异常截图
            instance.screenshot('../tmp/tmp.png')
            with open('../tmp/tmp.png', 'rb') as f:
                content = f.read()
            # 截图添加入allure中
            allure.attach(content, attachment_type=allure.attachment_type.PNG)
            logging.error('元素未找到,开始处理黑名单流程')
            instance.set_implicitly_wait(1)
            # 出现异常时判断计数器是否超过上限
            if _error_num > _max_error_num:
                # 如果erro次数大于max_rror,清空erro次数并报异常
                _error_num = 0
                raise f
            _error_num += 1
            # 遍历黑名单,并点击关闭或跳过按钮来跳过弹窗
            for ele in _black_list:
                eles = instance.finds(ele)
                if len(eles) > 0:
                    logging.info(f'找到黑名单元素{ele}')
                    # 点击黑名单元素
                    logging.info(f'开始处理黑名单元素{ele}')
                    eles[0].click()
                    # 返回自身,再次执行操作
                    return wrapper(*args, **kwargs)
            raise ValueError('无黑名单中的元素')

    return wrapper
