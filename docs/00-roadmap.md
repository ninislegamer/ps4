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
- Vérifier auprès de l'URSSAF (3698) ou de la CCI :
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
| Shopify Payments — versements | 🔄 IBAN pro ajouté le 16/08 (BOURSORAMA, EI IZRI NACIM, compte finissant par 6345) — délai de sécurité standard Shopify après changement de coordonnées bancaires, reprise automatique des versements le **20/08/2026**, rien à faire d'ici là |
| PayPal Business | ⏸️ en attente du rattachement du compte bancaire |
| Boîte e-mail contact@maison-nsaia.fr | ✅ créée (Gandi) |
| E-mail expéditeur Shopify | ✅ authentifié (6 CNAME DKIM) |
| DMARC | ✅ `_dmarc` TXT `v=DMARC1; p=none` |
| Taxes (franchise en base) | ✅ vérifié — 0 %, aucune inscription fiscale |
| Double authentification | ✅ active (SMS) — passer à une appli + codes de secours |
| Forfait | ✅ Basic, promo **1 €/mois jusqu'au 10/11/2026** |
| POS Pro | ✅ désinstallé — essai qui aurait bascule à ~89 €/mois |
| Domaine des comptes clients | ✅ basculé le 16/08 sur compte.maison-nsaia.fr |
| Thème Dawn installé et réglé | ✅ publié le 16/08 — était resté en brouillon, la boutique tournait sur Horizon (thème par défaut) jusque-là. Bannière d'accueil, barre d'annonces (2 messages en rotation), section « Une provenance vérifiée » (titre + texte + bouton « Découvrir mon histoire » relié à la page À propos), newsletter du pied de page traduite, page « À propos » créée (Visible) et ajoutée au menu principal, tout fait le 16/08. |
| Photos produits harmonisées | ⬜ plus tard |
| Système d'avis clients (Judge.me) | ✅ installé le 17/08 — plan gratuit, étoiles + avis en bas de fiche, 2 premiers avis Vinted importés et confirmés par mail (colline_dvl, lillyo456) |
| Collection « Chaussures » | ✅ créée le 17/08 — automatique, catégorie = Chaussures OU Chaussures de sport, 6 articles (4 baskets, 1 randonnée, 1 ballerines). « Vêtements » pas encore ouverte (2 réf. seulement, sous le seuil de 5-6) |
| Collection « Nouveautés » | ✅ créée le 17/08 — automatique, statut = Actif, triée par date de création la plus récente. « Dernière pièce » volontairement pas créée : tout le stock étant déjà à 1 exemplaire, elle ne filtrerait rien — à revoir seulement si des références en plusieurs quantités arrivent (ex. sportswear racheté en lot) |
| Menu principal | ✅ « Chaussures » et « Nouveautés » ajoutés le 17/08, en plus d'Accueil / Catalogue / Contact / À propos |
| Shopify Inbox (chat en direct) | ✅ installé le 17/08 — gratuit, message d'accueil en français, couleurs alignées automatiquement sur la charte |
| Expédition et livraison (France, Europe, retrait sur RDV) | ✅ configuré le 16/08 — voir détail ci-dessous |
| Marché Union européenne | ✅ créé et actif |

À retenir : l'éditeur de thème Shopify est inutilisable confortablement sur
téléphone. Tout le reste de l'admin passe bien en mobile.

### À faire à la prochaine session (sur ordinateur)

1. ~~**URL des comptes clients**~~ ✅ fait le 16/08 — basculé sur
   `compte.maison-nsaia.fr` en domaine principal (il était connecté mais
   configuré en simple redirection).
2. ~~**Thème Dawn**~~ ✅ publié le 16/08, réglages de la bannière d'accueil et
   de la barre d'annonces faits (voir tableau ci-dessus). Reste : finir la
   structure des autres sections de la page d'accueil.
3. **Configurer contact@maison-nsaia.fr sur Outlook** — boîte hébergée chez
   Gandi (webmail.gandi.net). À faire en IMAP/SMTP : demandé le 17/08, pas
   encore fait.

### À faire maintenant que le RIB est là

3. ~~**Shopify Payments — IBAN.**~~ ✅ fait le 16/08 — compte EI IZRI NACIM
   ajouté et confirmé. Les versements ne sont plus suspendus.
4. **PayPal Business — rattacher le compte bancaire.** 🔄 En cours depuis le
   16/08 : IBAN Boursorama saisi sur PayPal (Portefeuille → Comptes
   bancaires et cartes), statut **« Confirmation en attente »** — PayPal a
   envoyé un virement test de 0,01 € à confirmer, qui peut prendre jusqu'à
   1-2 jours ouvrés. **Ne pas retoucher/re-ajouter le compte d'ici là**
   (relancer la demande la remet à zéro). Une fois le centime visible sur le
   relevé Boursorama : revenir dans la même section, cliquer sur
   « Confirmer » et saisir le montant exact. Ensuite seulement, relier
   PayPal à Shopify → *Paiements* → *Moyens de paiement supplémentaires* →
   PayPal, **en second moyen de paiement** (Shopify Payments reste le
   principal — commission PayPal environ le double de Shopify Payments).
   Point mineur à corriger à l'occasion : le nom d'entreprise sur PayPal est
   affiché « Nsaia », à harmoniser en « Maison Nsaia ».

Rappel : carte, Apple Pay et Google Pay sont déjà couverts par Shopify Payments.
PayPal est un moyen de paiement supplémentaire, pas un remplacement.

### À faire avant l'ouverture de la boutique

- ~~**Expédition et livraison**~~ ✅ fait le 16/08 : zone France (Colissimo
  domicile 8,90 €, 2-5 jours ouvrables ; Mondial Relay point relais 5,90 €,
  3-5 jours ouvrables), zone Europe (Livraison suivi 16,90 €, 5-8 jours
  ouvrables, marché Union européenne créé et actif — 26 pays vendables),
  Retrait en magasin gratuit sur rendez-vous (2 rue du Levant, 31700
  Beauzelle). Pas d'agrégateur (Boxtal/Sendcloud) pour l'instant — tarifs
  forfaitaires manuels, à reconsidérer si le volume d'envois augmente.
- ~~**Confidentialité des clients**~~ ✅ vérifié le 16/08 — déjà entièrement
  automatisé par Shopify : politique de confidentialité publiée, bandeau
  cookies actif sur toute l'UE, page d'opposition au partage de données non
  requise pour nos zones de vente. Rien à configurer manuellement.
- ~~**Politiques**~~ ✅ fait le 16/08 — Coordonnées, Mention légale,
  Politique de retour, Politique d'expédition, Conditions de service et
  Politique de confidentialité tous publiés. **Conditions de vente
  publiées avec une réserve** : la section 9 (médiateur de la consommation,
  obligatoire art. L616-1 du code de la consommation) est encore un
  placeholder « à compléter ». Aucun médiateur choisi ni inscription faite
  — reporté volontairement à plus tard. **Ne pas considérer la boutique
  ouvrable tant que cette section n'est pas complétée et republiée.**

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
le seuil de franchise est dépassé — auprès de l'URSSAF ou de la CCI.

---

## Ce qui sera codé plutôt qu'acheté

Objectif : aucun abonnement d'application récurrent.

| Fonction | Solution retenue | Coût |
|----------|------------------|------|
| Facture PDF avec mention art. 293 B | Order Printer (gratuit) + template Liquid sur mesure | 0 € |
| Favoris / wishlist | code thème + métachamps client | 0 € |
| Badges « 100 % Authentique », « Neuf avec étiquette », « Origine vérifiée en maison de vente » | Liquid sur la fiche produit | 0 € |
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

**Deux lignes de clôture systématiques**, sur chaque fiche, en plus de la
description propre à la pièce :

```
Pièce authentifiée en maison de vente. Un seul exemplaire disponible.

Vendu par un professionnel : garanties légales de conformité et contre
les vices cachés applicables. Détail dans les conditions générales de vente.
```

Mesures réelles (épaules/poitrine/longueur sur un vêtement, longueur de semelle
intérieure sur une chaussure) : à ajouter dès que la pièce est sous la main —
non bloquant, laissé de côté tant que le stock n'est pas physiquement disponible
pour mesurer. **Première fiche mise à jour avec les deux lignes : adidas x
Stella McCartney — ASMC Ultraboost 21 Metallic — 36, le 16/08.**

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

**Refacturés au client, jamais absorbés par la marge. Sans exception**, y compris
sur les produits standardisés dont les concurrents annoncent la livraison
gratuite. Si la comparaison devient défavorable, c'est le **prix affiché** qu'on
baisse, jamais la marge qu'on ampute.

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

**Compter six à douze mois avant que `maison-nsaia.fr` apparaisse dans les
résultats**, quoi qu'on fasse sur les prix. Les six premiers mois, le trafic
viendra de **Leboncoin, Vinted et eBay** — ils ont déjà l'audience. C'est
d'ailleurs là que s'est faite la première vente.

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

## Vente multicanale et stock unitaire

Chaque article existe en un seul exemplaire. Le vendre simultanément sur
plusieurs canaux crée un risque de double vente, et aucune synchronisation
automatique n'existe entre Shopify, Leboncoin et Reverb.

### Règle : un seul canal en achat immédiat

- **Shopify est la source de vérité.** Stock à 1, retrait automatique de la fiche
  à l'épuisement (étape 4, Shopify Flow). La deuxième commande est bloquée.
- **Leboncoin** : désactiver le paiement sécurisé et la livraison intégrée.
  L'acheteur passe par message, la disponibilité est vérifiée avant de conclure.
- **Reverb** : fonctionne en achat immédiat. Sur un article à forte valeur,
  choisir entre Reverb et l'achat direct sur la boutique — pas les deux. La fiche
  Shopify peut rester en ligne en « nous contacter ».

### Réflexe

Dès qu'une vente est conclue quelque part, **supprimer les autres annonces avant
d'emballer**, jamais après.

### Si une double vente survient

Rembourser immédiatement et intégralement, avec un message honnête. Priorité au
premier arrivé, sauf si la commande marketplace est déjà payée : une annulation
sur Reverb affecte la note vendeur, un remboursement sur la boutique ne laisse
aucune trace publique.

### Pourquoi les places de marché dès le lancement

Une boutique neuve n'a aucun trafic et aucun historique ; un achat à plusieurs
centaines d'euros chez un vendeur inconnu se heurte à un problème de confiance.
Le site construit la marque, les places de marché font tourner la trésorerie. Au
démarrage, la **rotation prime sur la marge** : 470 € encaissés en trois semaines
valent mieux que 780 € en six mois, car le capital retourne au sourcing.

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

### À vérifier auprès de l'URSSAF ou de la CCI avant la phase 2

Sous le régime de la **franchise en base**, aucune TVA n'est collectée. Les
ventes à des particuliers dans d'autres pays de l'UE sont soumises à un **seuil
annuel de l'ordre de 10 000 €** de ventes transfrontalières, au-delà duquel
l'enregistrement au guichet **OSS** et l'application de la TVA du pays du client
entrent en jeu. L'articulation exacte avec la franchise en base relève du
l'URSSAF — à poser en même temps que la question des seuils (voir 0.1).

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

## Où vérifier — pas de comptable, c'est normal

En micro-entreprise il n'y a **ni bilan, ni compte de résultat, ni
expert-comptable obligatoire**. La comptabilité est tenue soi-même.

| Question | Où |
|----------|-----|
| Cotisations, taux, déclarations | **autoentrepreneur.urssaf.fr** · tél. **3698** |
| Obligations légales d'un commerçant | **entreprendre.service-public.fr** |
| CGV, rétractation, information du consommateur | **DGCCRF** — `economie.gouv.fr/dgccrf` |
| Liste des médiateurs agréés | **CECMC**, sur `economie.gouv.fr` |
| Impôt, abattement, déclaration | **impots.gouv.fr** |

Et le plus utile, souvent oublié : **la Chambre de Commerce et d'Industrie**. Les
conseillers CCI reçoivent gratuitement les commerçants et répondent précisément
sur les CGV, les registres et les obligations. Un rendez-vous vaut mieux que dix
heures de recherche.

### Les trois registres obligatoires

| Registre | Obligation |
|----------|-----------|
| **Livre des recettes** | toute micro-entreprise — date, client, montant, mode de paiement |
| **Registre des achats** | dès qu'il y a achat-revente — les factures des maisons de vente y vont |
| **Registre des objets mobiliers** | achat-revente de biens d'occasion, art. 321-7 du code pénal — tenue numérique admise depuis 2020 |

**Classeur dédié : `exports/maison-nsaia-registres.xlsx`.** Quatre feuilles —
mode d'emploi, livre des recettes, registre des achats, objets mobiliers. 300
lignes vierges prêtes, numérotation automatique, et le total du CA encaissé avec
l'URSSAF à provisionner affichés en tête du livre des recettes.

Il est **séparé du classeur de stock** volontairement : le stock change tous les
jours, les registres sont des documents à écriture continue qu'on ne réordonne
jamais.

### Règles de tenue

- **Ordre chronologique**, au fil de l'eau.
- **Jamais de suppression ni de réordonnancement.** Une erreur se corrige par une
  ligne rectificative, pas par un effacement.
- **Numérotation continue**, sans rupture — elle se calcule seule dès qu'une date
  est saisie.
- **Conservation 5 ans**, factures des maisons de vente comprises : elles
  justifient chaque ligne.

### Ce qu'on déclare à l'URSSAF

Le chiffre d'affaires **encaissé** sur la période, pas facturé. Une vente de
décembre encaissée en janvier se déclare en janvier.

---

## Avant tout le reste : cinq chantiers, dans cet ordre

Ces cinq points priment sur le logo, les couleurs et la personnalisation du
thème. **Un beau site vide ne vend rien ; un site simple avec 18 fiches
irréprochables, oui.**

| Ordre | Chantier | Temps |
|-------|----------|-------|
| **1** | Les pages légales — bloquant | 1 h |
| **2** | Les photos des 18 pièces | une demi-journée |
| **3** | Les mesures réelles, en même temps que les photos | 30 s par pièce |
| **4** | La page « À propos » | 20 min |
| **5** | La mention « 1 exemplaire disponible » | 5 min |

### 1. Les pages légales — c'est bloquant

CGV, mentions légales, politique de confidentialité, politique de retour et de
remboursement.

Sans elles, **la vente est illégale** et **Google Merchant Center refuse le
compte** — donc pas de Google Shopping, qui est pourtant la seule voie de trafic
gratuit à court terme.

Shopify génère des modèles dans **Paramètres → Politiques**. À adapter avec le
SIRET et la mention « TVA non applicable, art. 293 B du CGI ».

### 2. La photographie est le produit

Sur une boutique de pièces uniques, **les photos ne sont pas l'illustration du
produit, elles sont le produit**. Le client n'essaie pas, ne touche pas. Il n'a
que ça.

Un thème parfait avec des photos moyennes fait un site amateur. Un thème basique
avec des photos rigoureuses fait un site sérieux. C'est le seul investissement
dont le rendement est certain à ce stade.

Protocole à tenir sur les 18 pièces **sans exception** :

- **Un seul fond, un seul éclairage, un seul cadrage.** La cohérence entre les
  fiches vaut plus que la beauté de chacune.
- Lumière du jour, près d'une fenêtre, jamais de flash.
- **Cinq vues par pièce** : face, dos, détail matière, **étiquette de marque**,
  **étiquette de taille**.
- Sur le neuf, l'étiquette en gros plan justifie le prix mieux qu'un paragraphe.

### 3. Les mesures réelles sur chaque fiche

Presque personne ne le fait, et c'est ce qui tue les ventes de vêtements en
ligne.

Mesurer à plat et publier : **épaules, poitrine, taille, longueur** sur un
vêtement ; **longueur de semelle intérieure** sur une chaussure.

```
Mesures à plat
Épaules 40 cm · Poitrine 48 cm · Longueur 92 cm
```

Deux effets : la **conversion monte** — l'acheteuse hésitante achète quand elle
peut comparer avec un vêtement qu'elle possède — et les **retours s'effondrent**.
Sur une pièce unique, un retour est une vente perdue et un article à
reconditionner.

Trente secondes par pièce avec un mètre de couturière.

### 4. Une page « À propos » qui dit d'où viennent les pièces

C'est le **seul avantage concurrentiel réel**, et il est enterré dans les fiches
produit.

La plupart des revendeurs ne peuvent pas dire d'où vient leur marchandise. Ici
si : maisons de vente, avec facture, et un opérateur **légalement responsable de
l'authenticité**. C'est un argument que Vinted ne peut pas offrir.

Cinq lignes, à la première personne, sur une vraie page — **sans jamais nommer
les maisons de vente**.

### 5. « 1 exemplaire disponible » sur chaque fiche

Toutes les boutiques fabriquent une fausse urgence. Celle-ci est vraie : il y a
réellement un exemplaire de chaque chose.

À afficher en clair sous le prix. Pas de compte à rebours, pas de « plus que 2 en
stock » : juste le fait.

```
Pièce unique — 1 exemplaire disponible
```

C'est honnête, c'est rare, et c'est ce qui fait qu'on n'attend pas les soldes.

---

## Structure des catégories (étape 2)

**Un seul univers : la mode.** Les cartes Pokémon, boosters et displays sortent
du périmètre. Les produits déjà en ligne qui en relèvent (cartes, Beyblade) sont
à dépublier lors de cette étape.

Navigation principale par genre et catégorie — c'est ainsi qu'un client cherche
un vêtement. Les niveaux de gamme sont des **sélections**, pas des rayons : ils
se croisent avec les catégories au lieu de les dupliquer.

### La règle d'ouverture : cinq références minimum

**Une catégorie ne s'ouvre qu'à partir de cinq ou six références.** Une catégorie
vide, ou à deux articles, fait plus de mal qu'une catégorie absente : elle
signale un magasin qui ne tient pas ses promesses.

On part donc étroit et on élargit au fil du stock. **Chaque rayon nouveau doit
être justifié par le stock existant, jamais par une intention.**

### Structure au lancement — 18 références

```
BOUTIQUE
├─ Vêtements       7 réf.  Elisabetta Franchi · Sonia Rykiel · Karl Lagerfeld
│                          Sandro · Chiara Ferragni · Pier Antonio Gaspari · ba&sh
└─ Chaussures     11 réf.  Hogan · adidas by Stella McCartney · Forma Legacy
                           Massimo Dutti · New Balance BB80 · New Balance 650
                           New Balance GS 1906 · Tommy Jeans · Emporio Armani
                           Geox · Plein Sport

SÉLECTIONS (collections automatiques, pas des rayons)
├─ Nouveautés
└─ Dernière pièce
```

Pas de séparation Femme / Homme au départ : deux références homme ne justifient
pas un rayon. Elle s'ouvrira à cinq références masculines.

### Le sportswear a une fonction : faire entrer du monde

Les New Balance, Tommy Jeans, Emporio Armani et Geox ont une marge quasi nulle —
0,97 € à 4,64 €. Ce n'est pas leur rôle. Leur rôle est celui qui était déjà écrit
dans le tableau des niveaux de gamme : **acquisition, produits connus, panier
d'entrée**.

Quelqu'un tape « New Balance 650 » dans une barre de recherche et tombe sur la
fiche. Personne ne tape « Pier Antonio Gaspari ». **Le sportswear amène le
trafic, les créateurs font la marge.**

La commission carte de 1,5 % coûte ~1 € sur ces fiches, soit l'essentiel de leur
marge. C'est le meilleur euro de publicité de la boutique : il paie un visiteur
qui découvre le reste du catalogue.

### Plancher de prix boutique : 49 €

En dessous, places de marché. Cette règle exclut proprement les Morgan (12-19 €),
les Mrs.Ertha (19 €), les Havaianas (13,90 €) et les pompes Robby (42 €) sans
avoir à arbitrer au cas par cas.

Le catalogue tient ainsi dans une bande de **49 à 159 €**, cohérente. Ce qui
cassait le positionnement n'était pas le sportswear — c'étaient les articles à
moins de 20 €.

### Une fiche vendue ne se supprime jamais

**Le stock passe à zéro, la fiche reste en ligne avec la mention « Vendue ».**
C'est ce que font les maisons de vente avec leurs résultats, et ça sert trois
choses :

1. **Le site n'est jamais vide.** 18 pièces en vente plus 20 vendues font un
   catalogue de 38 fiches.
2. **Ça prouve que la boutique fonctionne.** Un visiteur qui voit des pièces
   vendues sait qu'il n'est pas le premier client.
3. **Ça montre ce qui est sourcé.** Quelqu'un qui cherche du Sonia Rykiel et voit
   qu'il y en a déjà eu revient à la prochaine.

Ajouter un bouton **« Prévenez-moi des pièces similaires »** sur les fiches
vendues : il alimente la liste de diffusion. C'est la seule chose qui transforme
une archive en actif — quelqu'un tombe sur une pièce vendue, laisse son adresse,
et devient un client pour la suivante.

**C'est probablement ce que la boutique fera de mieux la première année** — pas
vendre, mais collecter les adresses de gens qui ont vu des pièces qu'ils auraient
voulues.

### Photographier à réception, pas au moment de vendre

**Une pièce partie ne se photographie plus.** Attendre la vente pour faire les
photos, c'est perdre la fiche définitivement.

Réflexe à prendre : **un colis arrive → tout est photographié immédiatement**,
avant même de décider du canal. Cinq vues, même protocole, même fond. Cela vaut
aussi pour ce qui part à la famille : on photographie, puis on donne.

### Le prix affiché sur une fiche vendue

| Cas | Ce qu'on affiche |
|-----|------------------|
| Vendue **au prix de la fiche** | le prix, avec la mention « Vendue » |
| Vendue **hors marché** — famille, sans bénéfice | **« Vendue », sans prix** |

Afficher 99 € sur une pièce partie à 40 € donne une fausse idée du niveau de
prix, et la crédibilité n'y survit pas si quelqu'un le découvre. Les maisons de
vente font de même : quand un lot part hors adjudication, elles publient le
résultat, pas un chiffre inventé.

**Rappel comptable : une vente sans bénéfice reste du chiffre d'affaires.** Le
livre des recettes ne distingue pas une vente à la famille d'une vente à un
inconnu — 40 € encaissés, c'est 40 € déclarés et 4,96 € d'URSSAF.

### Cumuler boutique et places de marché sans double vente

Le seul risque est de vendre deux fois le même article. Il n'existe que sur les
canaux à **achat immédiat non désactivable**.

| Canal | Achat immédiat | Cumulable avec la boutique |
|-------|----------------|----------------------------|
| **Leboncoin** sans paiement sécurisé | non — l'acheteur contacte | **oui, sans risque** |
| Leboncoin avec paiement sécurisé | oui | non |
| **Vinted** | oui, non désactivable | **non** |
| **eBay** | oui | non |

**Règle : Vinted et eBay sont réservés aux pièces qui ne sont pas sur la
boutique.** Tout le reste va sur la boutique **et** sur Leboncoin sans paiement
sécurisé.

### La boutique est la source de vérité

Le danger du double affichage n'est pas la fiche, c'est le **décalage**. Une
pièce vendue sur Leboncoin à 14h et mise à jour le lendemain peut être achetée et
payée entre-temps sur la boutique. Il faut alors annuler et rembourser — mauvaise
expérience, et les annulations répétées pénalisent un compte Shopify Payments.

> **Dès qu'un acheteur Leboncoin dit oui, premier geste : stock à 0 sur Shopify.
> Ensuite seulement, confirmer à l'acheteur.** Jamais l'inverse.

C'est ce qui rend le double affichage totalement sûr, et c'est possible parce que
Leboncoin est **sans paiement sécurisé** : la vente passe par une conversation,
il y a toujours le temps de faire la manœuvre. Sur Vinted et eBay, l'acheteur
paie sans prévenir — d'où leur exclusion des pièces de boutique.

### Deux états plutôt qu'un

| Moment | Fiche boutique |
|--------|----------------|
| L'acheteur Leboncoin dit « je le prends » | **Réservée** — stock à 0 |
| Il a payé et récupéré | **Vendue** |

Un désistement — fréquent sur Leboncoin — se règle en remettant le stock à 1.
Rien n'est perdu.

### La manœuvre, sur Shopify

1. **Stock à 0**, et vérifier que « Continuer la vente en rupture de stock » est
   **désactivé**
2. **Ne pas dépublier, ne pas supprimer** — l'URL reste vivante et Google
   continue de l'indexer
3. Shopify affiche « Épuisé » par défaut : **remplacer ce mot par « Vendue »**
   dans les traductions du thème

Trente secondes par vente.

### Structure cible, à mesure que le stock grossit

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

### Élargissement hors mode : différé, pas exclu

La question s'est posée d'ouvrir la boutique à tout ce qui est sourcé en vente
aux enchères — son et image, maison et jardin, collection — parce que les pièces
de créateurs sont rares : **sur une vingtaine de lots examinés le 12 août, un
seul passait les quatre filtres**, et 19 des 27 lignes du stock ne rentrent dans
aucun rayon actuel.

**Décision : différé.** On n'ouvre pas de rayon pour du stock qu'on n'a pas
encore. Les pompes Robby, les tongs, les New Balance et les Morgan se vendent sur
Leboncoin, Vinted et eBay.

Si l'élargissement se fait un jour, il devra changer le principe organisateur du
site : ce qui unit les articles ne sera plus le **niveau de gamme** mais la
**provenance et le prix** — « des pièces sourcées en maison de vente, vérifiées,
vendues sous leur prix de marché ». Cette phrase couvre une robe YSL comme une
pompe. Elle transforme la boutique en **maison de vente en ligne** plutôt qu'en
boutique de luxe, ce qui est plus proche de la réalité de l'activité.

Quatre conditions si cela se fait :

1. Jamais de mélange de prix sur une même page — les rayons restent étanches.
2. La page d'accueil montre le haut du panier et donne le ton.
3. Une seule charte photo pour tout, de la robe à la pompe. C'est elle qui tient
   visuellement un site généraliste.
4. La mention de provenance sur chaque fiche, sans exception.

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

**Neuf uniquement, acheté en vente aux enchères** (liquidation, invendus,
redressement judiciaire). Jamais d'occasion sur cette famille : l'occasion est
réservée aux pièces de créateurs.

L'objection habituelle — impossible de battre Thomann ou Amazon sur du neuf —
tombe dès lors que l'acquisition se fait sous le prix de gros. C'est le seul
angle qui rend la stratégie de prix bas applicable sur des produits comparables :
neuf, code-barres, référencé sur Google Shopping, et moins cher parce que le
coût d'entrée est plus bas, pas parce que la marge est sacrifiée.

Contraintes propres à cette famille de produits :

- **Garantie légale de conformité de 2 ans**, portée par le vendeur. Sur du
  matériel acheté en liquidation, aucun recours vers la marque faute d'être
  revendeur agréé : une panne au bout de quatorze mois est à la charge de la
  boutique.
- **Port** : lourd et fragile, 20-30 € d'expédition et assurance obligatoire. Un
  colis cassé efface la marge de plusieurs ventes.
- **Retour** : 14 jours de rétractation sur une pièce à plusieurs centaines
  d'euros, qui peut revenir abîmée.
- **État déclaré** : neuf réel ou ex-démonstration. Un carton ouvert interdit la
  mention « neuf », sur la fiche comme sur Google Shopping.
- **Origine du stock** : liquidation, retours clients ou import parallèle — cela
  détermine ce qui peut être affirmé.

### Seuil de marge sur les articles à forte valeur

Un seuil fixe perd son sens quand la valeur monte : 100 € sur un manteau à 400 €
représentent 25 %, contre 6 % sur une platine à 1 700 € — où une seule panne sous
garantie efface la marge de cinq ventes.

**Au-delà de 1 000 € de prix de revente, viser 12 à 15 % de marge** plutôt qu'un
montant fixe.

Deux points juridiques s'appliqueront :

- **Garantie légale de conformité de 2 ans** sur le neuf vendu par un
  professionnel, contre 12 mois sur l'occasion — sensible sur de l'électronique.
- **Éco-participation (DEEE)** sur les équipements électriques et électroniques,
  à vérifier auprès de la CCI en cas d'import de neuf.

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

---

## Les charges fixes : ce que la boutique coûte avant d'avoir vendu

| Poste | Aujourd'hui | À partir du 11/11/2026 |
|-------|-------------|------------------------|
| Abonnement Shopify | 1 €/mois | **36 €/mois** |
| Abonnement Claude | 22 €/mois | 22 €/mois |
| **Total** | **23 €/mois** | **58 €/mois — 696 €/an** |

Et à partir de 2027, la **CFE** s'ajoute : exonérée la première année, puis 200 à
600 €/an selon la commune. Soit un plancher réaliste de **900 €/an** en 2027.

### Le chiffre qui compte : le CA minimum

Le stock restant représente **2 424 € de chiffre d'affaires attendu** pour
**679 € de marge nette** après URSSAF, carte, emballage et impôt. Soit un taux de
marge nette de **28 % du CA**.

À ce taux :

| | Charges | **CA mensuel nécessaire** |
|---|---|---|
| Aujourd'hui | 23 €/mois | **82 €** |
| À partir du 11/11/2026 | 58 €/mois | **207 €** |

**207 € de ventes par mois, c'est le seuil de survie de la boutique** à partir de
novembre. En dessous, l'activité coûte de l'argent même quand elle vend.

Ramené à ton stock : sur les 40 lots restants, il faut en écouler l'équivalent de
**deux articles moyens par mois** pour rester à l'équilibre. C'est atteignable —
mais ça suppose de publier, pas de sourcer.

### Ce que tout le stock couvre

Les 679 € de marge du stock entier couvrent **11,7 mois** de charges au tarif de
novembre. Autrement dit : **tout ce que tu as en cartons paie à peine un an
d'abonnements.**

Ce n'est pas un problème de marge, c'est un problème d'échelle. Deux sorties
possibles :

1. **Vendre plus vite** — la marge est déjà là, elle attend d'être publiée.
2. **Réduire la charge** — à 36 €/mois, Shopify n'est justifié que si la boutique
   apporte des ventes que Leboncoin n'apporte pas. À vérifier en novembre, chiffres
   en main : si la boutique n'a rien vendu en propre d'ici là, la question se pose
   honnêtement.

**Le rappel du 10 novembre 2026 doit être posé maintenant**, pas découvert sur un
relevé bancaire en décembre.

---

# Passer en professionnel sur les plateformes

*Décidé le 14/08/2026. À exécuter sur deux semaines, pas en une soirée.*

## Pourquoi ce n'est pas optionnel

Se présenter comme un particulier quand on est immatriculé est une **pratique
commerciale trompeuse** — l'article L121-4 11° du code de la consommation vise
expressément le fait de « se présenter faussement comme un consommateur ».

Le vrai enjeu n'est pas l'amende, c'est ce que ça retire à l'acheteur : la
**garantie légale de conformité** et le **droit de rétractation de 14 jours** en
vente à distance. C'est ça que la loi protège.

Et l'anonymat est déjà illusoire : **Vinted et eBay déclarent leurs vendeurs au
fisc** au-delà de 30 ventes ou 2 000 € par an (directive DAC7). Le relevé annuel
de janvier 2027 portera le nom de l'exploitant.

Le risque concret n'est pas le procureur, c'est l'acheteur : celui qui découvre le
statut peut exiger rétroactivement la rétractation et la garantie. Les plateformes
tranchent en faveur de l'acheteur.

## La règle qui décide de tout : le taux de marge

**Une commission se calcule sur le prix. Une marge se calcule sur le coût.** C'est
tout le problème : un article cher à faible marge paie une grosse commission sur
une petite marge.

```
taux de marge = marge ÷ prix de vente
```

| Canal | Commission | **Taux de marge minimum** |
|-------|-----------|---------------------------|
| Boutique, remise en main propre | 0 % | aucun |
| Leboncoin sans paiement sécurisé | 0 % | aucun |
| **Vinted Pro** | 5 % + 0,30 € | **5,5 %** |
| **eBay pro** | ~12 % + 0,35 € | **13 %** |

Appliqué au stock actuel : **27 lots sur 30 supportent Vinted Pro, 22 seulement
supportent eBay.**

### Les huit lots que eBay ferait passer en perte

| Taux de marge | Marge | Prix | Lot |
|---------------|-------|------|-----|
| 3,3 % | +2,17 € | 65 € | Tommy Jeans baskets basses P.40 |
| 4,5 % | +2,22 € | 49 € | Beyblade lot n°299 |
| 5,3 % | +3,45 € | 65 € | New Balance montantes P.44 |
| 6,8 % | +2,37 € | 35 € | Pompe Robby ligne 122 |
| 7,8 % | +3,52 € | 45 € | Pompe Robby ligne 84 |
| 8,8 % | +8,76 € | 99 € | New Balance GS 1906 |
| 10,1 % | +6,96 € | 69 € | Emporio Armani P.36 |
| 12,2 % | +6,60 € | 54 € | New Balance P.38 |

Sur eBay, la Tommy Jeans à 65 € rapporterait **−5,98 €**. Ces huit lots vont sur
**Leboncoin en main propre ou sur la boutique**, jamais sur eBay.

C'est cohérent avec ce qu'ils sont : ce sont précisément les lots achetés trop
près du prix du marché, ceux que la règle des deux tiers aurait écartés.

## L'ordre des opérations

### 0. Ne rien supprimer avant l'encaissement de la Salomon

Une transaction en cours sur un compte qu'on ferme, c'est l'argent qui se bloque.
**100 € sont derrière.** Attendre la validation de réception par le client italien.

> **Fait le 14/08.** Colis déposé en locker Mondial Relay, cinq jours avant
> l'échéance du 19 août 20h12. Reste à attendre la livraison et la validation :
> tant que le virement n'est pas arrivé, **la Salomon n'entre pas au livre des
> recettes**. Conserver la preuve de dépôt jusqu'à l'encaissement — c'est la seule
> défense si le client déclare une non-réception.

### 1. eBay en professionnel — cette semaine

Gratuit, aucune contrepartie, aucune ambiguïté. C'est le geste qui sort du risque
le plus vite pour le moins cher. À faire en premier.

**Et republier seulement les 22 lots au-dessus de 13 % de taux de marge.**

### 2. Vinted — vérifier avant de basculer

Les CGU de Vinted Pro réservent la plateforme à la **revente de seconde main par
des professionnels**. Le périmètre autorisé inclut cependant « les retours
boutique, les fins de série déstockées par un professionnel » — **c'est exactement
la nature d'un lot racheté en maison de vente**.

Ce qui est exclu, c'est de vendre du neuf comme le ferait un magasin :
approvisionnement en gros chez une marque, ou créations fabriquées par le vendeur.

**À faire avant de basculer :**

1. Lire `vinted.fr/pro-guide`, la source officielle.
2. Si le texte reste ambigu, **écrire au support Vinted et garder la réponse** :
   *« je rachète des lots de déstockage et de retours boutique en maison de vente
   aux enchères, articles parfois neufs avec étiquette — sont-ils admis sur un
   compte Pro ? »*

Une réponse écrite protège en cas de retrait d'annonces sur signalement. Deux jours
d'attente contre le risque de perdre un compte qui a déjà fait trois ventes.

### 3. Leboncoin — attendre

L'offre Pro démarre à environ **29 €/mois**. Elle ferait passer les charges fixes
de 58 à 87 €/mois à partir de novembre, soit **312 € de chiffre d'affaires mensuel
nécessaire** pour être à l'équilibre, au taux de marge nette de 27,9 %.

Ce n'est pas le volume actuel — 343 € en trois semaines. **À reconsidérer quand le
chiffre mensuel dépasse 400 €**, pas avant.

D'ici là : vérifier s'il existe une déclaration de statut professionnel gratuite ou
à l'annonce dans la catégorie mode. C'est l'obligation légale, et elle est distincte
de l'abonnement payant.

### 4. La boutique devient le canal propre par construction

Mentions légales, SIRET, CGV, garantie, rétractation : tout y est déjà conforme, et
il n'y a **aucune commission**.

**Ça change la décision du 10 novembre.** Les 36 €/mois de Shopify ne sont plus un
coût de vitrine : c'est le seul canal où l'on est en règle sans rien reverser.
Comparé à 29 €/mois de Leboncoin Pro plus 5 % de Vinted plus 12 % d'eBay, la
boutique devient l'option la moins chère, pas la plus chère.

## PayPal Business — ce que ça change, et ce que ça ne change pas

*Compte créé le 14/08/2026.*

### Ce que c'est, et ce que ce n'est pas

PayPal Business est un **compte de paiement**, pas un compte bancaire. Il ne
remplace pas le compte professionnel : l'obligation de compte dédié ne se
déclenche qu'au-dessus de **10 000 € de chiffre d'affaires deux années de suite**
— on en est loin — mais l'argent qui dort chez PayPal n'est pas de la trésorerie
disponible. **Virer le solde sur le compte pro régulièrement**, pas une fois par
trimestre.

### Le piège, c'est le même que sur Vinted

**L'URSSAF se calcule sur le montant payé par le client, pas sur ce que PayPal
verse.**

Un client paie 89 €, PayPal en crédite ~86 € : le chiffre d'affaires déclaré est
**89 €**, et les cotisations se calculent sur 89 €. Les 3 € de commission ne se
déduisent nulle part — en micro-entreprise, **aucune charge n'est déductible**.
Ils sortent directement de la marge.

Au livre des recettes : montant brut, mode de règlement « PayPal », référence de
la transaction. La commission n'est pas une ligne du registre.

### Le coût réel, à relever sur ton propre compte

Les sources publiques se contredisent — de 2,29 % à 3,49 %, et de 0,25 € à 0,49 €
de frais fixe selon les pages. **Aucune n'est fiable pour ton contrat.** Le seul
chiffre qui compte est dans ton espace : *Paramètres → Frais marchands*.

Relève-le et reporte-le dans l'onglet **Paramètres** du classeur, lignes 39 à 41
— elles sont en jaune, prêtes à recevoir le vrai taux.

| Canal | Taux | Frais fixe | Coefficient de marge |
|-------|------|------------|----------------------|
| **Main propre, espèces** | 0 % | 0 € | **0,876** |
| **Vinted** (compte particulier) | 0 % | 0 € | **0,876** |
| **Shopify Payments** | 1,5 % | 0,25 € | **0,861** |
| **PayPal** | ~2,9 % *(à confirmer)* | ~0,35 € *(à confirmer)* | **~0,847** |

**PayPal coûte environ deux fois Shopify Payments.** Sur une vente à 89 €, l'écart
est de ~1,35 € ; sur quarante ventes, une soixantaine d'euros — l'équivalent d'un
mois de charges fixes.

### Donc : deuxième bouton, pas premier

La bonne configuration sur la boutique est **Shopify Payments en principal,
PayPal en second**. L'écart de commission est réel, mais il ne se compare pas à
une vente perdue : certains acheteurs ne saisissent pas leur carte sur une
boutique qu'ils ne connaissent pas et paieront par PayPal, ou pas du tout. 1,35 €
de commission en plus vaut mieux que 89 € de vente en moins.

Là où PayPal gagne vraiment sa commission :

- **les pièces à plus de 100 €**, où la protection acheteur lève l'hésitation —
  Forma 159 €, BMW 139 €, Yeezy 105 € ;
- **l'international**, où c'est souvent le seul moyen de paiement partagé.
  Attention : un supplément s'applique hors zone euro, à relever aussi.

### Deux règles à ne jamais enfreindre

**Jamais de paiement « entre proches ».** Un acheteur proposera d'envoyer les
fonds en *friends and family* pour éviter les frais. C'est une transaction
commerciale déguisée : **aucune protection vendeur**, et PayPal peut restreindre
le compte. Sur une vente professionnelle, c'est aussi une opération dissimulée.
Refuser, sans exception.

**Le compte est au nom de l'entreprise.** Enseigne Maison Nsaia, SIRET
804 431 799 00027 — les mêmes coordonnées que sur les factures et les mentions
légales. Un compte au nom personnel qui encaisse des ventes professionnelles
rouvre exactement le problème qu'on est en train de fermer sur eBay et Vinted.

### À faire cette semaine

- [ ] Relever le taux exact dans *Paramètres → Frais marchands* et le reporter
      dans le classeur
- [ ] Vérifier que la raison sociale, le SIRET et l'adresse du compte
      correspondent aux mentions légales
- [ ] Brancher PayPal sur Shopify **en second moyen de paiement**
- [ ] Programmer un virement du solde PayPal vers le compte pro, au minimum
      mensuel
- [ ] Ajouter « PayPal » aux modes de règlement du livre des recettes

## Les ventes déjà faites

**Rien à rattraper.** Le fond est propre : huit ventes déclarées, URSSAF
provisionnée, trois registres tenus, facture n° 2026-001 émise. C'est la forme du
compte qui était fausse, et elle ne se corrige pas rétroactivement.

La seule chose à faire est d'arrêter la pratique.
