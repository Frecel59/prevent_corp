import pandas as pd
import os

from data_cleaning.cha_cleaning import charac_clean_data_05_18, charac_clean_data_19_21
from data_cleaning.lieux_cleaning import lieux_clean_data_05_18, lieux_clean_data_19_21
from data_cleaning.usagers_cleaning import usagers_clean_data_05_18, usagers_clean_data_19_21
from data_cleaning.vehicules_cleaning import vehicules_clean_data_05_18, vehicules_clean_data_19_21

def concatenate_function(name, data_1 :pd.DataFrame, data_2 :pd.DataFrame) -> pd.DataFrame:
    """ Fusionne les deux data fram de caracéristique et retourne le
        data farm avec les accidents dans lo'dre d'arrivé
    """
    print(f"Fusion des Dataframe {name} 2005-2018 et 2019-2021 ...")
    data = pd.concat([data_1, data_2], ignore_index=True).sort_values(by="Num_Acc")
    print(f"Fusion des Dataframe {name} 2005-2018 et 2019-2021 -> Done ")
    return data

def save_clean_data(name, data:pd.DataFrame):
    data.to_csv(f"data/clean_data/{name}_final.csv", index=False)
    return

def clean_characteristics_data():
    data_carac = concatenate_function("Characteristics", charac_clean_data_05_18(), charac_clean_data_19_21())
    print(f"Fusion des Dataframe Characteristics 2005-2018 et 2019-2021 -> Done")
    return data_carac


def clean_all_data():
    data_carac = concatenate_function("Characteristics", charac_clean_data_05_18(), charac_clean_data_19_21())
    data_lieux = concatenate_function("Lieux", lieux_clean_data_05_18(), lieux_clean_data_19_21())
    data_usagers = concatenate_function("Usagers", usagers_clean_data_05_18(), usagers_clean_data_19_21())
    data_vehicules = concatenate_function("Véhicules", vehicules_clean_data_05_18(), vehicules_clean_data_19_21())

    print("Fin de la création des Dataframe pour toutes les catégories !")
    return data_carac, data_lieux, data_usagers, data_vehicules

if __name__ == "__main__":
    data = clean_characteristics_data()
    print(data.shape)
