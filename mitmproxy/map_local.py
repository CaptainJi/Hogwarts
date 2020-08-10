import json
from mitmproxy import http


def response(flow: http.HTTPFlow):
    # 设置判断条件:如果url中包含"quote.json"
    if "quote.json" in flow.request.pretty_url:
        # 读取本地json文件
        with open('quote.json', encoding='utf-8') as f:
            data = json.load(f)
            # 将读取的的json文件赋值给response
        flow.response.text = json.dumps(data)

        # # 读取在线获取的json并修改内容赋值给response返回
        # data = json.loads(flow.response.content)
        # data['data']['items'][0]['quote']['name'] = data['data']['items'][0]['quote']['name'] + "周杰偷"
        # flow.response.text = json.dumps(data)
