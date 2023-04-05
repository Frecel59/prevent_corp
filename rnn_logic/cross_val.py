import numpy as np
import pandas as pd
from tqdm import tqdm
import pickle

from rnn_logic.model import SarimaModel
from rnn_logic.preprocessing import create_fold
from rnn_logic.data import import_clean_data


def cross_val(data: pd.DataFrame, n_fold: int, dep: int, params: dict):


    # After the cross val
    # retrain on the whole dataset (exept last year for the demo)
    folds = create_fold(data, n_fold)
    model = SarimaModel(dep, params)
    mse_list = []
    rmse_list = []
    mape_list = []
    for train_index, test_index in folds:
        X_train, X_test = data.iloc[train_index], data.iloc[test_index]
        model.fit(X_train[dep])
        model.evaluate(X_test[dep])
        mse, rmse, mape = model.metrics
        mse_list.append(mse)
        rmse_list.append(rmse)
        mape_list.append(mape)

    model.fit(data[dep])

    mean_mse = np.mean(mse_list)
    mean_rmse = np.mean(rmse_list)
    mean_mape = np.mean(mape_list)

    results = {
        'mse_list': mse_list,
        'rmse_list': rmse_list,
        'mape_list': mape_list,
        'mean_mse': mean_mse,
        'mean_rmse': mean_rmse,
        'mean_mape': mean_mape
    }
    model.save_model(target="gcp")
    #model.save_results
    return results

def import_json():
    with open('best_params.pickle', 'rb') as handle:
        best_params = pickle.load(handle)
        return best_params

if __name__=="__main__":
    params = import_json()
    data = import_clean_data()
    for dep in tqdm(params.keys()):
        cross_val(data, 8, dep,params)
