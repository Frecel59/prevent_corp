Prevent Corp : Prédiction des Accidents de la Route en France

Objectif
Développer un 'worflow' afin de prédire les accidents mensuels de la route en France (hors Corse et DOM/TOM). L'application vise à permettre aux autorités et aux organisations de mieux se préparer et de réduire les accidents de la route. Durant ce projet, la démo finale a été présentée, révélant le potentiel et l'efficacité de notre solution. Il a été passionnant de travailler sur ce projet unique, appelé "Prevent Corp", où notre mission était de développer 95 modèles distincts SARIMA pour arriver à une solution prédictive robuste et inédite.

Fichiers & Explications

cleaning.py
Ce script est dédié à la préparation des data. Il contient des fonctions qui nettoient et fusionnent les jeux de données pour différents aspects tels que les caractéristiques, les lieux, les usagers et les véhicules.

cross_val.py
Ce fichier gère la validation croisée des modèles. Il utilise le modèle SARIMA pour évaluer les performances sur différents plis de données.

data.py
Ce fichier contient une fonction pour télécharger les données nettoyées à partir d'un stockage GCP.

model.py
Définit la structure et les méthodes associées au modèle SARIMA, notamment la formation, la prédiction, l'évaluation et la sauvegarde du modèle sur le stockage local ou GCP.

preprocessing.py
Fichier dédié à la préparation des données avant de les entrer dans le modèle. Il gère le chargement des données, leur préparation, et la création des séquences pour le modèle temporel.

Comment exécuter ?
Assurez-vous d'avoir tous les packs nécessaires installés. Si ce n'est pas le cas, installez-les via pip :
pip install -r requirements.txt

Remerciements
Un grand merci à l'équipe; Cedric, Victor, Titouan, Arnaud, ainsi qu'aux équipes pédagogiques du Wagon pour avoir rendu ce projet possible et pour avoir travaillé sans relâche durant 9 semaines !
