import os
import pandas as pd

def lieux_clean_data_05_18():
    """
    Importation des datasets de 2012 à 2018
    """
    print("Cleaning Lieux de 2005 à 2018 ...")
    directory = "data/raw_data/lieux/1"
    files = [file for file in os.listdir(directory) if file.startswith("lieux_") and file.endswith(".csv")]
    data = pd.DataFrame()
    for file in files:
        df = pd.read_csv(os.path.join(directory, file), sep=',', encoding='ISO-8859-1', engine='python')
        data = pd.concat([data, df], ignore_index=True)
    data = data.drop(columns=['voie','v1','v2', 'pr', 'pr1', 'lartpc', 'larrout', 'env1'])
    data.dropna(inplace=True)
    data = data.astype(int)
    print("Cleaning Lieux de 2005 à 2018 -> Done")
    return data

def lieux_clean_data_19_21():
    """
    Importation des datasets de 2019 à 2021
    """
    print("Cleaning Lieux de 2019 à 2021 ...")
    directory = "data/raw_data/lieux/2"
    files = [file for file in os.listdir(directory) if file.startswith("lieux_") and file.endswith(".csv")]
    data = pd.DataFrame()
    for file in files:
        df = pd.read_csv(os.path.join(directory, file), sep=';', encoding='ISO-8859-1', engine='python')
        data = pd.concat([data, df], ignore_index=True)
    data = data.drop(columns=['voie','v1','v2', 'pr', 'pr1', 'lartpc', 'vma', 'larrout'])
    print("Cleaning Lieux de 2019 à 2021 -> Done")
    return data
