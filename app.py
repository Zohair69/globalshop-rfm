from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import streamlit as st

# Dossier où se trouvent les fichiers sauvegardés par le notebook (section 12.1)
DOSSIER_MODELES = Path(__file__).parent / "models"


@st.cache_resource
def charger_modeles():
    scaler = joblib.load(DOSSIER_MODELES / "scaler.joblib")
    modele = joblib.load(DOSSIER_MODELES / "kmeans_final.joblib")
    dicos = joblib.load(DOSSIER_MODELES / "segments.joblib")
    return scaler, modele, dicos


scaler, modele, dicos = charger_modeles()

st.set_page_config(page_title="GlobalShop Direct - Simulateur de segment", page_icon="🛒")

st.title("GlobalShop Direct : simulateur de segment client")
st.write(
    "Entrez la Récence, la Fréquence et le Montant d'un client. "
    "L'application lui attribue un segment et propose une action marketing."
)

recence = st.number_input("Récence : nombre de jours depuis le dernier achat", min_value=1, step=1)
frequence = st.number_input("Fréquence : nombre de commandes", min_value=1, step=1)
montant = st.number_input("Montant : total net dépensé (£)", min_value=0.01, step=10.0)

if st.button("Trouver le segment"):
    # Même chemin que dans le notebook : log1p, standardisation, prédiction
    client = pd.DataFrame({"recence": [recence], "frequence": [frequence], "montant": [montant]})
    client_log = np.log1p(client)
    client_standardise = pd.DataFrame(scaler.transform(client_log), columns=client.columns)
    cluster = modele.predict(client_standardise)[0]

    segment = dicos["noms_segments"][cluster]
    action = dicos["actions_segments"][segment]

    st.subheader("Segment : " + segment)
    st.info("Action recommandée : " + action)
    st.caption("Cluster K-Means n° " + str(cluster))
