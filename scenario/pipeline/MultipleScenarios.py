from sklearn.base import TransformerMixin, BaseEstimator


class MultipleScenarios(BaseEstimator, TransformerMixin):

    def __init__(self, transformer_list):
        self.transformer_list = transformer_list

    def transform(self, scenario_names, y=None):
        #Parallel(n_jobs=self.n_jobs)(
         #   delayed(_fit_one_transformer)(trans, scenario_names, y)
         #   for _, trans, _ in self._iter())
        for scenario_name in scenario_names:
            for trans in self.transformer_list:
                trans.transform(scenario_name)
        return scenario_names

    def fit(self, *_):
        return self