from sklearn.base import TransformerMixin, BaseEstimator

from scenario import Scenario

class GetScenarioByName(BaseEstimator, TransformerMixin):

#    def transform(self, scenario_names, y=None):
#        try:
#            scenarios = []
#            for scenario_name in scenario_names:
#                scenarios.append(Scenario.Scenario(scenario_name))
#            return scenarios
#        except TypeError:
#            return Scenario.Scenario(scenario_names)

    def transform(self, scenario_name, y=None):
        return Scenario(scenario_name)

    def fit(self, *_):
        return self