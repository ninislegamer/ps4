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
- Nécessaire pour développer l'app admin (dashboard marge + génération IA).
- Prévoir une clé API Anthropic pour la génération des titres/descriptions.

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

- **Expédition et livraison** — transporteurs, tarifs, et **limiter les
  livraisons à la France** au démarrage (évite les questions de TVA et de
  douane à l'international).
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
| Génération IA des titres/descriptions | app admin + clé API Anthropic | usage réel |
| Bon de livraison de marque | template imprimable | 0 € |

**Ce qui reste irréductiblement payant :** l'affranchissement des colis et la
consommation de l'API pour la génération IA.

**Étiquettes d'expédition : non générables.** Le code-barres encode un numéro de
suivi réel émis et payé auprès du transporteur ; un fichier fabriqué ne scanne
pas. Comparer **Boxtal** et **Sendcloud** (tarifs Colissimo / Mondial Relay
souvent meilleurs que Shopify Shipping, qui n'est de toute façon pas disponible
partout en France).

**Contrepartie du sur-mesure :** une mise à jour majeure du thème peut casser une
personnalisation, et il n'y a pas de support éditeur derrière. Arbitrage assumé
au volume actuel.

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
| 7 | Dashboard admin | App marge automatique + génération IA des fiches |

---

## Structure des catégories (étape 2)

```
Femme
  ├─ Vêtements
  ├─ Baskets
  └─ Sandales
Homme
  ├─ Vêtements
  ├─ Baskets
  └─ Sandales
Cartes Pokémon
  ├─ Boosters scellés
  └─ Displays scellés
Jouets & Divers
```

Collections transverses : *Nouveautés*, *Pièces rares*, *Neuf avec étiquette*,
*Dernière pièce*.

---

## Règle de marge (étape 7)

Charges micro-entreprise achat-revente : **12,4 %** du chiffre d'affaires
(12,3 % cotisations + 0,1 % formation professionnelle).

```
marge = prix_vente − prix_achat − (0,124 × prix_vente)
      = 0,876 × prix_vente − prix_achat
```

Prix de vente minimum pour une marge cible `M` :

```
prix_min = (prix_achat + M) / 0,876
```

Seuils : `M = 25 €` en standard, `M = 100 €` sur les grosses pièces.

Les frais de paiement (~1,4 % + 0,25 €) et le port ne sont pas inclus dans cette
formule — option à activer dans le dashboard si l'on veut une marge nette réelle.
