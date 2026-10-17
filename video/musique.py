#!/usr/bin/env python3
"""Compose la musique de la vidéo : lounge chic, piano électrique, beat doux.

Musique originale générée par le script, donc libre de droits. Le tempo est
calé sur la vidéo : une mesure (4 temps) = un article, donc chaque changement
d'article tombe sur le premier temps.

Usage seul : python3 video/musique.py DUREE_SECONDES sortie.wav
"""
import sys
import wave

import numpy as np

SR = 44100
MESURE = 2.6               # = DUREE_ARTICLE de generer_video.py
TEMPS = MESURE / 4         # 92,3 BPM

# Fmaj9 – Em7 – Dm9 – Cmaj9 (notes MIDI), basse en dessous
ACCORDS = [
    ([53, 57, 60, 64, 67], 41),
    ([52, 55, 59, 62, 66], 40),
    ([50, 53, 57, 60, 64], 38),
    ([48, 52, 55, 59, 62], 36),
]


def hz(note):
    return 440.0 * 2 ** ((note - 69) / 12)


def enveloppe(n, attaque, decroissance):
    t = np.arange(n) / SR
    return np.minimum(1, t / attaque) * np.exp(-t / decroissance)


def piano(note, duree, vel=1.0):
    """Piano électrique façon Rhodes (synthèse FM)."""
    n = int(duree * SR)
    t = np.arange(n) / SR
    f = hz(note)
    mod = np.sin(2 * np.pi * f * t) * 1.6 * np.exp(-t / 0.25)
    son = np.sin(2 * np.pi * f * t + mod) + 0.25 * np.sin(2 * np.pi * 2 * f * t) * np.exp(-t / 0.4)
    return son * enveloppe(n, 0.004, 1.3) * vel


def basse(note, duree):
    n = int(duree * SR)
    t = np.arange(n) / SR
    f = hz(note)
    son = np.sin(2 * np.pi * f * t) + 0.15 * np.sin(2 * np.pi * 2 * f * t)
    env = np.minimum(1, t / 0.01) * np.minimum(1, (duree - t) / 0.05) * np.exp(-t / 1.2)
    return son * env


def grosse_caisse():
    n = int(0.45 * SR)
    t = np.arange(n) / SR
    freq = 45 + 90 * np.exp(-t / 0.03)
    return np.sin(2 * np.pi * np.cumsum(freq) / SR) * np.exp(-t / 0.18)


def bruit_filtre(rng, duree, decroissance, aigus):
    n = int(duree * SR)
    b = rng.standard_normal(n)
    if aigus:
        b = np.diff(b, prepend=0)          # garde les aigus (charleston)
    else:
        b = np.convolve(b, np.ones(6) / 6, mode="same")  # plus feutré (rimshot)
    return b * enveloppe(n, 0.001, decroissance)


def poser(piste, son, debut):
    i = int(debut * SR)
    fin = min(len(piste), i + len(son))
    if i < fin:
        piste[i:fin] += son[: fin - i]


def reverb(signal, rng, duree=1.8, mix=0.22):
    n = int(duree * SR)
    ir = rng.standard_normal(n) * np.exp(-np.arange(n) / SR / (duree / 5))
    ir /= np.sqrt(np.sum(ir ** 2))
    taille = len(signal) + n
    humide = np.fft.irfft(np.fft.rfft(signal, taille) * np.fft.rfft(ir, taille), taille)[: len(signal)]
    return signal * (1 - mix) + humide * mix * 1.5


def composer(duree, intro=MESURE):
    """Renvoie la musique en stéréo (n, 2), float entre -1 et 1."""
    rng = np.random.default_rng(7)
    n = int(duree * SR)
    cles, rythme, grave = np.zeros(n), np.zeros(n), np.zeros(n)
    nb_mesures = int(np.ceil(duree / MESURE))
    fin_beat = duree - 3.0     # la carte de fin : l'accord résonne seul

    for m in range(nb_mesures):
        t0 = m * MESURE
        notes, fondamentale = ACCORDS[m % 4]
        derniere = t0 >= fin_beat - 0.01
        # piano : accord sur le 1, rappel sur le « et » du 2
        for k, note in enumerate(notes):
            decalage = 0.012 * k   # léger arpège, plus humain
            poser(cles, piano(note, 3.0 if derniere else 2.2, 0.55), t0 + decalage)
            if not derniere:
                poser(cles, piano(note + 12 if k == len(notes) - 1 else note, 1.2, 0.25), t0 + 1.5 * TEMPS + decalage)
        if derniere:
            break
        if t0 >= intro:
            poser(grave, basse(fondamentale, 1.4 * TEMPS), t0)
            poser(grave, basse(fondamentale, 0.9 * TEMPS), t0 + 2.5 * TEMPS)
            poser(grave, basse(fondamentale + 7, 0.9 * TEMPS), t0 + 3.5 * TEMPS)
        for b in range(4):
            tb = t0 + b * TEMPS
            if t0 >= intro:
                if b in (0, 2):
                    poser(rythme, grosse_caisse() * 0.9, tb)
                if b in (1, 3):
                    poser(rythme, bruit_filtre(rng, 0.2, 0.05, False) * 0.25, tb)
            # charleston en croches, légèrement swingué, dès l'intro mais plus discret
            vol = 0.06 if t0 < intro else 0.11
            poser(rythme, bruit_filtre(rng, 0.08, 0.018, True) * vol, tb)
            poser(rythme, bruit_filtre(rng, 0.06, 0.012, True) * vol * 0.6, tb + TEMPS * 0.58)

    cles = reverb(cles, rng)
    gauche = cles * 0.9 + grave * 0.45 + rythme * 0.5
    droite = reverb(cles, np.random.default_rng(11)) * 0.9 + grave * 0.45 + rythme * 0.5
    stereo = np.stack([gauche, droite], axis=1)

    # fondus d'entrée et de sortie, puis limiteur doux
    t = np.arange(n) / SR
    stereo *= np.minimum(1, t / 0.3)[:, None]
    stereo *= np.clip((duree - t) / 2.0, 0, 1)[:, None]
    stereo = np.tanh(stereo / np.max(np.abs(stereo)) * 1.3)
    return stereo / np.max(np.abs(stereo)) * 0.89


def ecrire_wav(stereo, chemin):
    with wave.open(str(chemin), "wb") as f:
        f.setnchannels(2)
        f.setsampwidth(2)
        f.setframerate(SR)
        f.writeframes((stereo * 32767).astype("<i2").tobytes())


if __name__ == "__main__":
    ecrire_wav(composer(float(sys.argv[1])), sys.argv[2])
