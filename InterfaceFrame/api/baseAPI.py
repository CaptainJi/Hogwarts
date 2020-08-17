import json

import requests


class BaseAPI:
    params = {}

    def send(self, data):
        raw_data = json.dumps(data)
        for key, value in self.params.items():
            raw_data = raw_data.replace('${' + key + '}', value)
        data = json.loads(raw_data)
        return requests.request(**data).json()
