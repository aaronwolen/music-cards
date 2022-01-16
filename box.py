#!/usr/bin/env python
# from readtest import *
import re
from CardList import CardList
from Reader import Reader
import sys
import subprocess
import os
import time

reader = Reader()
card_list = CardList()

# verify necessary Home-Assistant environment variables are set
if not os.environ.get("HASS_SERVER"):
    print("HASS_SERVER not set")
    sys.exit(1)

if not os.environ.get("HASS_TOKEN"):
    print("HASS_TOKEN not set")
    sys.exit(1)

while True:
    print("Ready: scan a card with the reader")
    read_code = reader.readCard()
    try:
        print(f"Read card code {read_code}")
        card = card_list.get_card(code=read_code)
        print(card)
        print(f"Found card: {card['title']}")
        if card is not None:
            subprocess.check_call(
                [
                    f"./haevent.sh {card['uri']} {card['type']} {card['artURL']} {card['title']} {card['subtitle']} {card['uri']}"
                ],
                shell=True,
            )
        range(10000)  # some payload code
        time.sleep(0.2)  # sane sleep time of 0.1 seconds
    except OSError as e:
        print("Execution failed:")
        range(10000)  # some payload code
        time.sleep(0.2)  # sane sleep time of 0.1 seconds
