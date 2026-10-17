#!/usr/bin/env python3
"""Génère une vidéo verticale (1080x1920, MP4) des articles en vente pour TikTok et Snapchat.

Usage :
    python3 video/generer_video.py                  # télécharge les photos depuis Shopify
    python3 video/generer_video.py --photos DOSSIER # utilise des photos locales (01.jpg, 02.png… dans l'ordre de produits.json)

Sortie : exports/maison-nsaia-tiktok.mp4
"""
import argparse
import io
import json
import subprocess
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

RACINE = Path(__file__).resolve().parent.parent
PRODUITS = Path(__file__).resolve().parent / "produits.json"
SORTIE = RACINE / "exports" / "maison-nsaia-tiktok.mp4"

L, H, FPS = 1080, 1920, 30
DUREE_INTRO, DUREE_ARTICLE, DUREE_OUTRO, FONDU = 2.0, 2.6, 3.0, 0.35

# Couleurs du thème (docs/01-theme.md)
FOND = (250, 249, 247)
TEXTE = (26, 26, 26)
GRIS = (110, 110, 110)

SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_GRAS = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SANS = "/usr/share/fonts/opentype/inter/Inter-Regular.otf"
SANS_GRAS = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"


def police(chemin, taille):
    return ImageFont.truetype(chemin, taille)


def texte_centre(dessin, y, texte, fonte, couleur=TEXTE, largeur_max=L - 120):
    """Écrit un texte centré, sur plusieurs lignes si besoin. Renvoie le y suivant."""
    mots, lignes, ligne = texte.split(), [], ""
    for mot in mots:
        essai = f"{ligne} {mot}".strip()
        if dessin.textlength(essai, font=fonte) <= largeur_max:
            ligne = essai
        else:
            lignes.append(ligne)
            ligne = mot
    lignes.append(ligne)
    hauteur = fonte.size + fonte.size // 4
    for l in lignes:
        dessin.text(((L - dessin.textlength(l, font=fonte)) / 2, y), l, font=fonte, fill=couleur)
        y += hauteur
    return y


def charger_photo(produit, index, dossier_photos):
    if dossier_photos:
        candidats = sorted(Path(dossier_photos).glob(f"{index + 1:02d}.*"))
        if not candidats:
            raise SystemExit(f"Photo manquante : {dossier_photos}/{index + 1:02d}.jpg ({produit['marque']})")
        return Image.open(candidats[0]).convert("RGB")
    url = produit["image"] + "?width=1200"
    with urllib.request.urlopen(url, timeout=30) as reponse:
        return Image.open(io.BytesIO(reponse.read())).convert("RGB")


def carte_article(produit, photo, numero, total):
    """Image fixe de l'article ; la photo est rendue à part pour l'effet de zoom."""
    fond = Image.new("RGB", (L, H), FOND)
    d = ImageDraw.Draw(fond)
    d.text((60, 70), "MAISON NSAIA", font=police(SANS_GRAS, 34), fill=TEXTE)
    compteur = f"{numero}/{total}"
    f = police(SANS, 34)
    d.text((L - 60 - d.textlength(compteur, font=f), 70), compteur, font=f, fill=GRIS)

    y = 1290
    y = texte_centre(d, y, produit["marque"].upper(), police(SANS_GRAS, 44), GRIS)
    y = texte_centre(d, y + 10, produit["nom"], police(SERIF, 60))
    y = texte_centre(d, y + 10, produit["taille"], police(SANS, 40), GRIS)

    prix = f"{produit['prix']} €"
    fp = police(SANS_GRAS, 64)
    lp = d.textlength(prix, font=fp)
    x0, y0 = (L - lp) / 2 - 50, y + 30
    d.rounded_rectangle((x0, y0, x0 + lp + 100, y0 + 110), radius=55, fill=TEXTE)
    d.text(((L - lp) / 2, y0 + 18), prix, font=fp, fill=FOND)
    return fond


def image_article(fond, photo, t):
    """Compose la carte avec la photo légèrement zoomée (t de 0 à 1)."""
    zone_l, zone_h, zone_y = L - 120, 1080, 160
    zoom = 1.0 + 0.06 * t
    p = ImageOps.contain(photo, (int(zone_l * zoom), int(zone_h * zoom)), Image.LANCZOS)
    # recadre au centre pour garder la photo dans sa zone
    gauche = max(0, (p.width - zone_l) // 2)
    haut = max(0, (p.height - zone_h) // 2)
    p = p.crop((gauche, haut, gauche + min(p.width, zone_l), haut + min(p.height, zone_h)))
    img = fond.copy()
    img.paste(p, ((L - p.width) // 2, zone_y + (zone_h - p.height) // 2))
    return img


def carte_texte(titre, sous_titre, pied):
    img = Image.new("RGB", (L, H), TEXTE)
    d = ImageDraw.Draw(img)
    y = texte_centre(d, 760, titre, police(SERIF_GRAS, 110), FOND)
    y = texte_centre(d, y + 40, sous_titre, police(SANS, 50), (200, 200, 200))
    texte_centre(d, 1500, pied, police(SANS_GRAS, 52), FOND)
    return img


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--photos", help="dossier de photos locales numérotées 01, 02…")
    parser.add_argument("--sortie", default=str(SORTIE))
    args = parser.parse_args()

    produits = json.loads(PRODUITS.read_text(encoding="utf-8"))
    total = len(produits)

    # (image ou fonction t -> image, durée)
    sequences = [(carte_texte("Maison Nsaia", f"{total} pièces de marque disponibles", "Tout est en ligne"), DUREE_INTRO)]
    for i, produit in enumerate(produits):
        print(f"[{i + 1}/{total}] {produit['marque']} — {produit['nom']}")
        photo = charger_photo(produit, i, args.photos)
        fond = carte_article(produit, photo, i + 1, total)
        sequences.append(((lambda t, f=fond, p=photo: image_article(f, p, t)), DUREE_ARTICLE))
    sequences.append((carte_texte("maison-nsaia.fr", "Pièces uniques, neuves ou comme neuves", "Lien en bio · Livraison en France"), DUREE_OUTRO))

    Path(args.sortie).parent.mkdir(parents=True, exist_ok=True)
    ffmpeg = subprocess.Popen(
        ["ffmpeg", "-y", "-loglevel", "error",
         "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{L}x{H}", "-r", str(FPS), "-i", "-",
         "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
         "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-shortest", "-movflags", "+faststart", args.sortie],
        stdin=subprocess.PIPE,
    )

    def rendu(seq, t):
        source, _ = seq
        return source(t) if callable(source) else source

    precedente = None
    for seq in sequences:
        n = int(seq[1] * FPS)
        n_fondu = int(FONDU * FPS)
        for k in range(n):
            img = rendu(seq, k / max(1, n - 1))
            if precedente is not None and k < n_fondu:
                img = Image.blend(precedente, img, (k + 1) / n_fondu)
            ffmpeg.stdin.write(img.tobytes())
        precedente = rendu(seq, 1.0)
    ffmpeg.stdin.close()
    if ffmpeg.wait() != 0:
        raise SystemExit("ffmpeg a échoué")
    print(f"Vidéo prête : {args.sortie}")


if __name__ == "__main__":
    main()
