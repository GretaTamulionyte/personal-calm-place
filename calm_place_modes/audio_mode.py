from .modes_base_class import Mode

from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings

from dotenv import load_dotenv

from pydub import AudioSegment
from pydub.utils import which

import json
import math
import os
import sys


class MakeAudio(Mode):

    def interact_with_mode(self):
        print(
            "\n\nAre you ready to create a relaxation tape from your text?\n\
First select from the list of texts by typing the id number"
        )
        self.texts_data = self.load_file()
        mode_running = True
        while mode_running:
            self.show_texts()
            text_id = self.choose_text()

            for item in self.texts_data:
                if item["id"] == text_id:
                    index_of_text = self.texts_data.index(item)

            print(
                f"You've selected the text called {self.texts_data[index_of_text]['title']}"
            )
            if isinstance(self.texts_data[index_of_text]["text"], list):
                self.texts_data[index_of_text]["text"] = " ".join(
                    self.texts_data[index_of_text]["text"]
                )

            if (
                self.texts_data[index_of_text]["text"] is None
                or self.texts_data[index_of_text]["text"] == ""
            ):
                print(
                    "The text you have chosen appears to be empty. Please start over."
                )
                sys.exit()

            audio_conversion_running = True
            while audio_conversion_running:
                confirmation_to_audio = input(
                    "\n\nDo you want convert your text to audio?\n\
Type 'y' if yes, type 'n' if no, type 'e' if you want to exit the mode:\n"
                )
                if confirmation_to_audio == "e":
                    mode_running = False
                    audio_conversion_running = False
                elif confirmation_to_audio == "n":
                    audio_conversion_running = False
                elif confirmation_to_audio == "y":
                    self.choose_parameters(index_of_text)
                    print(
                        "\n\nDo you want to add some soothing background sounds to your audio?\n"
                    )
                    while True:
                        user_choice = input("Type 'y' if you do, 'n' if you don't.")
                        if user_choice == "n":
                            mode_running = False
                            audio_conversion_running = False
                            print(
                                "\n\nYour audio without background sounds is ready.\n\n"
                            )
                            break
                        elif user_choice == "y":
                            self.add_sounds(index_of_text)
                            audio_conversion_running = False
                            mode_running = False
                            break
                        else:
                            continue

                else:
                    print("Type one of they available keywords.\n")
                    continue

    def choose_parameters(self, index_of_text):
        load_dotenv()

        ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
        client = ElevenLabs(
            api_key=ELEVENLABS_API_KEY,
        )
        available_voice_ids = {
            "fa": "1wGbFxmAM3Fgw63G1zZJ",
            "fb": "l32B8XDoylOsZKiSdfhE",
            "mb": "xGDJhCwcqw94ypljc95Z",
        }

        while True:

            print(
                """
                Choose a soothing voice for your relaxation tape:

                Type 'fa' for a calming American female voice
                Type 'fb' for a wistful British female voice
                Type 'mb' for a relaxing British male voice
            
                Type 'e' to exit

                """
            )

            voice_selection = input("\n\nYour choice: ")

            if voice_selection in available_voice_ids.keys():
                try:
                    response = client.text_to_speech.convert(
                        voice_id=available_voice_ids[
                            voice_selection
                        ],  # Adam pre-made voice
                        output_format="mp3_22050_32",
                        text=self.texts_data[index_of_text]["text"],
                        model_id="eleven_turbo_v2_5",  # use the turbo model for low latency
                        # Optional voice settings that allow you to customize the output
                        voice_settings=VoiceSettings(
                            stability=0.0,
                            similarity_boost=1.0,
                            style=0.0,
                            use_speaker_boost=False,
                            speed=1.0,
                        ),
                    )
                except Exception as e:
                    print(f"An error occured: {e}")
                except BaseException as e:
                    print(f"Critical error: {e}")
                    raise
                else:
                    save_file_path = f"{self.texts_data[index_of_text]['title']}.mp3"

                    with open(save_file_path, "wb") as f:
                        for chunk in response:
                            if chunk:
                                f.write(chunk)
                    print(
                        f"\n\n{save_file_path}: Your text was successfully converted to audio!"
                    )

                    break

            elif voice_selection == "e":
                break

            else:
                print("Choose one of the available keywords.\n\n")

    def add_sounds(self, index_of_text):

        print(
            "\n\n Now you can add some calming background sounds\n\
 of your choice and your custom relaxation tape will be all done.\n\n"
        )

        available_sounds = {
            "birds": "birds-chirp.mp3",
            "rainw": "rain.mp3",
            "waves": "waves.mp3",
            "rainf": "rainforest.mp3",
        }

        while True:
            print(
                """
    
                    Choose a type of relaxing background sound for your relaxation tape:


    
                    Type 'birds' for birds chirping
                    Type 'rainw' for rain and wind chimes
                    Type 'waves' for calm waves on a sandy beach
                    Type 'rainf' for rainforest sounds

                    Type 'e' to exit and leave the audio with no background ambience

                    """
            )

            sound_selection = input("\n\nYour choice: ")
            if sound_selection in available_sounds.keys():
                AudioSegment.converter = which("ffmpeg")
                talking_audio = AudioSegment.from_file(
                    f"{self.texts_data[index_of_text]['title']}.mp3"
                )
                background_sounds = AudioSegment.from_file(
                    f"{available_sounds[sound_selection]}"
                )
                # Measure RMS (average loudness) so that later
                # we can adjust background sound volume in relation to talking audio volume
                talking_rms = talking_audio.rms
                background_rms = background_sounds.rms
                # Set the background to a percentage of the main track's volume
                desired_ratio = (
                    0.95  # Background should be 95% of main track's loudness
                )
                adjustment_db = 20 * math.log10(
                    (talking_rms / background_rms) * desired_ratio
                )
                # Apply volume adjustment to the background track
                background_sounds = background_sounds - adjustment_db
                fade_in_duration = 5000
                fade_out_duration = 10000

                # Create padding: 5 sec before and 10 sec after the main track
                silence_before = AudioSegment.silent(duration=5000)
                silence_after = AudioSegment.silent(duration=10000)
                required_length = (
                    len(silence_before) + len(talking_audio) + len(silence_after)
                )
                while len(background_sounds) < required_length:
                    background_sounds += background_sounds  # Repeat the background track if its shorter than required

                # Trim the background track to exactly match the required length
                background_sounds = background_sounds[:required_length]

                background_sounds = background_sounds.fade_in(
                    fade_in_duration
                ).fade_out(fade_out_duration)

                talking_audio = silence_before + talking_audio + silence_after
                audio_with_background = talking_audio.overlay(background_sounds)

                try:
                    audio_with_background.export(
                        f"{self.texts_data[index_of_text]['title']}_finished.mp3",
                        format="mp3",
                    )
                except Exception as e:
                    print(f"Handled error: {e}")
                except BaseException as e:

                    print(f"Critical error: {e}")

                    raise

                else:

                    print(
                        f"\n\nYour custom relaxation tape is finished and saved as {self.texts_data[index_of_text]["title"]}_finished.mp3"
                    )

                    break
            elif sound_selection == "e":

                break
            else:
                print("Choose one of the available keywords.\n\n")
