#!/usr/bin/env python

import argparse
import os.path
import sys

# from readtest import *
from CardList import CardList
from Reader import Reader

def record_user_input(label: str) -> str:
    """
    Record user input
    :param label: label to display
    """
    user_input = input(f"Enter {label} (or 'q' to quit):\n> ")
    if user_input == 'q':
        sys.exit(0)
    return user_input

def read_card_from_reader() -> dict:
    """Read card from reader"""
    print("Setting up the reader")

    while True:
        print("\nPlace the card in the reader...")
        card = {}
        card["code"] = reader.readCard()
        print(f"\tRead card: {card['code']}")

        card["uri"] = record_user_input("Spotify URI [required]")
        card["card_type"] = record_user_input("Card type [required: song, album, playlist, or event]")
        card["title"] = record_user_input("Title [required]")
        card["subtitle"] = record_user_input("Subtitle [optional]")
        card["art_url"] = record_user_input("Art URL [optional]")

        return card


def main():
    """Add new cards to the card list"""
    p = argparse.ArgumentParser()
    p.add_argument("-c", "--config-dir", help="Configuration directory", default="config")
    args = p.parse_args()

    if not os.path.isdir(args.config_dir):
        print("Config directory does not exist")
        sys.exit(1)

    card_list = CardList(args.config_dir)
    new_card = read_card_from_reader()
    card_list.add_card(**new_card)

if __name__ == "__main__":
    main()
