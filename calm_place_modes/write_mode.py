from .modes_base_class import Mode


class WriteTexts(Mode):
    last_id = 0

    def __init__(self, texts_file):
        self.id = None
        self._title = None
        self._text = None
        self.chosen_form = None
        self.texts_file = texts_file

    def interact_with_mode(self):
        self.texts_data = self.load_file()
        print(
            "\n\n\nHere you can write a text about a calm place you wish to transport yourself to. \n\
The benefit of writing your own text which will later be turned into a custom relaxing \n\
vizualization tape is that you can create a place, surroundinngs and atmosphere \n\
that is unique to YOUR personal sense of calm.\n\n\n"
        )
        self.chosen_form = self.choose_parameters()
        mode_running = True
        while mode_running:

            if self.chosen_form == "f":
                print("\n\nHere is an example of a typical vizualization script:\n\n")
                print(*self.texts_data[0]["text"], sep="\n")

                self.title = input(
                    "\n\nNow think of a title for your vizualization script: "
                )
                print("\n\n")
                self.text = input(
                    "Now write your own short personal vizualization script that's unique to you:\n"
                )
                while len(self.text) > 4000:
                    print(
                        "\nUnfortunately your text is a bit too long for a typical relaxation audiotape. Try to shorten it a bit.\n"
                    )
                    self.text = input(
                        "\nWrite your own short personal vizualization script that's unique to you:\n"
                    )

                WriteTexts.last_id = max(item["id"] for item in self.texts_data)
                WriteTexts.last_id += 1
                self.id = WriteTexts.last_id

                with open(self.texts_file, "w") as file:
                    new_text = {
                        "id": self.id,
                        "title": self.title,
                        "text": self.text,
                    }
                self.texts_data.append(new_text)

                print(self.save_file())
                mode_running = False

            if self.chosen_form == "g":
                self.title = input(
                    "\n\nThink of a title for your vizualization script: "
                )
                print(
                    "\n\nTip: you may want to use the second person as the tape \n\
you make in this program will be read out to you by a calming voice of your choosing \n\
that reads the script back to you. For example, use sentences like 'You are resting on a light white cloud...'\n\n"
                )
                self.text = []
                prompts = [
                    "\n\nThink of a place that calms you.\nDescribe how you are arriving at this place, what surrounds you:\n",
                    "\n\nDecribe that place in more detail, the colors, shapes, textures:\n",
                    "\n\nDescribe what are you doing in that place, what calming thoughts are going through your head:\n",
                    "\n\nWhat's particulary calming about that place? Write about the way the place makes you feel:\n",
                    "\n\nWrite out some happy calming thoughts that make you feel relaxed and at ease. Write them as if you're experiencing them in that place right now:\n",
                    "\n\nLet your mind drift into happy thoughts and calming associations. What does the place remind you of? Write why the place feels safe:\n",
                    "\n\nWhat is happening in this place? Are there beautiful clouds in the sky? Some beautiful greenery? Fresh air? Or Maybe some birds chirping? Or maybe something else entirely that you know makes you feel safe and calm:\n",
                    "\n\nWrite an affirmation or mantra that would help soothe and calm you down:\n",
                    "\n\nFor the ending of the tape, write some positive, optimistic affirmations and describe with what positive feelings you're leaving this place:\n",
                ]
                for prompt in prompts:
                    paragraph = self.get_paragraph(prompt)
                    self.text.append(paragraph)

                WriteTexts.last_id = max(item["id"] for item in self.texts_data)
                WriteTexts.last_id += 1
                self.id = WriteTexts.last_id

                with open(self.texts_file, "w") as file:
                    new_text = {
                        "id": self.id,
                        "title": self.title,
                        "text": self.text,
                    }
                self.texts_data.append(new_text)

                print(self.save_file())
                mode_running = False

            if self.chosen_form == "e":
                mode_running = False

    def choose_parameters(self):
        print(
            "You can choose between writing the text whole, in a free-form style, \n\
the program will only give you a typical example \n\
of a vizualization script to draw inspiration from.\n\
Or you can choose to write a text in a more guided fashion. \n\
The program will help you to construct a text by giving helpful prompts.\n\n\n"
        )
        valid_answers = ["f", "g", "e"]
        while True:
            chosen_form = input(
                "Type 'f' to choose free-form text writing \n\n\
type 'g' to choose the guided approach \n\n\
Type 'e' if you want to exit to the menu. Do not use parentheses: "
            )
            if chosen_form in valid_answers:
                return chosen_form
            else:
                continue

    def get_paragraph(self, prompt):
        paragraph = input(prompt)
        while len(paragraph) > 500:
            print("\nThe paragraph is a bit too long. Please try to trim it.\n")
            paragraph = input("Try again:\n")
        return paragraph
