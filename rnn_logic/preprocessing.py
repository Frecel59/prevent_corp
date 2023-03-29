# importation :
import numpy as np
import pandas as pd

from rnn_logic.cleaning import clean_all_data

def prepare_data_for_model(data:pd.DataFrame):
    print("Preparing data for the model -> ...")
    data.an = data.an.map({11:11,
                           12:12,
                           13:13,
                           14:14,
                           15:15,
                           16:16,
                           17:17,
                           18:18,
                           2019:19,
                           2020:20,
                           2021:21})
    data['date'] = pd.to_datetime(data['an']*10000 + data['mois']*100 + 1, format='%y%m%d')
    data = data.drop(columns=['an', 'mois', 'lum', 'agg', 'int', 'atm', 'col'])
    data = pd.pivot_table(data, values='Num_Acc', index='date', columns='dep', aggfunc='count')
    print(data.shape)
    for i in range(95):
        if data[i+1].isna().sum()> 0:
            data[i+1]=data[i+1].fillna(data[i+1].mean())
    data = data.astype(int)
    print("Preparing data for the model -> Done")

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

def create_sequences(data : pd.DataFrame, dep: int, sequence_length: int):
    """
    Découpe les données en séquences de taille spécifiée avec un décalage d'un mois à chaque fois.

    :param data: DataFrame contenant les données à découper en séquences
    :param sequence_length: Longueur des séquences
    :return: Numpy array contenant les séquences
    """
    print("Creating sequences -> ...")
    data = data[[dep]]
    sequences = []
    for i in range(len(data) - sequence_length):
        sequence = data.iloc[i:i + sequence_length].values
        sequences.append(sequence)
    print("Creating sequences -> Done")
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

if __name__ == "__main__":
    data_char, data_lieux, data_usagers, data_vehiules = clean_all_data()
    data_char = prepare_data_for_model(data_char)
    print(data_char.shape)
    train_data, test_data = create_split(data_char, 0.7)
    print(train_data.shape)
    sequence = create_sequences(train_data, 75, 12)
    print(sequence.shape)
    baseline = create_baseline(train_data, 75)
