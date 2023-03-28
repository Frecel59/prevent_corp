import os
import pandas as pd

def clean_lieux_11_18():
    """
    Importation des datasets de 2011 à 2018
    """
    # Chemin vers le dossier contenant les fichiers CSV
    directory = "../data/data_raw/lieux/1"

    # Création d'une liste de noms de fichiers
    files = [file for file in os.listdir(directory) if file.startswith("lieux_") and file.endswith(".csv")]

    # Initialisation du dataframe pour stocker les données concaténées
    concatenated_lieux1 = pd.DataFrame()

    # Boucle pour lire chaque fichier CSV et concaténer les données
    for file in files:
        # Lecture du fichier CSV
        df = pd.read_csv(os.path.join(directory, file), sep=',', encoding='ISO-8859-1', engine='python')
        # Concaténation avec le dataframe principal
        concatenated_lieux_df1 = pd.concat([concatenated_lieux1, df], ignore_index=True)

    # Sauvegarde du dataframe concaténé dans un fichier CSV
    # concatenated_lieux_df1.to_csv("../data/clean_data/lieux1_concat.csv", index=False)

    # Drop des colonnes inutiles
    concatenated_lieux_df1 = concatenated_lieux_df1.drop(columns=['voie','v1','v2', 'pr', 'pr1', 'lartpc', 'vma', 'larrout'])

    # Supression des nan
    concatenated_lieux_df1.dropna(inplace=True)

    # Transformation en int64
    concatenated_lieux_df1 = concatenated_lieux_df1.astype(int)

    return concatenated_lieux_df1


def clean_lieux_19_21():
    """
    Importation des datasets de 2019 à 2021
    """
    # Chemin vers le dossier contenant les fichiers CSV
    directory = "../data/data_raw/lieux/2"

    # Création d'une liste de noms de fichiers
    files = [file for file in os.listdir(directory) if file.startswith("lieux_") and file.endswith(".csv")]

    # Initialisation du dataframe pour stocker les données concaténées
    concatenated_df2 = pd.DataFrame()

    # Boucle pour lire chaque fichier CSV et concaténer les données
    for file in files:
        # Lecture du fichier CSV
        df2 = pd.read_csv(os.path.join(directory, file), sep=';', encoding='ISO-8859-1', engine='python')
        # Concaténation avec le dataframe principal
        concatenated_lieux_df2 = pd.concat([concatenated_df2, df2], ignore_index=True)

    # Sauvegarde du dataframe concaténé dans un fichier CSV
    # concatenated_lieux_df2.to_csv("../data/clean_data/lieux2_concat2.csv", index=False)

    # Drop des colonnes inutiles
    concatenated_lieux_df2 = concatenated_lieux_df2.drop(columns=['voie','v1','v2', 'pr', 'pr1', 'lartpc', 'vma', 'larrout'])

    return concatenated_lieux_df2


def concat_lieux(concatenated_lieux_df1, concatenated_lieux_df2):
    """
    Concat des 2 dataframe
    """
    lieux_df = pd.concat([concatenated_lieux_df1, concatenated_lieux_df2], ignore_index=True)

    return lieux_df
