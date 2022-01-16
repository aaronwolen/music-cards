# import os
# from HomeassistantClient import HomeassistantClient
# from CardList import CardList

# cli = HomeassistantClient(
#     server=os.environ.get("HASS_SERVER"), token=os.environ.get("HASS_TOKEN")
# )

# card_list = CardList()
# card = card_list.get_card("550007f2ee")
# prefixed_card = {'card_' + k: v for k,v in card.items()}
# cli.fire_event("magic_card_scanned", data=prefixed_card)