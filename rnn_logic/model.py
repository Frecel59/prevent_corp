
import os
import time
import pickle
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX, SARIMAXResults
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error

from google.cloud import storage

class SarimaModel():
    '''
    Structure for the Arima Model
    '''
    def __init__(self,dep, params=None):
        self.dep = dep
        self.model_path = os.path.join("training_outputs", "models", f"{self.dep}.pkl")
        self.bucket_name = os.environ.get('BUCKET_NAME')

        if not params:
            self.load_model()
        else:
            self.order= params[dep]['order']
            self.seasonal_order = params[dep]['seasonal_order']


    def fit(self,X_train):
        print(" Fittig the model -> ...")
        self.model = SARIMAX(X_train,
                            order=self.order,
                            seasonal_order=self.seasonal_order,
                            initialization='approximate_diffuse')
        self.model = self.model.fit(disp=False)
        print("✅ Fittig the model -> Done")

    def predict(self, step:int = 12):
        print(" Prediction -> ...")
        self.predictions = self.model.forecast(step)
        print("✅ Prediction -> Done")
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

        if target == 'gcp':

            storage_client = storage.Client.from_service_account_json("service_account.json")

            bucket = storage_client.get_bucket(self.bucket_name)

            remote_path = self.model_path

            blob = bucket.blob(remote_path)
            blob.upload_from_filename(self.model_path)

            print(f"✅ Model saved to GCP at gs://{self.bucket_name}/{remote_path}")

    def load_model(self):
        if not os.path.isdir('training_outputs'):
            os.mkdir('training_outputs')
        if not os.path.isdir('training_outputs/models'):
            os.mkdir('training_outputs/models')
        if not os.path.isfile(self.model_path):

            storage_client = storage.Client.from_service_account_json("service_account.json")

            bucket = storage_client.get_bucket(self.bucket_name)

            remote_path = self.model_path

            blob = bucket.blob(remote_path)
            if blob.exists():

                blob.download_to_filename(self.model_path)
                print(f"✅ Model loaded from GCP at gs://{self.bucket_name}/{remote_path}")
            else:
                print("❌ Model not found on local or GCP")
                return

        # Load the model
        self.model = SARIMAXResults.load(self.model_path)


    def save_result(self,target="local"):
        '''
        Save the result on Big query or local
        '''
        if self.metrics is not None:
            metrics_path = os.path.join("training_outputs", "metrics", f"{self.dep}.pickle")
            with open(metrics_path, "wb") as file:
                pickle.dump(self.metrics, file)

        print("✅ Results saved locally")
