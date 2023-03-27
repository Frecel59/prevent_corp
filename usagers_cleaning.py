import os
import pandas as pd


def get_data_usagers_old():

    """
    Get all the 'old' data sets in 1 dataframe:
    - coming from the right  directory
    - get rid of all the missing and null data
    - get rid of the meaning less data
    - return a dataframe including a 'mergeable' dataframe
    """

    # Chemin vers le dossier contenant les fichiers CSV
    directory = "../data/raw_data/usagers/1"

    # Création d'une liste de noms de fichiers
    files = [file for file in os.listdir(directory) if file.startswith("usagers_") and file.endswith(".csv")]

    concatenated_usagers1 = pd.DataFrame()

    # Boucle pour lire chaque fichier CSV et concaténer les données
    for file in files:
        df = pd.read_csv(os.path.join(directory, file), sep=',', encoding='ISO-8859-1', engine='python')
        concatenated_usagers1_df = pd.concat([concatenated_usagers1, df], ignore_index=True)

    # Drop les colonnes avec valeurs manquantes, nulles ou incoherentes
    concatenated_usagers_df1 = concatenated_usagers_df1.drop(columns=['secu', 'place', 'actp'])
    concatenated_usagers_df1.dropna(inplace=True)

    concatenated_usagers_df1 = concatenated_usagers_df1.astype({'locp':int, 'etatp':int, 'an_nais':int, 'trajet':int})

    return concatenated_usagers1_df


def get_data_usagers_new():

    """
    Get all the 'new' data sets in 1 dataframe:
    - coming from the right  directory
    - get rid of all the missing and null data
    - get rid of the meaning less data
    - return a dataframe including a 'mergeable' dataframe
    """

    # Chemin vers le dossier contenant les fichiers CSV
    directory = "../data/raw_data/usagers/2"

    # Création d'une liste de noms de fichiers
    files = [file for file in os.listdir(directory) if file.startswith("usagers_") and file.endswith(".csv")]

    concatenated_usagers2 = pd.DataFrame()

    # Boucle pour lire chaque fichier CSV et concaténer les données
    for file in files:
        df2 = pd.read_csv(os.path.join(directory, file), sep=';', encoding='ISO-8859-1', engine='python')
        concatenated_usagers2_df = pd.concat([concatenated_usagers2, df2], ignore_index=True)

    # Drop les colonnes avec valeurs manquantes, nulles ou incoherentes
    concatenated_usagers_df2 = concatenated_usagers_df2.drop(columns=['id_vehicule', 'place', 'secu1', 'secu2', 'secu3', 'actp'])
    concatenated_usagers_df2.dropna(inplace=True)

    # calculer la moyenne de la colonne 'an_nais' et remplacer les valeurs manquantes dans la colonne 'an_nais' par la moyenne
    moyenne = concatenated_usagers_df2['an_nais'].median()
    concatenated_usagers_df2['an_nais'].fillna(moyenne, inplace=True)

    concatenated_usagers_df2 = concatenated_usagers_df2.astype({'an_nais':int})

    return concatenated_usagers2_df


def get_usagers_data():
    usagers_df = pd.concat([concatenated_usagers1_df, concatenated_usagers2_df], ignore_index=True)
    return usagers_df
