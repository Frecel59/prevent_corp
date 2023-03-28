import pandas as pd
import os


def vehicules_clean_data_12_18():
    print("Cleaning Véhicules de 2012 à 2018 -> ...")
    directory = "data/raw_data/vehicules/1"
    files = [file for file in os.listdir(directory) if file.startswith("vehicules_") and file.endswith(".csv")]
    data = pd.DataFrame()
    for file in files:
        df = pd.read_csv(os.path.join(directory, file), sep=',', encoding='ISO-8859-1', engine='python')
        data = pd.concat([data, df], ignore_index=True)

    data.dropna(inplace=True)
    data= data.astype({'obs':int, 'obsm':int, 'choc':int, 'manv':int})
    print("Cleaning Véhicules de 2012 à 2018 -> Done")
    return data


def vehicules_clean_data_19_21():
    print("Cleaning Véhicules de 2019 à 2021 -> ...")
    directory = "data/raw_data/vehicules/2"

    files = [file for file in os.listdir(directory) if file.startswith("vehicules_") and file.endswith(".csv")]
    data = pd.DataFrame()
    for file in files:
        df = pd.read_csv(os.path.join(directory, file), sep=';', encoding='ISO-8859-1', engine='python')
        data = pd.concat([data, df], ignore_index=True)
    print("Cleaning Véhicules de 2019 à 2021 -> Done")

    return data
