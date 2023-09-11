Prevent Corp : Prédiction des accidents de la route mensuel en France
Objectif : Développer un model a partir de nos connaissances en Data Science afin prédire les accidents de la route mensuels en France. L'application vise à permettre aux autorités et aux organisations de mieux se préparer et de réduire les accidents de la route. La démonstration finale de ce projet a été présentée, révélant le potentiel et l'efficacité de notre solution. Il a été passionnant de travailler sur ce projet unique, appelé "Prevent Corp", où notre mission était de développer 95 modèles distincts pour arriver à une solution prédictive robuste et innovante.

Axes d'améliorations:
Intégration de variables explicatives supplementaires
Explorer les hyper parametres de nos modeles par departement
Ajouter d’autre zones géographiques: plus de data et mieux ce sera
Apporter de la consistance lors de la récolte des données.

Grandes étapes:
Extraction des raws data provenant du site du gouvernement francais
Nettoyage, filtration et premieres analyses afin de garder uniquement les data cohérentes
Synchroniser les datasets propres sur GCP
Explorer les différentes solution pour finalement developper 95 modèles SARIMA, plus cross validation
Chargement des resultats du model sur GCP
Utilisation de Docker pour créer un environnement containerisé pour l'application
Interface et API via Streamlit

Fichiers & Explications
cleaning.py
Ce script est dédié à la préparation des données. Il contient des fonctions qui nettoient et fusionnent les jeux de données pour différents aspects tels que les caractéristiques, les lieux, les usagers et les véhicules.

cross_val.py
Ce fichier gère la validation croisée des modèles. Il utilise le modèle SARIMA pour évaluer les performances sur différents plis de données.

data.py
Ce fichier contient une fonction pour télécharger les données nettoyées à partir d'un stockage GCP (Google Cloud Platform).

model.py
Définit la structure et les méthodes associées au modèle SARIMA, notamment la formation, la prédiction, l'évaluation et la sauvegarde du modèle sur le stockage local ou GCP.

preprocessing.py
Fichier dédié à la préparation des données avant de les entrer dans le modèle. Il gère le chargement des données, leur préparation, et la création des séquences pour le modèle temporel.

Comment exécuter ?
Assurez-vous d'avoir tous les paquets nécessaires installés. Si ce n'est pas le cas, installez-les via pip :
pip install -r requirements.txt

Exécutez le fichier cleaning.py pour nettoyer et préparer vos données :
python cleaning.py

Lancez la validation croisée avec cross_val.py :
python cross_val.py

Pour obtenir des prédictions, utilisez le fichier model.py :
python model.py

Remerciements
Un grand merci à l'équipe composé de Cédric, Victor, Titouan et Arnaud, ainsi qu'aux équipes enseignantes du Wagon pour avoir rendu ce projet possible et pour avoir travaillé sans relâche afin de produire une solution innovatrice. À la prochaine aventure !
