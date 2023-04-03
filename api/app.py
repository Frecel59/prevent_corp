import streamlit as st
from PIL import Image


# Définir la couleur de fond de la page
st.set_page_config(page_title="Prevent-Corp")

# Ajouter le CSS pour changer la couleur de fond
st.markdown(
    f"""
    <style>
        body, .stApp, .stApp > div > div {{
            background-color: #134f5c;
        }}
    </style>
    """, unsafe_allow_html=True
)

# Récupérer la valeur du choix à partir des paramètres de l'URL
query_params = st.experimental_get_query_params()
choice = query_params.get("choice", ["Accueil"])[0]

# Créer la barre de navigation horizontale
menu = ["Accueil", "Visualisation", "Prédiction", "Suggestion", "L'équipe"]
st.markdown(
    f"""
    <style>

        .navbar {{
            overflow: hidden;
            display: flex;
        }}
        .navbar a {{
            margin-right: 10px;
            background-color: #ffd966ff;
            font-size: 18px;
            color: black;
            text-align: center;
            padding: 12px 16px;
            border: 1px solid black;
            border-radius: 5px;
            width: 200px;
            height: 50px;
        }}
        .navbar a:hover {{
            color: black;
        }}
        .navbar a.active {{
            color: white;
        }}
    </style>
    """
, unsafe_allow_html=True)

link_format = lambda name: f'<a class="{"active" if choice==name else ""}" href="?choice={name}" target="_self">{name}</a>'
menu_links = "".join([link_format(name) for name in menu])

st.markdown(f'<div class="navbar">{menu_links}</div>', unsafe_allow_html=True)

# Afficher la page sélectionnée
if choice == "Accueil":
    st.title("Accueil")
    # Ajouter le contenu de la page d'accueil ici
elif choice == "Visualisation":
    st.title("Data-vis accident global")
    # Ajouter le contenu de la page 1 ici
elif choice == "Prédiction":
    st.title("prédiction de votre département !")
    # Ajouter le contenu de la page 2 ici
elif choice == "Suggestion":
    st.title("Suggestion de prevent corp")
    # Ajouter le contenu de la page 3 ici
elif choice == "L'équipe":
    st.title("Notre équipe")
    # Ajouter le contenu de la page 4 ici
