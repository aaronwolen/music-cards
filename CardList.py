from typing import List, Optional
import json
import uuid
import os.path


class CardList:
    """
    Initialize CardList class

    On-disk format of cards.json designed to be compatible with:
    https://github.com/maddox/magic-cards.
    """

    def __init__(self, config_dir: str = "config"):
        # store card list as dictionary of dictionaries indexed by card code
        self.__cards = {}
        self.config_dir = config_dir
        self.card_list_file = os.path.join(self.config_dir, "cards.json")
        self.card_list_file_exists = os.path.isfile(self.card_list_file)

        if not self.card_list_file_exists:
            raise FileNotFoundError("Card list file not found")
        else:
            self.read_card_list()

    def get_card_list_file(self) -> str:
        """Get card list file path"""
        return self.card_list_file

    def get_card_list_file_exists(self) -> bool:
        """Check that card list file exists"""
        return self.card_list_file_exists

    def read_card_list(self) -> None:
        """Read card list from json file"""
        with open(self.card_list_file, "r") as f:
            self.__cards = {card["code"]: card for card in json.load(f)}
            f.close()

    def get_card_list(self) -> List[dict]:
        return [card for card in self.__cards.values()]

    def get_card(self, code: str) -> dict:
        """
        Get card by card code
        """
        return self.__cards.get(code)

    def add_card(
        self,
        code: str,
        uri: str,
        card_type: str,
        title: Optional[str] = None,
        subtitle: Optional[str] = None,
        art_url: Optional[str] = None,
    ) -> None:
        """
        Add new card to card list
        """

        assert card_type in ["song", "album", "playlist", "event"]
        card = {
            "code": code,
            "type": card_type,
            "action": "Home Assistant",
            "artURL": art_url,
            "title": title,
            "subtitle": "",
            "uri": uri,
            "id": str(uuid.uuid1()),
        }

        self.__cards.update({card["code"]: card})
        self.write_card_list()

    def write_card_list(self) -> None:
        """Write card list to json file"""
        with open(self.card_list_file, "w") as f:
            json.dump(self.get_card_list(), f, indent=2)
            f.close()
