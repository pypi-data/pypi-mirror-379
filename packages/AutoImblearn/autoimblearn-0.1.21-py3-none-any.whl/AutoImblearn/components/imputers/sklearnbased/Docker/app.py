from AutoImblearn.components.api import BaseTransformerAPI

from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import KNNImputer
import logging
import numpy as np


imps = {
    "ii": lambda **kw: IterativeImputer(**{**{"max_iter": 10}, **kw}),
    "knn": lambda **kw: KNNImputer(**{**{"weights": 'distance', "n_neighbors": 1}, **kw}),
}

class RunSklearnImputerAPI(BaseTransformerAPI):
    def __init__(self):
        self.result = None
        super().__init__(__name__)

    def get_hyperparameter_search_space(self):
        return {
        }

    def apply_rounding(self, categorical_columns):
        # self.category_columns = [i for i in self.category_columns if i in self.data.columns.values]
        for column in categorical_columns:
            self.data[column] = self.data[column].round(0)

    def fit(self, params, *args, **kwargs):
        model = params.model
        imputer_kwargs = params.imputer_kwargs
        categorical_columns = params.categorical_columns

        if 'data' in kwargs:
            data = kwargs.get('data')
        else:
            raise ValueError("There is no data passed in")

        factory = imps[model]
        impl = factory(**imputer_kwargs)
        self.result = impl.fit_transform(data)
        # self.apply_rounding(categorical_columns)

        logging.info("finished training")
        return

    def transform(self, *args, **kwargs):
        return self.result

RunSklearnImputerAPI().run()