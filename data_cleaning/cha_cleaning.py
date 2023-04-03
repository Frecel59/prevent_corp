import pandas as pd
import os

def charac_clean_data_05_18():
    """ Fonction qui nettoies les données des années 2005 à 2018
        et retourne un data frame de toutes ces données
    """
    print("Cleaning Characteristics de 2005 à 2018 ...")

    def update_format(dep):
        if dep > 90:
            dep = str(dep)
            return dep[:2]
        dep = str(dep)
        return dep[:1]

    directory = "data/raw_data/characteristiques/1"
    files = [file for file in os.listdir(directory) if file.startswith("caracteristiques_") and file.endswith(".csv")]
    data = pd.DataFrame()
    for file in files:
        if file == "caracteristiques_2009.csv":
            df = pd.read_csv(os.path.join(directory, file), sep='\t', encoding='ISO-8859-1', engine='python')
            data = pd.concat([data, df], ignore_index=True)
            continue
        df = pd.read_csv(os.path.join(directory, file), sep=',', encoding='ISO-8859-1', engine='python')
        data = pd.concat([data, df], ignore_index=True)

    data = data.drop(columns=["hrmn", "com", "adr", "lat", "long", "gps"])
    data["dep"] = data["dep"].apply(update_format)
    data = data.astype({'dep': int})
    deps_to_delete = [20, 97]
    data = data.drop(data[data['dep'].isin(deps_to_delete)].index)
    print("Cleaning Caractéristique de 2005 à 2018 -> Done")
    return data

def charac_clean_data_19_21():
    """ Fonction qui nettoies les données des années 2019 à 2021
        et retourne un data frame de toutes ces données
    """
    print("Cleaning Characteristics de 2019 à 2021 ...")
    directory = "data/raw_data/characteristiques/2"
    files = [file for file in os.listdir(directory) if file.startswith("caracteristiques_") and file.endswith(".csv")]
    data = pd.DataFrame()

    for file in files:
        df2 = pd.read_csv(os.path.join(directory, file), sep=';', encoding='ISO-8859-1', engine='python')
        data = pd.concat([data, df2], ignore_index=True)

    data = data.drop(columns=["jour", "hrmn", "com", "adr", "lat", "long"])
    deps_to_delete = ["972", "2B", "973", "2A", "987", "986", "971", "977", "978", "975", "988", "976", "974" ]
    data = data.drop(data[data['dep'].isin(deps_to_delete)].index)
    data = data.astype({'dep': int})
    print("Cleaning Characteristics de 2019 à 2021 -> Done")
    return data

if __name__ == "__main__":
    pass
