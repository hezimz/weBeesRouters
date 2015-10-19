import json
import os.path


class ParamsLoader(object):

    def __init__(self):
        self.json_file = os.path.dirname(__file__)+"/"+'params.json'
        self.params = self.load_json()
        self.routers_params = self.params["routers"]
        self.db_params = self.params["db"]
        self.local_file_location = self.params["localUserInfo"]["location"]
        self.local_file_name = self.params["localUserInfo"]["fileName"]

    def load_json(self):
        # return a dictionary with json data loaded
        json_data = open(self.json_file).read()
        return json.loads(json_data)


