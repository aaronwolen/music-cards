import pytest
import json
from CardList import CardList


def test_missing_card_list():
    """Errors on missing config directory"""
    with pytest.raises(FileNotFoundError):
        card_list = CardList(config_dir="missing")


def test_card_list():
    card_list = CardList()
    assert isinstance(card_list, CardList)
    assert isinstance(card_list.get_card_list(), list)
    assert isinstance(card_list.get_card_list_file(), str)
    assert isinstance(card_list.get_card_list_file_exists(), bool)
    assert len(card_list.get_card_list()) == 2


def test_card_list_file_exists():
    card_list = CardList()
    assert card_list.get_card_list_file_exists() == True


def test_get_card_by_code():
    card_list = CardList()
    card = card_list.get_card(code="550008352a")
    # assert isinstance(card, dict)
    assert card["title"] == "Cars"


def test_get_nonexistent_card():
    card_list = CardList()
    card = card_list.get_card(code="missing")
    assert card == None


def test_add_card(tmpdir):

    # make a copy of cards.json
    with open("config/cards.json", "r") as f:
        cards = json.load(f)
        f.close()
    with open(tmpdir + "/cards.json", "w") as f:
        json.dump(cards, f)
        f.close()

    card_list = CardList(config_dir=tmpdir)
    card_list.add_card(
        code="5500080cc7",
        uri="spotify:track:6oYkwjI1TKP9D0Y9II1GT7",
        card_type="song",
        title="Under the Sea",
        subtitle="The Little Mermaid",
    )
    assert len(card_list.get_card_list()) == 3
