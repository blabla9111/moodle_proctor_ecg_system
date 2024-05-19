import json
import urllib.parse


class RequestParserJson():
    def __init__(self, request, json_start_flag=False) -> None:
        self.body = request.body
        decoded_string = urllib.parse.unquote(self.body)
        if json_start_flag:
            decoded_string = decoded_string.replace('json=', '')
        self.js = json.loads(decoded_string)

    def get_json(self):
        return self.js

    def get_user_id(self):
        return self.js['user_id']

    def get_quiz_id(self):
        return self.js['quiz_id']

    def get_code(self):
        return self.js['code']

    def get_transaction_id(self):
        return self.js['id_transaction']

    def get_ecg_data(self):
        return self.js['ecg_data']

