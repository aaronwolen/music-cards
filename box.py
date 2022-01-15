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
cardList = CardList()

# verify necessary Home-Assistant environment variables are set
if not os.environ.get("HASS_SERVER"):
    print("HASS_SERVER not set")
    sys.exit(1)

if not os.environ.get("HASS_TOKEN"):
    print("HASS_TOKEN not set")
    sys.exit(1)

print("Ready: place a card on top of the reader")

while True:
    card = reader.readCard()
    try:
        print(f"Read card {card}")
        plist = cardList.getPlaylist(card)
        print(f"Playlist {plist}")
        if plist != "":
            subprocess.check_call(["./haevent.sh %s" % plist], shell=True)
        range(10000)  # some payload code
        time.sleep(0.2)  # sane sleep time of 0.1 seconds
    except OSError as e:
        print("Execution failed:")
        range(10000)  # some payload code
        time.sleep(0.2)  # sane sleep time of 0.1 seconds
