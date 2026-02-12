import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate
import pandas as pd

# Nos données utilisateurs doivent respecter ce format
url_csv = f"https://raw.githubusercontent.com/Antonio-prxd/Qu-te-S/refs/heads/main/authentification.csv"
df = pd.read_csv(url_csv)
lesDonneesDesComptes = {
    'usernames': {    
        }
    }

for i in range(len(df)):
    name = df.iloc[i, 0]
    password = df.iloc[i, 1]
    email = df.iloc[i, 2] 
    failed_login_attempts = df.iloc[i, 3] 
    logged_in = df.iloc[i, 4] 
    role = df.iloc[i, 5]
    lesDonneesDesComptes['usernames'][name] = { 'name': name,
                                                'password': password,
                                                  'email': email,
                                                    'failed_login_attempts': failed_login_attempts,
                                                      'logged_in': logged_in,
                                                        'role': role }

authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie name",         # Le nom du cookie, un str quelconque
    "cookie key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)

authenticator.login()
if st.session_state["authentication_status"] is None:
    st.info("Username : Sacha / Password : Bourg-Palette")

    
if st.session_state["authentication_status"]:
    with st.sidebar:
        st.title(f"Bienvenu {st.session_state['name']} !")
        # Le bouton de déconnexion
        authenticator.logout("Déconnexion")
        selection = option_menu(
            menu_title=None,
            options = ["Pokedex", "Voici mes starters"], 
            icons=["journal-text", "stars"],
        )
    if selection == "Pokedex":
        st.title("Bienvenue dans mon pokedex !")
        st.image("https://eternia.fr/public/media//rb/ressources/pokedex2.png")
    elif selection == "Voici mes starters":
        # Création de 3 colonnes 
        col1, col2, col3 ,col4= st.columns(4)

        # Contenu de la première colonne : 
        with col1:
            st.write("PIKACHU")
            st.image("https://pngimg.com/uploads/pokemon/small/pokemon_PNG9.png")

        # Contenu de la deuxième colonne :
        with col2:
            st.write("SALAMECHE")
            st.image("https://www.pokebip.com/pokedex-images/300/4.png?v=za-2.0")

        # Contenu de la troisième colonne : 
        with col3:
            st.write("CARAPUCE")
            st.image("https://www.pokepedia.fr/images/thumb/c/cc/Carapuce-RFVF.png/250px-Carapuce-RFVF.png")
        with col4: 
            st.write("BULBIZARRE") 
            st.image("https://www.pokepedia.fr/images/thumb/e/ef/Bulbizarre-RFVF.png/250px-Bulbizarre-RFVF.png")
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
