import json
import pytest
import tempfile

from calm_place_modes.write_mode import WriteTexts


def test_save_file():
    with tempfile.NamedTemporaryFile(
        delete=False, mode="w", encoding="utf-8"
    ) as temp_file:
        temp_path = temp_file.name

    test_data = [
        {
            "title": "The Forest",
            "text": "You are walking into a beautiful forest filled with lovely birdsong",
        },
    ]

    writetexts = WriteTexts(temp_path)
    writetexts.texts_data = test_data
    return_value = writetexts.save_file()

    writetexts.save_file()
    with open(temp_path, "r", encoding="utf-8") as file:
        saved_data = json.load(file)

    assert saved_data == test_data
    assert return_value == "\n\nYour text has been saved."
