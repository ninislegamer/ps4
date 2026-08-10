# Maison Nsaia — Feuille de route

Boutique Shopify de revente haut de gamme (grandes marques et créateurs, neuf avec
étiquette ou très bon état, pièces uniques authentifiées).

Ce document est la référence du projet : il liste ce qui doit être fait **hors code**
(par le porteur du projet) et ce qui sera construit dans ce dépôt.

---

## Phase 0 — À faire toi-même, dans cet ordre

Aucune ligne de code n'est utile tant que 0.1 à 0.5 ne sont pas faits.

### 0.1 — Cadre juridique (avant tout le reste)

- Créer / confirmer le statut (micro-entreprise en achat-revente, activité
  commerciale) et obtenir le **SIRET**. Guichet unique INPI.
- Vérifier avec un comptable / l'URSSAF :
  - le régime **franchise en base de TVA (art. 293 B du CGI)** et les seuils en
    vigueur — ils ont bougé récemment, ne pas se fier à un chiffre trouvé en ligne ;
  - le **registre des objets mobiliers** ("livre de police"), obligatoire pour les
    professionnels revendant des objets mobiliers usagés (art. 321-7 du code pénal) ;
  - la conservation des **preuves d'achat** (factures de maisons de vente, tickets,
    certificats) : c'est ce qui rend défendable la promesse "100 % authentique".
- Rédiger : CGV, mentions légales, politique de retour (14 j de rétractation),
  politique de confidentialité. Shopify génère des modèles, à faire relire.

**Bloquant pour :** activation des paiements, mention TVA sur les factures.

### 0.2 — Compte Shopify + plan

- Créer le compte sur shopify.com avec l'e-mail pro (essai gratuit).
- Nom de la boutique : `Maison Nsaia`.
- Plan recommandé au démarrage : **Basic** (facturation annuelle si la trésorerie le
  permet, ~25 % moins cher). Le plan supérieur ne se justifie que quand les frais de
  transaction économisés dépassent la différence de prix.
- Vérifier les tarifs affichés au moment de l'inscription (ils évoluent).

### 0.3 — Identité de la boutique

- Logo (SVG ou PNG transparent, version claire + sombre) et favicon.
- Palette : 1 neutre profond, 1 blanc cassé, 1 accent discret. Pas plus.
- E-mail pro sur le domaine (`contact@…`). Gandi fournit une boîte incluse selon
  l'offre, sinon Google Workspace.

### 0.4 — Domaine Gandi → Shopify

Deux options. **Garder le domaine chez Gandi** et pointer les DNS (recommandé :
réversible, pas de période de blocage).

Dans Gandi → *Nom de domaine* → *Enregistrements DNS* :

| Type  | Nom | Valeur              |
|-------|-----|---------------------|
| A     | `@` | `23.227.38.65`      |
| CNAME | `www` | `shops.myshopify.com` |

- Supprimer d'abord les enregistrements Gandi existants sur `@` et `www`
  (parking / webredir), sinon le conflit empêche la validation.
- Puis Shopify → *Paramètres* → *Domaines* → *Connecter un domaine existant*.
- Propagation : de quelques minutes à 48 h. Le certificat SSL est émis
  automatiquement par Shopify une fois les DNS validés.
- Vérifier la valeur de l'IP dans la doc Shopify au moment de la config.

### 0.5 — Paiements

- **Shopify Payments** : activer avec le SIRET + IBAN + pièce d'identité.
  Couvre carte bancaire, **Apple Pay**, **Google Pay** et Shop Pay.
- **PayPal** : compte PayPal Business, puis Shopify → *Paramètres* → *Paiements* →
  *Moyens de paiement supplémentaires*.
- Faire une commande test à 1 € avant l'ouverture.

### 0.6 — Logistique

- Choix des transporteurs et des tarifs (forfait ou par poids).
- Fournitures d'expédition, assurance sur les pièces à forte valeur.
- Procédure photo : mêmes fond / lumière / angles pour toutes les pièces.

### 0.7 — Compte Partenaire Shopify (pour l'étape 7)

- Créer un compte sur partners.shopify.com (gratuit).
- Nécessaire pour développer l'app admin (dashboard de marge).
- Aucune clé API à prévoir : les fiches produit sont rédigées en conversation,
  pas générées par une intégration.

---

## État d'avancement

Domaine : **maison-nsaia.fr** (Gandi, DNS pointés vers Shopify).
Boutique technique : `n0v0ux-pn.myshopify.com`.
Thème retenu : **Dawn**.

| Point | État |
|-------|------|
| Statut juridique / SIRET | ✅ obtenu |
| Compte Shopify + boutique | ✅ créé |
| Domaine connecté (`@`, `www`, principal) | ✅ connecté |
| Shopify Payments — acceptation | ✅ active |
| Shopify Payments — versements | ⏸️ IBAN manquant, en attente du RIB |
| PayPal Business | ⏸️ en attente du RIB |
| Boîte e-mail contact@maison-nsaia.fr | ✅ créée (Gandi) |
| E-mail expéditeur Shopify | ✅ authentifié (6 CNAME DKIM) |
| DMARC | ✅ `_dmarc` TXT `v=DMARC1; p=none` |
| Taxes (franchise en base) | ✅ vérifié — 0 %, aucune inscription fiscale |
| Double authentification | ✅ active (SMS) — passer à une appli + codes de secours |
| Forfait | ✅ Basic, promo **1 €/mois jusqu'au 10/11/2026** |
| POS Pro | ✅ désinstallé — essai qui aurait bascule à ~89 €/mois |
| Domaine des comptes clients | 🔄 à basculer sur maison-nsaia.fr |
| Thème Dawn installé et réglé | ⬜ à faire sur ordinateur |
| Photos produits harmonisées | ⬜ plus tard |

À retenir : l'éditeur de thème Shopify est inutilisable confortablement sur
téléphone. Tout le reste de l'admin passe bien en mobile.

### À faire à la prochaine session (sur ordinateur)

1. **URL des comptes clients** → basculer sur `compte.maison-nsaia.fr`.
   *Paramètres* → *Comptes client* → section **URL** → *Gérer*.
   Le DNS est déjà en place (CNAME `compte` → `shops.myshopify.com.`), il ne
   manque que la sélection du domaine. Le sélecteur ne s'affiche pas sur mobile.
2. **Thème Dawn** → installation et réglages (voir `01-theme.md`).

### À faire dès réception du RIB

3. **Shopify Payments — IBAN.** *Paramètres* → *Paiements* → **Ajouter un
   compte**. Sans ça, l'encaissement fonctionne mais les versements restent
   suspendus.
4. **PayPal Business.** Créer le compte sur paypal.com (possible dès maintenant
   sans RIB : e-mail + SIRET suffisent, le compte bancaire se rattache plus
   tard), puis Shopify → *Paiements* → *Moyens de paiement supplémentaires* →
   PayPal → relier le compte.

Rappel : carte, Apple Pay et Google Pay sont déjà couverts par Shopify Payments.
PayPal est un moyen de paiement supplémentaire, pas un remplacement.

### À faire avant l'ouverture de la boutique

- **Expédition et livraison** — choisir l'agrégateur, puis créer les zones
  **France, Belgique, Luxembourg** avec des tarifs distincts par zone
  (voir « Ouverture à l'international »).
- **Confidentialité des clients** — RGPD, bandeau cookies.
- **Politiques** — CGV, mentions légales, retours (dépend de 0.1).

**Forfait : ne rien changer avant novembre 2026.** La boutique est sur Basic avec
une promo à 1 €/mois jusqu'au 10/11/2026 (tarif plein 36 €). Basculer en annuel
maintenant ferait perdre la promo — environ 80 € de surcoût sur les trois mois
pour économiser 25 % sur un tarif plein. **Rappel à poser au 1er novembre 2026 :
passer en facturation annuelle juste avant la fin de la promo.**

Taux de carte Shopify Payments sur ce forfait : **1,5 % + 0,25 €** en ligne. À
intégrer au calcul de marge de l'étape 7 si l'on veut la marge nette réelle.

**Taxes : rien à faire.** Shopify applique 0 % faute d'inscription fiscale, ce
qui correspond exactement à la franchise en base. Ne jamais ajouter de numéro de
TVA sur cet écran tant que le régime s'applique. À revoir uniquement le jour où
le seuil de franchise est dépassé — avec le comptable.

---

## Ce qui sera codé plutôt qu'acheté

Objectif : aucun abonnement d'application récurrent.

| Fonction | Solution retenue | Coût |
|----------|------------------|------|
| Facture PDF avec mention art. 293 B | Order Printer (gratuit) + template Liquid sur mesure | 0 € |
| Favoris / wishlist | code thème + métachamps client | 0 € |
| Badges « 100 % Authentique », « Neuf avec étiquette », « Origine vérifiée » | Liquid sur la fiche produit | 0 € |
| Retrait automatique du stock à 0 | Shopify Flow (inclus) | 0 € |
| Suivi de commande | natif Shopify | 0 € |
| Dashboard de marge | app admin développée ici | 0 € |
| Rédaction des fiches produit | écrites en conversation, collées dans Shopify | 0 € |
| Bon de livraison de marque | template imprimable | 0 € |

**Ce qui reste irréductiblement payant :** l'affranchissement des colis — et il
est **refacturé au client**, donc il ne pèse pas sur la marge. Hors abonnement
Shopify et renouvellement du domaine, le coût récurrent du projet est nul.

**Étiquettes d'expédition : non générables.** Le code-barres encode un numéro de
suivi réel émis et payé auprès du transporteur ; un fichier fabriqué ne scanne
pas. Comparer **Boxtal** et **Sendcloud** (tarifs Colissimo / Mondial Relay
souvent meilleurs que Shopify Shipping, qui n'est de toute façon pas disponible
partout en France).

**Contrepartie du sur-mesure :** une mise à jour majeure du thème peut casser une
personnalisation, et il n'y a pas de support éditeur derrière. Arbitrage assumé
au volume actuel.

---

## Rédaction des fiches produit

Pas de génération automatique ni d'intégration IA. Les fiches sont **rédigées en
conversation**, puis collées dans Shopify.

Méthode : fournir pour chaque pièce la marque, le modèle, la taille ou les
dimensions, la matière, l'état exact, la provenance et, si possible, les photos.
En retour : un titre et une description conformes au brief de marque
(`brief-ia.md`) — ton de maison de vente, aucune information inventée, rareté
énoncée par le fait et non par l'adjectif.

Avantage sur une génération automatique : chaque fiche est relue, et rien
d'inexact ne peut être publié sur une pièce dont l'authenticité est l'argument
principal.

---

## Bon de livraison et carte d'authenticité

Document imprimable glissé dans chaque colis, aux couleurs de Maison Nsaia.
Zéro coût récurrent : un template, une impression.

Contenu prévu :

- En-tête Maison Nsaia (logo, `maison-nsaia.fr`, `contact@maison-nsaia.fr`)
- Numéro de commande et date
- Le détail de la pièce : marque, modèle, taille, état
- **La mention d'authenticité** : pièce sourcée et vérifiée en maison de vente,
  exemplaire unique
- La mention **« TVA non applicable, art. 293 B du CGI »**
- Le rappel du droit de rétractation de 14 jours et la marche à suivre
- Une ligne manuscrite possible (remerciement, numéro de pièce)

À concevoir à l'étape 6, en même temps que la facture PDF — les deux partagent
les mêmes données de commande.

---

## Frais de livraison

**Refacturés au client**, jamais absorbés par la marge.

À arbitrer à l'étape « Expédition » :

- **Tarif forfaitaire** par mode (ex. Colissimo suivi, Mondial Relay) — le plus
  lisible, et le plus simple à tenir sur des pièces de poids très variables.
- **Assurance** sur les pièces à forte valeur : à intégrer au forfait ou à
  proposer en option, mais jamais à négliger sur une pièce à plusieurs centaines
  d'euros.
- **Livraison offerte au-delà d'un seuil** : levier commercial à garder en
  réserve, à n'activer que si le seuil couvre réellement le port.

### Choisir un agrégateur avant de fixer les tarifs

À faire **en premier** dans cette étape : le tarif d'achat détermine le tarif
affiché au client, donc le taux de conversion. Ne pas partir du tarif guichet.

Comparer, sur les formats réels de la boutique (une paire de baskets, un
manteau, un display scellé) :

| Service | À vérifier |
|---------|-----------|
| **Boxtal** | tarifs Colissimo / Mondial Relay négociés, pas d'abonnement sur l'offre de base |
| **Sendcloud** | palier gratuit limité en volume, puis abonnement |
| **Tarif guichet La Poste** | référence de comparaison, presque toujours le plus cher |

Vérifier les conditions commerciales au moment du choix (elles évoluent) et
brancher le service retenu sur Shopify avant de créer les zones et tarifs
d'expédition. Objectif : afficher au client le tarif le plus bas possible, pas
absorber la différence.

---

## Visibilité et acquisition

**Le prix bas ne génère pas de trafic.** Il améliore la conversion une fois le
visiteur arrivé, mais aucun moteur de recherche ne classe par prix.

### Ce qui ne fonctionne pas

Le référencement naturel dépend de la pertinence, de l'ancienneté du domaine, du
contenu et des liens entrants. Un domaine neuf n'a aucune autorité : être le
moins cher du marché ne le fera pas remonter dans les résultats.

### Google Shopping : utile mais étroit

Les fiches gratuites de Google Shopping (via Merchant Center, canal
« Google & YouTube » gratuit dans Shopify) tiennent compte du prix. À activer,
puisque c'est sans coût.

Le mécanisme repose sur la comparaison de produits identifiés par code-barres.

- **Pièces neuves avec étiquette** — elles portent un code-barres : c'est le bon
  candidat pour ce canal. L'effet « moins cher » ne joue toutefois que si
  d'autres marchands référencent encore le même code ; sur une pièce de saison
  passée, la fiche apparaît seule (visibilité gratuite, sans comparaison).
- **Pièces d'occasion uniques** — aucun équivalent à comparer, le levier ne
  s'applique pas.
- **Produits scellés standardisés** — le levier fonctionne, mais ce sont ceux qui
  placent la boutique en guerre de prix (voir le critère d'admission).

Deux précautions sur Merchant Center :

- **Déclarer l'état avec exactitude.** Une pièce réellement neuve et jamais
  portée peut être déclarée neuve ; ne jamais forcer ce champ sur du très bon
  état. Une déclaration inexacte entraîne la suspension du compte, longue à
  lever.
- **Contrôle renforcé sur les grandes marques**, en raison de la contrefaçon. Le
  compte peut être examiné : les preuves d'achat (voir 0.1) servent aussi ici.

### Les canaux qui comptent réellement

1. **Requêtes précises.** Personne ne cherche « manteau pas cher » ; quelqu'un
   cherche « Margiela veste laine taille 48 occasion ». Peu de concurrence, et
   une fiche bien rédigée peut ressortir. C'est la raison du format de titre
   imposé dans `brief-ia.md` : Marque + Modèle + Caractéristique + Taille.
2. **Instagram et TikTok.** Premier canal sur la revente de pièces rares, loin
   devant la recherche. Une pièce filmée, bien éclairée.
3. **Newsletter.** Le seul canal réellement possédé, indépendant de tout
   algorithme.

---

## Newsletter

Canal prioritaire pour ce modèle : les pièces sont uniques, une pièce se vend une
fois, et l'e-mail est le seul moyen de prévenir les intéressés avant qu'elle
parte.

### Outils (aucun abonnement)

- **Formulaire d'inscription** : bloc natif de Dawn, à activer dans le pied de
  page. Aucun code, aucune app.
- **Shopify Email** : inclus, quota mensuel gratuit largement suffisant au
  volume de départ. Vérifier le quota exact à la configuration.
- **Lien de désinscription** : automatique, conforme au RGPD. Mentionner la
  newsletter dans la politique de confidentialité.

### Rythme retenu

Pas d'envoi automatique à chaque fiche publiée : techniquement bricolable, mais
un e-mail par pièce ajoutée fait fuir les abonnés.

**Campagne « Nouvelles pièces »** hebdomadaire ou bimensuelle, 5 à 10 articles
bien photographiés, préparée dans Shopify Email.

### Mécanique à mettre en place

**Accès prioritaire abonnés** : les nouveautés sont visibles 24 h avant leur mise
en ligne publique. Donne une raison concrète de s'inscrire, crée de l'urgence sur
des pièces uniques, et ne coûte rien. À implémenter à l'étape 2 (collection
réservée) ou 6 (segment client).

---

## Ouverture à l'international

Objectif retenu : une boutique perçue comme internationale, ouverte par paliers.

### Déploiement par phases

| Phase | Zone | Déclencheur |
|-------|------|-------------|
| 1 | France, Belgique, Luxembourg | ouverture |
| 2 | Allemagne, Espagne, Italie, Pays-Bas | deux ou trois envois faits sans accroc |
| 3 | Hors UE (Royaume-Uni, Suisse, États-Unis) | volume qui justifie la complexité |

À l'intérieur de l'UE il n'y a ni douane, ni déclaration, ni frais surprise pour
le client : ouvrir aux pays francophones voisins dès le premier jour ne coûte
rien en complexité. La difficulté commence **hors UE**, pas dans l'UE.

**Condition unique :** des tarifs de livraison distincts par zone. Un colis vers
Berlin coûte plus cher qu'un colis vers Toulouse — un tarif unique reviendrait à
absorber la différence sur la marge.

### À vérifier avec le comptable avant la phase 2

Sous le régime de la **franchise en base**, aucune TVA n'est collectée. Les
ventes à des particuliers dans d'autres pays de l'UE sont soumises à un **seuil
annuel de l'ordre de 10 000 €** de ventes transfrontalières, au-delà duquel
l'enregistrement au guichet **OSS** et l'application de la TVA du pays du client
entrent en jeu. L'articulation exacte avec la franchise en base relève du
comptable — à poser en même temps que la question des seuils (voir 0.1).

### Contraintes hors UE (phase 3)

- Déclarations douanières (CN22 / CN23) sur chaque colis.
- Le client peut recevoir une facture de douane à la livraison : très mauvaise
  expérience sur une pièce à plusieurs centaines d'euros. Shopify permet de
  collecter droits et taxes à la commande, moyennant **0,5 % par transaction**.
- Coût d'un retour depuis un pays lointain, à arbitrer dans la politique de
  retour.

### Paraître international sans livrer partout

Indépendant des phases ci-dessus, et activable dès l'ouverture :

- **Shopify Markets** (inclus) pour l'affichage multi-devises.
- **Translate & Adapt** (app Shopify gratuite) pour les traductions. Français +
  anglais couvre l'essentiel ; espagnol et allemand peuvent suivre. Vérifier le
  nombre de langues autorisé sur le forfait Basic au moment de la configuration.

Un visiteur étranger voit alors une boutique professionnelle dans sa langue,
même si la livraison reste limitée à la zone ouverte du moment.

---

## Phases suivantes (accompagnées, une étape à la fois)

| # | Étape | Livrable |
|---|-------|----------|
| 1 | Thème | Thème choisi, installé, réglages typo/couleurs |
| 2 | Arborescence | Collections + navigation + métachamps |
| 3 | Fiche produit | Template avec badges, double bouton d'achat |
| 4 | Stock unitaire | 1 pièce = 1 fiche, retrait auto via Shopify Flow |
| 5 | Paiements | Carte / PayPal / Apple Pay / Google Pay + checkout |
| 6 | Espace client | Compte, suivi, favoris, facture PDF (art. 293 B) |
| 7 | Dashboard admin | App de calcul de marge automatique |

---

## Structure des catégories (étape 2)

**Un seul univers : la mode.** Les cartes Pokémon, boosters et displays sortent
du périmètre. Les produits déjà en ligne qui en relèvent (cartes, Beyblade) sont
à dépublier lors de cette étape.

Navigation principale par genre et catégorie — c'est ainsi qu'un client cherche
un vêtement. Les niveaux de gamme sont des **sélections**, pas des rayons : ils
se croisent avec les catégories au lieu de les dupliquer.

```
FEMME                HOMME                SÉLECTIONS
├─ Vêtements         ├─ Vêtements         ├─ Pièces d'exception
├─ Baskets           ├─ Baskets           ├─ Créateurs
└─ Sandales          └─ Sandales          ├─ Sportswear
                                          ├─ Nouveautés
                                          ├─ Neuf avec étiquette
                                          ├─ Très bon état
                                          └─ Dernière pièce
```

### Les trois niveaux de gamme

| Niveau | Contenu | Rôle économique |
|--------|---------|-----------------|
| **Sportswear** | Nike, New Balance, adidas… | acquisition : produits connus, panier d'entrée |
| **Créateurs** | maisons et créateurs établis | cœur de l'offre |
| **Pièces d'exception** | haut du panier, 100 € de marge minimum | marge |

Côté client, ne jamais employer « marques courantes » ou « entrée de gamme » :
personne ne navigue dans un rayon qui s'annonce comme le moins prestigieux.
**Sportswear** est descriptif et neutre.

**À savoir sur le Sportswear :** une paire de Nike neuve est le produit le plus
comparable qui soit — référence connue, disponible partout, prix vérifiable en
dix secondes. C'est donc le niveau où la marge sera la plus mince. Il se justifie
comme porte d'entrée et pour le référencement, pas comme centre de profit. Ne pas
y immobiliser l'essentiel de la trésorerie.

### Règle sur l'état

**Le « très bon état » est réservé aux créateurs et aux pièces d'exception.**

Sur du sportswear, uniquement du neuf : une paire de baskets courantes portée est
une commodité, comparable et sans prime. Sur du créateur, la même logique
s'inverse — une pièce d'occasion en très bon état est une trouvaille, et
l'authentification prend toute sa valeur.

États retenus : *Neuf avec étiquette*, *Neuf sans étiquette*, *Très bon état*.
L'état est un métachamp : il alimente les filtres de navigation et les badges de
la fiche produit.

### Critère d'admission d'un produit

Un seul test, valable pour toute catégorie présente ou future :

> **Ce produit est-il comparable en un clic ?**
>
> - **Oui** — référence connue, disponible ailleurs → guerre de prix. L'acheteur
>   compare en dix secondes et prend le moins cher.
> - **Non** — pièce unique, occasion en très bon état, série épuisée → aucune
>   comparaison possible. C'est ce qui justifie la marge.

Le sportswear neuf tombe volontairement du côté « oui » : il est admis pour son
rôle d'acquisition, en quantité maîtrisée, pas parce qu'il porte la marge.

### Piste écartée pour l'instant : audio, hi-fi, instruments

Hors périmètre au lancement. Conditions à réunir avant de rouvrir le sujet :
première boutique sortie, premières ventes faites, emballage rodé.

**Vintage uniquement, jamais de neuf.** Le neuf place la boutique face à Thomann,
Amazon ou Woodbrass, qui achètent par volumes inaccessibles — marge écrasée, et
aucune prime à l'authentification puisque personne ne doute d'un appareil neuf.
Le vintage recherché (platines, matériel de studio hors production) relève au
contraire pleinement de la thèse : marché actif, prix opaques, rareté réelle.

Contraintes propres à cette famille de produits :

- **Port** : lourd et fragile, 20-30 € d'expédition et assurance obligatoire. Un
  colis cassé efface la marge de dix ventes.
- **Test** : capacité à vérifier le fonctionnement d'un appareil d'occasion et à
  le décrire honnêtement.
- **Retour** : 14 jours de rétractation sur une pièce à plusieurs centaines
  d'euros, qui peut revenir abîmée.

Deux points juridiques s'appliqueront :

- **Garantie légale de conformité de 2 ans** sur le neuf vendu par un
  professionnel, contre 12 mois sur l'occasion — sensible sur de l'électronique.
- **Éco-participation (DEEE)** sur les équipements électriques et électroniques,
  à vérifier avec le comptable en cas d'import de neuf.

La garantie légale de 2 ans sur le neuf s'applique de toute façon dès maintenant
aux pièces neuves avec étiquette.
---

## Règle de marge (étape 7)

Charges micro-entreprise achat-revente : **12,4 %** du chiffre d'affaires
(12,3 % cotisations + 0,1 % formation professionnelle).

Frais de carte Shopify Payments : **1,5 % + 0,25 €** par transaction.

```
marge = prix_vente − prix_achat − (0,124 × prix_vente) − (0,015 × prix_vente + 0,25)
      = 0,861 × prix_vente − prix_achat − 0,25
```

Prix de vente minimum pour une marge cible `M` :

```
prix_min = (prix_achat + M + 0,25) / 0,861
```

Seuils de marge : **20 à 25 €** sur les petites pièces, **100 €** sur les grosses
pièces (proposition : au-delà de 300 € de prix de revente — à confirmer).

## Décision d'achat en vente aux enchères

Le chiffre utile devant une vente n'est pas le prix de revente : c'est
**l'enchère maximale à ne pas dépasser**.

### Les frais acheteur

En maison de vente, le coût réel d'acquisition est l'adjudication **plus les
frais acheteur**, généralement 20 à 30 %. Une adjudication à 100 € coûte 125 €.
Calculer la marge sur l'enchère seule fausse le résultat de 25 % et transforme
une marge de 25 € en perte.

### Formule

```
coût max         = 0,861 × prix_revente − marge_visée − 0,25
enchère maximale = (coût max − frais annexes) / (1 + taux frais acheteur)
```

Exemple, manteau revendable 250 €, frais acheteur 25 %, transport 10 € :

| Étape | Calcul | Résultat |
|-------|--------|----------|
| Coût max d'acquisition | 0,861 × 250 − 25 − 0,25 | **190 €** |
| Enchère max sans transport | 190 / 1,25 | **152 €** |
| Enchère max avec transport | (190 − 10) / 1,25 | **144 €** |

### Informations à réunir avant chaque vente

1. Photo et désignation complète — marque, modèle, taille, état visible
2. Estimation basse et haute annoncée
3. **Taux de frais acheteur** de la maison de vente (dans les conditions de
   vente, variable d'une maison à l'autre)
4. Frais de retrait ou d'expédition du lot

Sortie attendue : prix de revente réaliste, puis enchère maximale pour 20 €,
25 € et 100 € de marge.

Le port n'entre pas dans la formule : il est refacturé au client.

## Doctrine de prix

Stratégie retenue : **vendre moins cher que le moins cher, tout en tenant la
marge plancher.**

Cette stratégie ne se joue pas à la mise en ligne mais **à l'achat**. Avec la
formule ci-dessus, tenir 25 € de marge sous le prix marché suppose d'acheter aux
alentours de **60-65 % du prix marché**. Atteignable en maison de vente, sur des
lots ou en liquidation ; impossible au prix boutique.

Exemple, sur un article dont le prix marché est 140 € :

| Prix d'achat | Prix plancher | Verdict |
|--------------|---------------|---------|
| 89 € | 133 € | sous le marché, marge tenue |
| 110 € | 157 € | au-dessus du marché, invendable |

### Nuance selon l'univers

- **Collection (scellé)** — l'authenticité ne fait aucun doute, le moins cher
  gagne. La stratégie s'applique pleinement.
- **Mode de créateur** — un prix nettement sous le marché éveille le soupçon de
  contrefaçon et fait fuir l'acheteur visé. Ce qui vend ici, c'est la preuve :
  photos des étiquettes, mention de la maison de vente, description précise de
  l'état. Rester dans le marché, pas en dessous.

### Conséquence pour le dashboard (étape 7)

Afficher pour chaque pièce, à partir du prix d'achat saisi :

- le **prix plancher** (marge minimum atteinte) ;
- la **marge réelle** si le prix marché constaté est saisi ;
- un verdict vendable / non vendable à ce prix d'achat.

L'objectif est de trancher à l'achat, avant d'immobiliser de la trésorerie sur
une pièce invendable à la marge visée.
