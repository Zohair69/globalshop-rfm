# GlobalShop Direct : segmentation client RFM

Projet réalisé en binôme dans le cadre de la formation **Data Analyst de Simplon Lyon**.

**Auteurs :** Ludivine Thinet et Zohair Nazhaoui

## Contexte

La direction marketing de GlobalShop Direct, une plateforme e-commerce, veut mieux connaître ses clients pour adapter ses actions. À partir de l'historique des ventes (jeu de données *Online Retail*, décembre 2010 à décembre 2011), on regroupe les clients selon leur comportement d'achat avec la méthode **RFM** :

- **Récence** : nombre de jours depuis le dernier achat ;
- **Fréquence** : nombre de commandes ;
- **Montant** : total net dépensé (annulations déduites), en livres sterling.

## Démarche

1. **Nettoyage** : de 541 909 à 393 357 lignes (lignes sans client, doublons, codes non-produits, annulations, prix incohérents).
2. **Construction du dataset RFM** : 4 321 clients après retrait des montants nuls ou négatifs.
3. **Prétraitement** : transformation `log1p` pour réduire l'asymétrie, puis standardisation (`StandardScaler`).
4. **Clustering** : méthode du coude, score de silhouette, comparaison K-Means et clustering hiérarchique (CAH). Modèle retenu : **K-Means à 6 clusters**.
5. **PCA** : les deux premiers axes gardent 94 % de l'information et permettent de visualiser les segments en 2D.
6. **Profilage** : un nom de segment et une action marketing pour chaque cluster.

## Les 6 segments

| Segment | Clients | Part des clients | Part du CA | Profil typique (médianes) |
|---|---|---|---|---|
| Champions | 316 | 7,3 % | 50,1 % | 5 jours, 15 commandes, 5 675 £ |
| Fidèles | 634 | 14,7 % | 22,8 % | 32 jours, 6,5 commandes, 2 461 £ |
| Prometteurs | 656 | 15,2 % | 9,6 % | 10 jours, 4 commandes, 1 016 £ |
| Occasionnels | 821 | 19,0 % | 3,1 % | 34 jours, 1 commande, 294 £ |
| À risque | 929 | 21,5 % | 11,5 % | 94 jours, 2 commandes, 825 £ |
| Perdus | 965 | 22,3 % | 2,9 % | 240 jours, 1 commande, 218 £ |

Les Champions représentent 7,3 % des clients mais 50,1 % du chiffre d'affaires.

## Le simulateur Streamlit : « Le radar client »

L'application permet de saisir la Récence, la Fréquence et le Montant d'un nouveau client. Elle refait le même chemin que le notebook (`log1p`, standardisation, prédiction K-Means), puis affiche son segment et l'action marketing recommandée.

**Application en ligne :** https://globalshop-rfm-ludivine-zohair.streamlit.app

Test de vérification : le client 12347 (3 jours, 7 commandes, 4 310 £) est classé dans les **Champions**, comme dans le notebook.

## Structure du projet

```
globalshop-rfm/
├── .streamlit/
│   └── config.toml        # thème de l'application
├── data/                  # données (exclues du suivi Git)
├── models/
│   ├── scaler.joblib      # standardisation apprise sur les clients
│   ├── kmeans_final.joblib  # modèle K-Means à 6 clusters
│   └── segments.joblib    # noms des segments et actions marketing
├── notebooks/             # notebook d'analyse
├── app.py                 # application Streamlit
├── requirements.txt       # bibliothèques et versions
└── README.md
```

## Lancer l'application en local

```bash
git clone https://github.com/Zohair69/globalshop-rfm.git
cd globalshop-rfm
pip install -r requirements.txt
streamlit run app.py
```

## Outils

Python (pandas, NumPy, scikit-learn, Matplotlib, Seaborn), Jupyter, Streamlit, Looker Studio (Data Studio), Git et GitHub.
