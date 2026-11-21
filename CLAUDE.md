# Maison Nsaia — micro-entreprise

Répondre en français.

- Projet de la boutique : `docs/00-roadmap.md`.
- **Comptabilité et état des encaissements : lire d'abord `docs/04-suivi-comptable.md`**
  (trois activités : achat-revente, livraisons Uber, convoyage automobile ;
  trimestres déclarés ; ventes en attente ; règles de tenue).
- **Annonces (Vinted, Leboncoin, eBay, Shopify)** : l'état annoncé est celui du
  bordereau de la maison de vente. « Traces d'essayage » au bordereau =
  « neuf(s) avec traces d'essayage » dans l'annonce, jamais « neuf » seul. Règle détaillée en tête
  de `docs/annonces.md`.
- Registres légaux : `exports/maison-nsaia-registres.xlsx` (livre des recettes,
  registre des achats, objets mobiliers). Toute nouvelle recette s'y inscrit à la
  date d'encaissement, et `docs/04-suivi-comptable.md` est mis à jour en même temps.
- Quand un article est vendu, appliquer la procédure « Procédure à chaque
  vente » de `docs/00-roadmap.md` : stock à 0, tag `Vendu`, retrait du tag
  `Nouveau` et retrait de la collection « Page d'accueil » (À la une) sur
  Shopify, sans attendre qu'on le demande.
- Factures : modèle `exports/facture-2026-001-Aouimeur-Siham.html`,
  numérotation continue sans trou (2026-001, 2026-002, …). Une facture émise ne
  se supprime ni ne se modifie : une vente annulée s'annule par une facture
  d'avoir, dans la même numérotation (ex. avoir 2026-003 sur la facture 2026-002).
