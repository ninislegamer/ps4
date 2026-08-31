# Facture PDF et bon de livraison — Order Printer

*Établi le 31/08/2026.*

Deux templates Liquid prêts à coller dans l'app **Order Printer** (gratuite,
éditeur Shopify) :

- `order-printer-facture.liquid` — la facture légale (mention TVA art. 293 B,
  SIRET, garanties, coordonnées vendeur/acheteur, lignes de commande, totaux).
- `order-printer-bon-livraison.liquid` — le bon de livraison / carte
  d'authenticité à glisser dans le colis (pas de prix, mention d'authenticité,
  rappel du délai de rétractation, espace pour un mot manuscrit).

Même identité visuelle que `exports/facture-2026-001-Aouimeur-Siham.html`
(la facture de la vente en main propre du 9 août), mais templatés avec les
objets Liquid `order` pour se générer automatiquement sur **chaque commande
Shopify**, pas seulement les ventes en main propre.

## Installation

1. Boutique en ligne → Applications → chercher **« Order Printer »** (l'app
   gratuite de Shopify, pas un concurrent payant) → Installer.
2. Dans l'app, ouvrir un modèle de facture existant (ou en créer un nouveau)
   → onglet code → remplacer tout le contenu par celui de
   `order-printer-facture.liquid`.
3. Faire de même pour un second modèle avec
   `order-printer-bon-livraison.liquid`.
4. Tester sur une commande réelle (bouton « Aperçu » dans l'app, sur une
   commande existante) avant d'imprimer pour un vrai envoi.

## Ce qui reste à vérifier après collage

- **Le retrait en main propre** (pas de `shipping_address`) : les deux
  templates basculent sur « Retrait en main propre — 2 rue du Levant,
  31700 Beauzelle ». À confirmer visuellement sur une commande de ce type.
- **Format monétaire** : les templates utilisent le filtre Liquid `money`
  (respecte le format configuré dans Paramètres → Général → Devise). Si
  l'affichage sort bizarre, vérifier ce réglage plutôt que le template.
- **État de la pièce sur le bon de livraison** : lu depuis les tags produit
  (`Neuf avec étiquette` / `Neuf sans étiquette` / `Très bon état`), comme
  les badges de fiche produit. N'affiche rien si aucun de ces tags n'est
  présent — pas bloquant, juste silencieux.

## Pourquoi Order Printer plutôt qu'une autre app

C'est l'app **gratuite et officielle** de Shopify pour ce cas d'usage
(facture, bon de livraison, imprimés de commande) — cohérent avec le principe
du roadmap : zéro abonnement récurrent. Les alternatives payantes du App
Store n'apportent rien ici puisque le template est entièrement personnalisé
à la main.
