#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import textwrap

# Couleurs/Styles (fallback sans colorama si non dispo)
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except Exception:
    class _F: BLACK=RED=GREEN=YELLOW=BLUE=MAGENTA=CYAN=WHITE=RESET=""; LIGHTBLACK_EX=LIGHTWHITE_EX=""
    class _S: BRIGHT=DIM=NORMAL=RESET_ALL=""
    Fore=_F(); Style=_S()

# ──────────────────────────────────────────────────────────────────────────────
# Données
# ──────────────────────────────────────────────────────────────────────────────
DATA = [
    {
        "title": "Meilleurs spots pour la saouler",
        "emoji": "🍻",
        "places": [
            {
                "name": "La Ruée vers l'Orge",
                "url": "https://www.facebook.com/lrvoParis/",
                "desc": "Bar à bières avec une ambiance et un personnel très rare",
            },
            {
                "name": "Moonshiner",
                "url": "https://moonshinerbar.fr/",
                "desc": "Ce bar ressemble à s’y méprendre à une pizzeria, spoiler, non",
            },
        ],
    },
    {
        "title": "Meilleurs spots pour la remplir",
        "emoji": "🍽️",
        "places": [
            {
                "name": "Félicita",
                "url": "https://www.lafelicita.fr/",
                "desc": "Un incontournable pour une sortie romantique dans le thème de l’Italie",
            },
            {
                "name": "Kitchen Izakaya",
                "url": "https://www.kitchen-izakaya.com/",
                "desc": "Petit spot cozy pour manger japonais dans un cadre intimiste",
            },
            {
                "name": "TranTranZai",
                "url": "https://trantranzai.fr/",
                "desc": "Adresse incontournable pour manger à la chinoise",
            },
            {
                "name": "Melt Oberkampf",
                "url": "https://www.meltslowsmokedbarbecue.com/melt-restaurant-oberkampf",
                "desc": "Amis viandards vous serez très bien servis ici",
            },
            {
                "name": "Kasumi Paris",
                "url": "https://kasumi-restaurant.com/",
                "desc": "Restaurant japonais à volonté à la frontière de la haute gastronomie",
            },
        ],
    },
    {
        "title": "Meilleurs spots pour sortir du lot",
        "emoji": "✨",
        "places": [
            {
                "name": "Beer Spa Paris",
                "url": "https://www.beerspaparis.com/",
                "desc": "Bain à remous remplis des principaux ingrédients de la bière",
            }
        ],
    },
]

# ──────────────────────────────────────────────────────────────────────────────
# Mise en forme
# ──────────────────────────────────────────────────────────────────────────────
WIDTH = 80  # ajuste si besoin

def box(title):
    t = f" {title} "
    horiz = "─"
    side = "│"
    top = "┌" + (horiz * (WIDTH - 2)) + "┐"
    mid = side + t.center(WIDTH - 2) + side
    sep = "├" + (horiz * (WIDTH - 2)) + "┤"
    bot = "└" + (horiz * (WIDTH - 2)) + "┘"
    return top, mid, sep, bot

def color_title(s):
    return Style.BRIGHT + Fore.CYAN + s + Style.RESET_ALL

def color_section(s):
    return Style.BRIGHT + Fore.MAGENTA + s + Style.RESET_ALL

def color_url(s):
    return Style.DIM + Fore.BLUE + s + Style.RESET_ALL

def color_desc(s):
    return Fore.WHITE + s + Style.RESET_ALL

def print_catalog():
    # Titre encadré
    title = "Meilleurs spots pour un date à Paris"
    top, mid, sep, bot = box(color_title(title))
    print(top)
    print(mid)
    print(sep)

    # Sections
    bullet = f"{Fore.YELLOW}•{Style.RESET_ALL}"
    for i, section in enumerate(DATA):
        sec_title = f"{section['emoji']}  {section['title']}"
        if i == 1 :
            print("│ " + color_section(sec_title).ljust(WIDTH - 2) + "│")
        else :
            print("│ " + color_section(sec_title).ljust(WIDTH - 4) + "│")
        print("│" + (" " * (WIDTH - 2)) + "│")

        for p in section["places"]:
            name_line = f"{bullet} {Style.BRIGHT}{p['name']}{Style.RESET_ALL}"
            url_line  = f"   {color_url(p['url'])}"
            desc_line = f"   {color_desc(p['desc'])}"

            for line in [name_line, url_line, desc_line]:
                wrapped = textwrap.wrap(line, width=WIDTH - 4)
                for w in wrapped:
                    print("│ " + w.ljust(WIDTH - 4) + " │")
            print("│" + (" " * (WIDTH - 2)) + "│")

        if i < len(DATA) - 1:
            # fine séparation entre sections
            print("│ " + ("─" * (WIDTH - 4)) + " │")

    print(bot)

def main():
    print_catalog()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
