from cloudant.client import Cloudant
from cloudant.document import Document
import pandas as pd

class Scenario:

    def __init__(self, name):
        self.name = name
        self.client = Cloudant("saxo", "saxo-rest", url="https://saxo.cloudant.com", connect=True)
        #session = client.session()
        self.db = self.client['scenarios']

    def __str__(self):
        return self.name

    @staticmethod
    def getInvokingScenario():
        return Scenario("Scenario1")

    def getAsDataFrame(self, table):
        id = self.name+"_"+table
        data = self.db[id]
        return pd.read_json(data['value'])

    def put(self, table, pd):
        id = self.name+"_"+table
        if (Document(self.db, id).exists()):
            data = self.db[id]
            data['value'] = pd.to_json()
            data.save()
        else:
            data = {
            '_id': id,
            'value': pd.to_json()
            }
            self.db.create_document(data)
