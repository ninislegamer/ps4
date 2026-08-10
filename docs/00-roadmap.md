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
| Boîte e-mail contact@maison-nsaia.fr | ✅ créée (Gandi, DKIM+SPF OK) |
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
2. **E-mail expéditeur** → déclarer `contact@maison-nsaia.fr` dans Shopify.
   *Paramètres* → *Détails de la boutique* → e-mail de l'expéditeur.
   Shopify demandera probablement d'ajouter des enregistrements DNS chez Gandi
   pour authentifier le domaine expéditeur. Sans ça, les confirmations de
   commande partent depuis une adresse Shopify générique.
3. **Thème Dawn** → installation et réglages (voir `01-theme.md`).

### À faire dès réception du RIB

4. **Shopify Payments — IBAN.** *Paramètres* → *Paiements* → **Ajouter un
   compte**. Sans ça, l'encaissement fonctionne mais les versements restent
   suspendus.
5. **PayPal Business.** Créer le compte sur paypal.com (possible dès maintenant
   sans RIB : e-mail + SIRET suffisent, le compte bancaire se rattache plus
   tard), puis Shopify → *Paiements* → *Moyens de paiement supplémentaires* →
   PayPal → relier le compte.

Rappel : carte, Apple Pay et Google Pay sont déjà couverts par Shopify Payments.
PayPal est un moyen de paiement supplémentaire, pas un remplacement.

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
