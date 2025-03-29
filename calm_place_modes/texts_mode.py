from .modes_base_class import Mode


class TextData(Mode):

    def interact_with_mode(self):
        self.texts_data = self.load_file()
        print(
            "\n\nHere you can take a look at all the texts you've written. You can type the text id to read the full text.\n\n"
        )
        # function from base mode class that handles all this printing
        mode_running = True
        while mode_running:
            self.show_texts()
            self.choose_parameters()
            while True:
                continue_or_no = input(
                    "\n\nDo you want to continue to read texts?\n\
If you with to continue, type 'c', if you want to exit, type 'e': "
                )
                if continue_or_no == "c":
                    break
                elif continue_or_no == "e":
                    mode_running = False
                    break
                else:
                    continue

    def choose_parameters(self):
        text_id = self.choose_text()
        for item in self.texts_data:
            if item["id"] == text_id:
                print(f"\n\nTitle: {item["title"]}")
                print("\n\n")
                if isinstance(item["text"], list):
                    print(*item["text"], sep="\n")
                else:
                    print(item["text"])
