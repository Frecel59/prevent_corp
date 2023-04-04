
import os
import time
import pickle
import numpy as np
from statsmodels.tsa.arima.model import ARIMA, ARIMAResults
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error

class ArimaModel():
    '''
    Structure for the Arima Model
    '''
    def __init__(self,dep):
        self.dep = dep
        self.model_path = os.path.join("training_outputs", "models", f"{self.dep}.pkl")


    def fit(self,X_train):
        self.model = ARIMA(X_train)
        self.model = self.model.fit()

    def predict(self, step:int = 12):
        self.predictions = self.model.forecast(step)
        return self.predictions

    def evaluate(self,y_test):
        self.mse = mean_squared_error(y_test, self.predict(step=len(y_test)))
        self.rmse = np.sqrt(self.mse)
        self.mape = mean_absolute_percentage_error(y_test, self.predict(step=len(y_test)))
        self.metrics = [self.mse, self.rmse, self.mape]

    def save_model(self,target="local"):
        '''
        Save the model on GCP or local
        '''
            # save model locally
        self.model.save(self.model_path)
        print("✅ Model saved locally")

    def load_model(self,target='local'):
        self.model = ARIMAResults.load(self.model_path)
        pass


    def save_result(self,target="local"):
        '''
        Save the result on Big query or local
        '''
        if self.metrics is not None:
            metrics_path = os.path.join("training_outputs", "metrics", f"{self.dep}.pickle")
            with open(metrics_path, "wb") as file:
                pickle.dump(self.metrics, file)

        print("✅ Results saved locally")
