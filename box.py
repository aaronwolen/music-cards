#!/usr/bin/env python

import argparse
import sys
import os
import time
from HomeassistantClient import HomeassistantClient
from CardList import CardList
from Reader import Reader


def read_card_from_reader() -> str:
    """Read card from reader"""
    print("Setting up the reader")
    reader = Reader()

    print("\nWaiting for a card to be scanned...")
    card_code = reader.readCard()
    print(f"Read card: {card_code}")
    return card_code


def main():
    """Music card reader"""
    p = argparse.ArgumentParser()
    p.add_argument(
        "-c", "--config-dir", help="Configuration directory", default="config"
    )
    p.add_argument(
        "-s",
        "--server",
        help="Home-Assistant server",
        default=os.environ.get("HASS_SERVER"),
    )
    p.add_argument(
        "-t",
        "--token",
        help="Home-Assistant token",
        default=os.environ.get("HASS_TOKEN"),
    )
    args = p.parse_args()

    if not os.path.isdir(args.config_dir):
        print("Config directory does not exist")
        sys.exit(1)

    card_list = CardList(args.config_dir)

    if args.server is None:
        print("A valid Home-Assistant server is required")
        sys.exit(1)

    if args.token is None:
        print("A valid Home-Assistant token is required")
        sys.exit(1)

    hass_cli = HomeassistantClient(server=args.server, token=args.token)

    while True:
        card = card_list.get_card(code=read_card_from_reader())

        if card is not None:
            print(f"Found card: {card['title']}")

            # prefix card properties with "card_" to match magic-card's behavior
            card_data = {"card_" + k: v for k, v in card.items()}
            # TODO: magic_card_room should be a configurable parameter
            card_data["magic_cards_room"] = "Bonus Room"
            hass_cli.fire_event("magic_card_scanned", data=card_data)
        else:
            print("Card not found")

        range(10000)  # some payload code
        time.sleep(0.2)  # sane sleep time of 0.1 seconds


if __name__ == "__main__":
    main()
