import pandas as pd
import os

from data_cleaning.cha_cleaning import charac_clean_data_12_18, charac_clean_data_19_21
from data_cleaning.lieux_cleaning import lieux_clean_data_12_18, lieux_clean_data_19_21
from data_cleaning.usagers_cleaning import usagers_clean_data_12_18, usagers_clean_data_19_21
from data_cleaning.vehicules_cleaning import vehicules_clean_data_12_18, vehicules_clean_data_19_21

def concatenate_function(name, data_1 :pd.DataFrame, data_2 :pd.DataFrame) -> pd.DataFrame:
    """ Fusionne les deux data fram de caracéristique et retourne le
        data farm avec les accidents dans lo'dre d'arrivé
    """
    print(f"Fusion des Dataframe {name} 2011-2018 et 2019-2021 ...")
    return pd.concat([data_1, data_2], ignore_index=True).sort_values(by="Num_Acc")


def clean_characteristics_data():
    data_carac = concatenate_function("Characteristics", charac_clean_data_12_18(), charac_clean_data_19_21())
    print(f"Fusion des Dataframe Characteristics 2011-2018 et 2019-2021 -> Done")
    return data_carac


def clean_all_data():
    data_carac = concatenate_function("Characteristics", charac_clean_data_12_18(), charac_clean_data_19_21())
    print(f"Fusion des Dataframe Characteristics 2011-2018 et 2019-2021 -> Done")
    data_lieux = concatenate_function("Lieux", lieux_clean_data_12_18(), lieux_clean_data_19_21())
    print(f"Fusion des Dataframe lieux 2011-2018 et 2019-2021 -> Done")
    data_usagers = concatenate_function("Usagers", usagers_clean_data_12_18(), usagers_clean_data_19_21())
    print(f"Fusion des Dataframe Usagers 2011-2018 et 2019-2021 -> Done")
    data_vehicules = concatenate_function("Véhicules", vehicules_clean_data_12_18(), vehicules_clean_data_19_21())
    print(f"Fusion des Dataframe Véhicules 2011-2018 et 2019-2021 -> Done")

    return data_carac, data_lieux, data_usagers, data_vehicules

if __name__ == "__main__":
    clean_all_data()
