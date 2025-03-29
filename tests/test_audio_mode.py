import pytest
import json
from unittest.mock import mock_open, patch
from calm_place_modes.audio_mode import MakeAudio


@pytest.fixture
def mock_texts_data():
    return [
        {"id": 1, "title": "The Forest"},
        {"id": 2, "title": "The Ocean"},
    ]


def test_load_file(mock_texts_data):
    mock_json = json.dumps(mock_texts_data)

    make_audio = MakeAudio(texts_file="mock_texts_file.json")

    with patch("builtins.open", mock_open(read_data=mock_json)):
        result = make_audio.load_file()

    assert result == mock_texts_data
    assert make_audio.texts_data == mock_texts_data
