#!/bin/bash
card_code=$1
card_type=$2
card_art_url=$3
card_title=$4
card_subtitle=$5
card_uri=$6

# card_uri="spotify:track:3Z0oQ8r78OUaHvGPiDBR3W"

# payload variables
magic_cards_room="Bonus Room"

curl \
    --max-time 2 \
    --silent \
    --output /dev/null \
    -X POST \
    -H "Authorization: Bearer ${HASS_TOKEN}" \
    -H "Content-Type: application/json" \
    -d '{"card_title": "'"$card_title"'", "card_code": "'"$card_code"'", "card_uri": "'"$card_uri"'", "magic_cards_room": "'"$magic_cards_room"'"}' \
    "http://${HASS_SERVER}/api/events/magic_card_scanned"
