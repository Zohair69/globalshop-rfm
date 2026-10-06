from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import streamlit as st

# Dossier où se trouvent les fichiers sauvegardés par le notebook (section 12.1)
DOSSIER_MODELES = Path(__file__).parent / "models"

# Une couleur par segment (sans rouge ni vert)
COULEURS_SEGMENTS = {
    "Champions": "#FFD700",
    "Fidèles": "#4682B4",
    "Prometteurs": "#800080",
    "Occasionnels": "#FF8C00",
    "À risque": "#000000",
    "Perdus": "#808080",
}


@st.cache_resource
def charger_modeles():
    scaler = joblib.load(DOSSIER_MODELES / "scaler.joblib")
    modele = joblib.load(DOSSIER_MODELES / "kmeans_final.joblib")
    dicos = joblib.load(DOSSIER_MODELES / "segments.joblib")
    return scaler, modele, dicos


scaler, modele, dicos = charger_modeles()

st.set_page_config(page_title="Le radar client de GlobalShop Direct", page_icon="🛒")

st.title("Le radar client de GlobalShop Direct")
st.write(
    "Le simulateur de segmentation de GlobalShop Direct. "
    "Renseignez l'historique d'un client : le modèle le range dans l'un des 6 segments "
    "et propose l'action marketing adaptée."
)

# Les trois saisies côte à côte
col1, col2, col3 = st.columns(3)
with col1:
    recence = st.number_input("Récence (jours)", min_value=1, step=1,
                              help="Nombre de jours depuis le dernier achat")
with col2:
    frequence = st.number_input("Fréquence (commandes)", min_value=1, step=1,
                                help="Nombre de commandes passées")
with col3:
    montant = st.number_input("Montant (£)", min_value=0.01, step=10.0,
                              help="Total net dépensé, annulations déduites")

if st.button("Trouver le segment", type="primary"):
    # Même chemin que dans le notebook : log1p, standardisation, prédiction
    client = pd.DataFrame({"recence": [recence], "frequence": [frequence], "montant": [montant]})
    client_log = np.log1p(client)
    client_standardise = pd.DataFrame(scaler.transform(client_log), columns=client.columns)
    cluster = modele.predict(client_standardise)[0]

    segment = dicos["noms_segments"][cluster]
    action = dicos["actions_segments"][segment]
    couleur = COULEURS_SEGMENTS.get(segment, "#4682B4")

    # Carte de résultat : une bande de la couleur du segment à gauche
    st.markdown(
        f"""
        <div style="border-left: 10px solid {couleur}; background: #FFFFFF;
                    padding: 1.2rem 1.5rem; border-radius: 6px; margin-top: 1rem;">
            <p style="margin: 0; color: #5A6675;">Ce client appartient au segment</p>
            <p style="margin: 0.2rem 0 0.8rem 0; font-size: 2.2rem; font-weight: 700;">{segment}</p>
            <p style="margin: 0;"><b>Action recommandée :</b> {action}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.caption("Cluster K-Means n° " + str(cluster))
