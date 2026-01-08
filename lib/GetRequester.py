import urllib.request
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        with urllib.request.urlopen(self.url) as response:
            return response.read()

    def load_json(self):
        return json.loads(self.get_response_body())