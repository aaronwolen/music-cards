#!/bin/bash
card_uri=$1
# card_uri="spotify:track:3Z0oQ8r78OUaHvGPiDBR3W"

# payload variables
card_code="5500085f25"
card_arturl="https://i.imgur.com/Ue09EZ8.jpg"
magic_cards_room="Bonus Room"

curl \
    --max-time 2 \
    --silent \
    --output /dev/null \
    -X POST \
    -H "Authorization: Bearer ${HASS_TOKEN}" \
    -H "Content-Type: application/json" \
    -d '{"card_title": "Default Title", "card_code": "'"$card_code"'", "card_uri": "'"$card_uri"'", "magic_cards_room": "'"$magic_cards_room"'"}' \
    "http://${HASS_SERVER}/api/events/magic_card_scanned"
