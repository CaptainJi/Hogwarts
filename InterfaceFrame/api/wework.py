import json

import requests
import yaml

from api.baseAPI import BaseAPI
from api.util import Util


class WeWork(BaseAPI):
    def __init__(self):
        self.token = Util().get_token()
        self.params['token'] = self.token

    def add_tag(self, tagname, tagid):
        '''
        添加标签
        https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token=ACCESS_TOKEN
        :return:
        '''
        self.params['tagname'] = tagname
        self.params['tagid'] = tagid
        with open('../data/tagData.yml', encoding='utf-8') as f:
            data = yaml.load(f)
        return self.send(data['add'])

    def remove_tag(self, tagid):
        '''
        删除标签
        https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token=ACCESS_TOKEN&tagid=TAGID
        :return:
        '''
        self.params['tagid'] = tagid
        with open('../data/tagData.yml', encoding='utf-8') as f:
            data = yaml.load(f)
        return self.send(data['remove'])

    def update_tag(self, tagname, tagid):
        '''
        更改标签
        https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token=ACCESS_TOKEN
        :return:
        '''
        self.params['tagname'] = tagname
        self.params['tagid'] = tagid
        with open('../data/tagData.yml', encoding='utf-8') as f:
            data = yaml.load(f)
        return self.send(data['update'])

    def get_tag(self, tagid):
        '''
        获取标签
        https://qyapi.weixin.qq.com/cgi-bin/tag/get?access_token=ACCESS_TOKEN&tagid=TAGID
        :return:
        '''
        self.params['tagid'] = tagid
        with open('../data/tagData.yml', encoding='utf-8') as f:
            data = yaml.load(f)
        return self.send(data['get'])
