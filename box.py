#!/usr/bin/env python
# from readtest import *
import re
from HomeassistantClient import HomeassistantClient
from CardList import CardList
from Reader import Reader
import sys
# import subprocess
import os
import time

# verify necessary Home-Assistant environment variables are set
if not os.environ.get("HASS_SERVER"):
    print("HASS_SERVER not set")
    sys.exit(1)

if not os.environ.get("HASS_TOKEN"):
    print("HASS_TOKEN not set")
    sys.exit(1)

hass_cli = HomeassistantClient(
    server=os.environ.get("HASS_SERVER"),
    token=os.environ.get("HASS_TOKEN")
)
reader = Reader()
card_list = CardList()

while True:
    print("Ready: scan a card with the reader")
    read_code = reader.readCard()
    # try:
    print(f"Read card code {read_code}")
    card = card_list.get_card(code=read_code)
    if card is not None:
        print(f"Found card: {card['title']}")

        # prefix card properties with "card_" to match magic-cards behavior
        card_data = {'card_' + k: v for k,v in card.items()}
        # TODO: magic_card_room should be a configurable parameter
        card_data["magic_cards_room"] = "Bonus Room"
        hass_cli.fire_event("magic_card_scanned", data=card_data)
    else:
        print("Card not found")
    range(10000)  # some payload code
    time.sleep(0.2)  # sane sleep time of 0.1 seconds
    # except OSError as e:
    #     print("Execution failed:")
    #     range(10000)  # some payload code
    #     time.sleep(0.2)  # sane sleep time of 0.1 seconds
