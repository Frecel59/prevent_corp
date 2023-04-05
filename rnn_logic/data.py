import pandas as pd

def import_clean_data():
    """ Télécharge les données déjà preprocessés """

    data = pd.read_pickle('https://storage.googleapis.com/data-prevent-corp/caracteristiques_final.pkl')
    print("✅ Data load")
    return data

if __name__ == "__main__":
    data = import_clean_data()
