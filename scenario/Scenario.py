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

    def duplicate(self, name):
        newsc = Scenario(name)
        for table in self.getTables():
            newsc.put(table, self.getAsDataFrame(table))
        return newsc

    def getTables(self):
        tables = []
        for document in self.db:
            if document._document_id.startswith(self.name):
                a = len(self.name)+1
                b = len(document._document_id)
                tables.append(document._document_id[a: b])
        return tables

    @staticmethod
    def getInvokingScenario():
        return Scenario("Scenario1")

    def getAsDataFrame(self, table):
        id = self.name+"_"+table
        data = self.db[id]
        return pd.read_json(data['value'])

    def put(self, table, what):
        if isinstance(what, pd.DataFrame):
            id = self.name+"_"+table
            if (Document(self.db, id).exists()):
                data = self.db[id]
                data['value'] = what.to_json()
                data.save()
            else:
                data = {
                '_id': id,
                'value': what.to_json()
                }
                self.db.create_document(data)
