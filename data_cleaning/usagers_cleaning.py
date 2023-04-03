import os
import pandas as pd


def usagers_clean_data_05_18():

    """
    Fonction qui retourne toute la data de 2005 a 2018, moins les nulles / manquants / et donnees
    pas interessantes.
    """
    print("Cleaning Usagers de 2005 à 2018 -> ...")
    directory = "data/raw_data/usagers/1"
    files = [file for file in os.listdir(directory) if file.startswith("usagers_") and file.endswith(".csv")]

    data = pd.DataFrame()

    # Boucle pour lire chaque fichier CSV et concaténer les données
    for file in files:
        df = pd.read_csv(os.path.join(directory, file), sep=',', encoding='ISO-8859-1', engine='python')
        data = pd.concat([data, df], ignore_index=True)

    # Drop les colonnes avec valeurs manquantes, nulles ou incoherentes
    data = data.drop(columns=['secu', 'place', 'actp', "num_veh"])
    data.dropna(inplace=True)

    data = data.astype({'locp':int, 'etatp':int, 'an_nais':int, 'trajet':int})
    print("Cleaning Usagers de 2005 à 2018 -> Done")
    return data


def usagers_clean_data_19_21():
    """
    Fonction qui retourne toute la data de 2019 a 2021, moins les nulles / manquants / et donnees
    pas interessantes.
    """
    print("Cleaning Usagers de 2019 à 2021 -> ...")

    directory = "data/raw_data/usagers/2"
    files = [file for file in os.listdir(directory) if file.startswith("usagers_") and file.endswith(".csv")]

    data = pd.DataFrame()
    for file in files:
        df = pd.read_csv(os.path.join(directory, file), sep=';', encoding='ISO-8859-1', engine='python')
        data = pd.concat([data, df], ignore_index=True)

    data = data.drop(columns=['id_vehicule', 'place', 'secu1', 'secu2', 'secu3', 'actp', "num_veh"])
    data.dropna(inplace=True)

    # calculer la moyenne de la colonne 'an_nais' et remplacer les valeurs manquantes dans la colonne 'an_nais' par la moyenne
    moyenne = data['an_nais'].median()
    data['an_nais'].fillna(moyenne, inplace=True)

    data = data.astype({'an_nais':int})
    print("Cleaning Usagers de 2019 à 2021 -> Done")
    return data
