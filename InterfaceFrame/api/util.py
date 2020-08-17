import requests


class Util:
    def get_token(self):
        '''
        获取token
        https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET
        :return:
        '''
        request_params = {
            'corpid': 'ww9405441d4069fef0',
            'corpsecret': 'KJpNThutK68Cew8rjXibjxF1PbooeTIOHO38G1nLg9E'
        }
        r = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken', params=request_params)
        return r.json()['access_token']
