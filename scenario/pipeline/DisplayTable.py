from sklearn.base import TransformerMixin, BaseEstimator

from scenario import Scenario


class DisplayTable(BaseEstimator, TransformerMixin):

    def __init__(self, table_name):
        self.table_name = table_name

    def transform(self, scenario, y=None):
        pd = scenario.getAsDataFrame(self.table_name)
        print("Scenario: " + scenario.name + " " + self.table_name)
        print(pd.head())
        return scenario

    def fit(self, *_):
        return self