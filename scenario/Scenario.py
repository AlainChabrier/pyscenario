import json
import pandas as pd
import numpy as np

class Scenario:
    def __init__(self, name):
        self.name = name


    def __str__(self):
        return self.name

    @staticmethod
    def getInvokingScenario():
        return Scenario("Current Scenario")

    def getAsDataFrame(self, table):
        if (table == "gas"):
            gas_names = ["super", "regular", "diesel"]
            gas_data = np.array([[3000, 70, 10, 1], [2000, 60, 8, 2], [1000, 50, 6, 1]])
            nb_gas  = len(gas_names)
            range_gas = range(nb_gas)
            gaspd = pd.DataFrame([(gas_names[i],int(gas_data[i][0]),int(gas_data[i][1]),int(gas_data[i][2]),int(gas_data[i][3]))
                      for i in range_gas],
                                 index =range_gas )
            gaspd.columns = ['name','demand','price','octane','lead']
            return gaspd
        if (table == "oil"):
            oil_names = ["crude1", "crude2", "crude3"]
            oil_data = np.array([[5000, 45, 12, 0.5], [5000, 35, 6, 2], [5000, 25, 8, 3]])
            nb_oils = len(oil_names)
            range_oil = range(nb_oils)
            oilpd = pd.DataFrame([(oil_names[i],int(oil_data[i][0]),int(oil_data[i][1]),int(oil_data[i][2]),oil_data[i][3])
                      for i in range_oil])
            oilpd.columns= ['name','capacity','price','octane','lead']
            return oilpd

