# Maison Nsaia — consignes permanentes

## Annonces Vinted

Dès que de nouveaux articles arrivent (fiche Shopify, photo, facture ADN ou
simple description), rédiger leur annonce Vinted **au même format que
`docs/vinted-annonces.md`** et l'ajouter à ce fichier, à son rang de vitesse
de vente.

### Périmètre
- **Seulement ce qui reste à vendre** (stock > 0). Les articles vendus ne
  figurent nulle part, même pas dans une liste « écartés ».
- Un article **sans photo** va dans la section « ⏸️ En attente de photos »
  (numérotée M1, M2…), et non dans la liste à publier.
- Publication depuis le **compte Vinted Pro** : le neuf y est accepté.

### Format d'une annonce
1. **Titre** : marque + type + couleur + « neuf/neuve(s) » (+ « étiquette » si
   c'est le cas) + taille (`T.40`, `T.M`) ou pointure (`P.38`).
2. **Champs Vinted** : catégorie (chemin complet), marque, taille au format
   Vinted (`L / 40 / 12`), état, prix.
3. **Description**, dans un bloc à copier, avec des emojis :
   - ligne article : modèle, couleur, taille ;
   - ligne état, avec la référence si elle est connue (voir `stock.md`) ;
   - `💰 Valeur boutique ~X €` ;
   - `✅ 100 % authentique – authentifié en maison de vente`, **avec le bon
     accord** : `authentiques – authentifiées` pour une paire de chaussures,
     `authentifiée` pour une robe ou une jupe, `authentifié` pour un short, un
     polo, un top, un jean, un pantalon ou un blazer ;
   - `📦 Envoi soigné sous 48 h` ;
   - **15 à 19 hashtags** : marque, modèle, type, couleur, taille, style,
     usage, `#neuf`. Pas de `-` ni de `&` dans un hashtag (ils le coupent).
4. **Photos** : les liens Shopify CDN, sans le paramètre `?v=`.
5. **Notes sous l'annonce** : prix plancher, concurrence, photos à ajouter,
   corrections faites.

### Ce qu'on n'écrit jamais
- « lot de déstockage », « acheté en maison de vente ».
- Le nom d'un revendeur ou d'un outlet qui vend la pièce moins cher (YOOX,
  outlet officiel…).
- Une affirmation non vérifiée : `#madeinitaly` sans preuve, `#vintage` sur une
  pièce récente.
- Une valeur boutique supérieure au prix le plus haut relevé dans `stock.md`.
- `#invitée` sur une robe blanche ou ivoire : viser plutôt mariée, mairie,
  baptême.

### État : être honnête
- Modèle d'exposition → **Neuf sans étiquette**.
- Pièce nettoyée ou essayée → **Très bon état**.
- Le badge « Neuf avec étiquette » de la fiche Shopify n'est pas une preuve :
  vérifier avec la description de la pièce.

### Prix
- Prix = **prix Shopify actuel**.
- Donner un **plancher** : marge visée 25 €, coefficient 0,876 (URSSAF), donc
  plancher ≈ (coût + 25) / 0,876.
- **Coûts** : le tableur `exports/maison-nsaia-stock.xlsx` fait foi sur
  `stock.md`.
- Signaler la concurrence relevée dans `stock.md`.

### Tri par vitesse de vente
Classer en 🟢 rapide / 🟡 moyen / 🔴 plus lent selon :
- la notoriété de la marque sur Vinted ;
- la taille : 38-40 et M/L se vendent le mieux ;
- le prix : sous 70 €, ça part plus vite ;
- les photos.

Une pointure 40 mixte va en catégorie Femmes, avec `#mixte`.

### Stock Shopify
- **Ne pas passer le stock à 0** quand une pièce est publiée sur Vinted. C'est
  le choix du 17/10 : la boutique n'est pas encore référencée, et un double
  achat se règle par une annulation et un remboursement.
- Après une vente Vinted : stock à 0 + tag `Vendu` sur Shopify, puis une ligne
  dans `exports/maison-nsaia-registres.xlsx`.

### Façon de travailler
- Sur « suivant », envoyer **une annonce à la fois**.
- **Corriger d'office** les erreurs (taille, accord, faute de marque, prix sous
  le plancher, photo prise sur internet…) et dire en une ligne ce qui a été
  changé.
- Commit et push après chaque modification de `docs/vinted-annonces.md`.
- Ne pas genrer l'utilisatrice ou l'utilisateur dans les réponses.
