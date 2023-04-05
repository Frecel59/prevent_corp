# importation :
import numpy as np
import pandas as pd
from sklearn.model_selection import TimeSeriesSplit

from rnn_logic.cleaning import clean_characteristics_data


def load_data_for_time_serie():
    '''
    Load the data from our bucket to the current local
    '''
    # if not  data.csv exist :
    #     telecharge data
    # data = pd.read_csv("path/todata.csv")

    pass



def prepare_data_for_model():
    print("\nPreparing data for the model -> ...")

    data= clean_characteristics_data()
    data = data.drop(['lum', 'agg', 'atm', 'int', 'col', "jour"], axis=1)
    year_mapping = {5: 2005, 6: 2006, 7: 2007, 8: 2008, 9: 2009,
    10: 2010, 11: 2011, 12: 2012, 13: 2013, 14: 2014,
    15: 2015, 16: 2016, 17: 2017, 18: 2018, 19: 2019,
    20: 2020, 21: 2021}

    data['an'] = data['an'].replace(year_mapping)
    data['date'] = pd.to_datetime(data['an'].astype(str) + '-' + data['mois'].astype(str) + '-' + "1")
    data.drop(['mois', 'an'], axis=1, inplace=True)
    data['date'] = pd.to_datetime(data['date'])
    data['year_month'] = data['date'].dt.to_period('M')
    data = pd.pivot_table(data, values='Num_Acc', index='date', columns='dep', aggfunc='count')
    for i in range(1,95):
        if i == 20:
            continue
        if data[i].isna().sum()> 0:
            data[i]=data[i].fillna(data[i].mean())

    data.loc['2020-03-01'] = data.loc[['2019-03-01', '2018-03-01', '2017-03-01']].mean()
    data.loc['2020-04-01'] = data.loc[['2019-04-01', '2018-04-01', '2017-04-01']].mean()
    data.loc['2020-05-01'] = data.loc[['2019-05-01', '2018-05-01', '2017-05-01']].mean()

    data.loc['2020-10-01'] = data.loc[['2019-10-01', '2018-10-01', '2017-10-01']].mean()
    data.loc['2020-11-01'] = data.loc[['2019-11-01', '2018-11-01', '2017-11-01']].mean()
    data.loc['2020-12-01'] = data.loc[['2019-12-01', '2018-12-01', '2017-12-01']].mean()

    data.loc['2021-04-01'] = data.loc[['2020-04-01', '2019-04-01', '2018-04-01']].mean()
    data.loc['2021-05-01'] = data.loc[['2020-05-01', '2019-05-01', '2018-05-01']].mean()

    print("Preparing data for the model -> Done")
    data.to_pickle(f"data/clean_data/Charatesitiques_final.pkl")

    return data

def create_split(data, split_value):
    print("Creating train test split -> ...")
    # Calculer le nombre de lignes à inclure dans l'ensemble d'entraînement
    train_size = int(len(data) * split_value)

    # Diviser le dataframe en ensembles d'entraînement et de test en utilisant iloc
    train_data = data.iloc[:train_size,:]
    test_data = data.iloc[train_size:,:]
    print("Creating train test split -> Done")
    return train_data, test_data

def create_sequences(name: str, data : pd.DataFrame, dep: int, sequence_length: int):
    """
    Découpe les données en séquences de taille spécifiée avec un décalage d'un mois à chaque fois.

    :param data: DataFrame contenant les données à découper en séquences
    :param sequence_length: Longueur des séquences
    :return: Numpy array contenant les séquences
    """
    print(f"Creating {name} sequences -> ...")
    data = data[[dep]]
    sequences = []
    for i in range(len(data) - sequence_length):
        sequence = data.iloc[i:i + sequence_length].values
        sequences.append(sequence)
    print(f"Creating {name} sequences  -> Done")
    return np.array(sequences)

def create_baseline(data, dep):
    """
    Calcule la moyenne des valeurs pour chaque mois sur l'ensemble de la période disponible.
    :param df: DataFrame contenant les données
    :return: DataFrame contenant la moyenne des valeurs pour chaque mois
    """
    data = data[[dep]]
    baseline = data.groupby(data.index.month).mean()
    return baseline

def full_preprocessing():
    dep = int(input("Numéro de Département : "))
    sequence_size = int(input("Taille de la séquence : "))
    print("Début du Data Cleaning :")
    data = clean_characteristics_data()
    print("Data Cleaning Terminé !")
    print("Début du precrocessing :")
    data = prepare_data_for_model(data)
    train_data, test_data = create_split(data, 0.7)
    train_sequence = create_sequences("train", train_data, dep, sequence_size)
    test_sequence = create_sequences("test", test_data, dep, sequence_size)
    print("Preprocessing Terminé !")

    return train_sequence, test_sequence

def create_fold(data: pd.DataFrame, n_fold:int):
    '''
    CUT n_fold for the cross validation
    '''
    tscv = TimeSeriesSplit(n_splits=n_fold, test_size=12)
    folds = []

    for train_index, test_index in tscv.split(data):
        folds.append((train_index, test_index))

    return folds

if __name__ == "__main__":
    data = prepare_data_for_model()
    print(data.shape)
