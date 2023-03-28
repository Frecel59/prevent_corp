import pandas as pd
import os


def vehicules1_cleaning():
     # Chemin vers le dossier contenant les fichiers CSV
     directory = "raw_data/data/vehicules/1"

     # Création d'une liste de noms de fichiers
     files = [file for file in os.listdir(directory) if file.startswith("vehicules_") and file.endswith(".csv")]

     # Initialisation du dataframe pour stocker les données concaténées
     concatenated_vehicules1 = pd.DataFrame()

     # Boucle pour lire chaque fichier CSV et concaténer les données
     for file in files:
        # Lecture du fichier CSV
        df = pd.read_csv(os.path.join(directory, file), sep=',', encoding='ISO-8859-1', engine='python')
        # Concaténation avec le dataframe principal
        concatenated_vehicules1_df = pd.concat([concatenated_vehicules1, df], ignore_index=True)

     concatenated_vehicules1_df.dropna(inplace=True)

     concatenated_vehicules1_df= concatenated_vehicules1_df.astype({'obs':int, 'obsm':int, 'choc':int, 'manv':int})

     return concatenated_vehicules1_df


def vehicules2_cleaning():
     # Chemin vers le dossier contenant les fichiers CSV
     directory = "raw_data/data/vehicules/2"

     # Création d'une liste de noms de fichiers
     files = [file for file in os.listdir(directory) if file.startswith("vehicules_") and file.endswith(".csv")]

     # Initialisation du dataframe pour stocker les données concaténées
     concatenated_vehicules2 = pd.DataFrame()

     # Boucle pour lire chaque fichier CSV et concaténer les données
     for file in files:
         # Lecture du fichier CSV
         df = pd.read_csv(os.path.join(directory, file), sep=';', encoding='ISO-8859-1', engine='python')
         # Concaténation avec le dataframe principal
         concatenated_vehicules2_df = pd.concat([concatenated_vehicules2, df], ignore_index=True)

     return concatenated_vehicules2_df

def concat_data(concatenated_vehicules1_df, concatenated_vehicules2_df):
    vehicules = pd.concat([concatenated_vehicules1_df, concatenated_vehicules2_df], ignore_index=True)
    return vehicules
