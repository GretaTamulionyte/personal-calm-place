import pytest
from unittest.mock import patch
from calm_place_modes.texts_mode import TextData


@pytest.fixture
def mock_texts_data():
    return [
        {"id": 1, "title": "The Forest"},
        {"id": 2, "title": "The Ocean"},
        {"id": 3, "title": "The Mountain"},
    ]


def test_choose_text_valid_input(mock_texts_data):
    text_data = TextData(texts_file="mock_texts_file.json")
    text_data.texts_data = mock_texts_data

    with patch("builtins.input", side_effect=["2"]):
        assert text_data.choose_text() == 2


def test_choose_text_invalid_then_valid(mock_texts_data):
    text_data = TextData(texts_file="mock_texts_file.json")
    text_data.texts_data = mock_texts_data

    with patch("builtins.input", side_effect=["abc", "4", "1"]):
        assert text_data.choose_text() == 1


def test_choose_text_handles_valueerror(mock_texts_data):
    text_data = TextData(texts_file="mock_texts_file.json")
    text_data.texts_data = mock_texts_data

    with patch("builtins.input", side_effect=["not_a_number", "3"]):
        assert text_data.choose_text() == 3
