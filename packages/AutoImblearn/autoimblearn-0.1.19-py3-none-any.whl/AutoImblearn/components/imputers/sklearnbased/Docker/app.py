from AutoImblearn.components.api import BaseTransformerAPI

from sklearn.impute import IterativeImputer
from sklearn.impute import KNNImputer
import logging
import numpy as np


imps = {
    'ii': IterativeImputer,
    'knn': KNNImputer,

}

class RunSklearnImputerAPI(BaseTransformerAPI):
    def __init__(self):
        super().__init__(__name__)

    def get_hyperparameter_search_space(self):
        return {
        }

    def apply_rounding(self, categorical_columns):
        # self.category_columns = [i for i in self.category_columns if i in self.data.columns.values]
        for column in categorical_columns:
            self.data[column] = self.data[column].round(0)

    def fit(self, params, *args, **kwargs):
        categorical_columns = params['categorical_columns']

        impute = KNNImputer(weights='distance', n_neighbors=1)
        self.data[:] = impute.fit_transform(self.data)
        # self.apply_rounding(categorical_columns)

        result = None
        if 'data' in kwargs:
            pass
        else:
            pass

        logging.info("finished parameter setting")

        return

    def transform(self, X_test, y_test=None):

        return X_test

RunSklearnImputerAPI().run()