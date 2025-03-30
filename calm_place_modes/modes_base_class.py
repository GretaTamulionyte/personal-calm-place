from abc import ABC, abstractmethod

import json


class Mode(ABC):
    def __init__(self, texts_file):
        self.texts_file = texts_file
        self.texts_data = []

    def load_file(self):
        with open(self.texts_file, "r", encoding="utf-8") as file:
            self.texts_data = json.load(file)
        return self.texts_data

    def save_file(self):
        with open(self.texts_file, "w", encoding="utf-8") as file:
            json.dump(self.texts_data, file, indent=1, ensure_ascii=False)
        return "\n\nYour text has been saved."

    def show_texts(self):
        print(f"Currently there are {len(self.texts_data)} texts in total.\n\n")

        for item in self.texts_data:
            print(f"Title: {item["title"]}")
            print(f"Id: {item["id"]}\n\n\n")

    def choose_text(self):
        while True:
            try:
                text_id = int(input("Text id: "))
            except ValueError:
                print("Please type one of the available ids. Use numbers, not words.\n")
                continue
            else:
                if text_id not in (item["id"] for item in self.texts_data):
                    continue
                else:
                    return text_id

    @abstractmethod
    def interact_with_mode(self): ...
    @abstractmethod
    def choose_parameters(self): ...
