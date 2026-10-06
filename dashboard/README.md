# Dashboard Looker Studio (version de Zohair)

Dashboard réalisé à partir de mon notebook `notebooks/rfm_zohair.ipynb`, pour m'entraîner sur Looker Studio (Data Studio). Le dashboard retenu pour la présentation du projet est celui de Ludivine.

**Voir le dashboard en ligne :** https://datastudio.google.com/s/mE50rLfsrhY

**Version PDF :** [dashboard_looker_zohair.pdf](dashboard_looker_zohair.pdf)

## Données

Le fichier `data/processed/rfm_looker.csv` est exporté par l'étape 6 du notebook : une ligne par client, avec sa Récence, sa Fréquence, son Montant, son cluster, son persona et ses coordonnées sur les deux premiers axes de la PCA.

## Contenu du dashboard

- Deux chiffres clés : **4 317 clients** et **8 291 748,56 £** de chiffre d'affaires net.
- Le nombre de clients par persona.
- Le chiffre d'affaires par persona.
- Un tableau des profils moyens (Récence, Fréquence, Montant) par persona.
- Un filtre pour afficher un seul persona.
- Le nuage de points des clients sur les deux premiers axes de la PCA.

## Les 4 personas (K-Means, K = 4)

| Persona | Clients | Part des clients | Part du CA |
|---|---|---|---|
| Les Fans | 697 | 16,1 % | 64,7 % |
| Les Habitués | 1 180 | 27,3 % | 23,3 % |
| Les Curieux | 827 | 19,2 % | 5,5 % |
| Les Endormis | 1 613 | 37,4 % | 6,5 % |

Chaque persona garde la même couleur dans le notebook et dans le dashboard (sans rouge ni vert).
