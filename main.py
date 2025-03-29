from calm_place_modes import AddSounds, MakeAudio, TextData, WriteTexts


import json


def main():
    print(introduction())
    texts_file = "texts.json"

    try:
        with open(texts_file, "r", encoding="utf-8") as file:
            texts_file_content = file.read()
    except FileNotFoundError:
        with open(texts_file, "w", encoding="utf-8") as file:
            texts_file_content = default_text()
            json.dump(texts_file_content, file, indent=1, ensure_ascii=False)

    interact_with_menu(texts_file)













def introduction():
    intro = """
Hello! Welcome to Personal Calm Place.

This program lets you create custom relaxation tapes based on vizualization scripts that you yourself write.


You can tap into your creativity and write scripts that are unique to you, reflecting what personally calms you the most.
You can also choose the type of realistic calming voice that will read your creations back to you.
Also, you can add some calming background audio to make the experience even more relaxing.
Your finished audio files will be saved to a folder called ''.


 
    """
    return intro



def interact_with_menu(texts_file):

    program_running = True
    while program_running:
        while True:
            print("""


        Menu:
        
        type 'write' to:  Write a description about your calm place that is uniquelly soothing to you
        type 'texts' to:  Take a look at all the texts you've written and the example text
        type 'audio' to:  Make a personalised relaxation audio with your written text and add some calming sounds

        type  'exit' to:  Exit program 
        
        
        """)

            mode = input("Choose mode by typing the keyword without quotes: ")
            if mode == "write":
                writetexts = WriteTexts(texts_file)
                writetexts.interact_with_mode()

            elif mode == "audio":
                makeaudio = MakeAudio(texts_file)
                makeaudio.interact_with_mode()

            elif mode == "texts":
                textdata = TextData(texts_file)
                textdata.interact_with_mode()

            elif mode == "exit":
                print("\n\nExiting the program. Goodbye!")
                program_running = False
                break
            
            else:
                print("\n\nPlease choose one of the available keywords.\n\n")



            






def default_text():

    only_default_text = """
                Let your imagination take you out into the woods for an adventure
                that will help you feel refreshed and so you can feel like yourself
                again…these woods are quite special and a place where you can escape
                and feel safe…it’s your own private hideaway.  Pretend as if you’re there now.

                It’s the perfect kind of day to be outside…
                it’s gorgeous and the temperature feels great…
                Overhead, the sky is a brilliant color… the sunlight
                surrounds you with healing light and warms you, 
                through and through … the clouds form into all 
                sorts of shapes and drift on by, and as the 
                clouds come and go, your worries evaporate … your mind clears, 
                like the depth and expanse of the infinite sky…

                The trees are magnificent and the woods are brimming with life… it smells delightful.
                Imagine yourself walking along a path…take a little time to yourself and notice what
                it’s like…how wide is it…what is it made of…how does it feel to be walking on it. 
                And with each step you take, notice how you feel more and more alive with a bounce 
                in your step…and it’s hard not to grin.  Walking feels effortless and invigorating …
                like you’re gliding upon a magic carpet.

                Walking along, your tiredness melts away, and more and more you notice feeling renewed 
                and revived with boundless energy.  There’s a spring in your step and it feels great to be here.
                Looking around, notice your surroundings…there are many types of trees…all different shapes and sizes,
                each one is inspiring in its own special way…and perhaps there’s a rainbow of smiling wildflowers 
                dancing in the light …and the smell of the woods comes alive.
                Notice the sounds that come and go…perhaps you hear the sound of a gentle breeze
                rustling through the leaves…the songs of the birds…or an occasional bark of a dog,
                off in the distance…what other sounds can you notice?

                The sunlight streams through beaming a golden light that dapples
                through the branches above… casting shadows here and there … 
                and the air tingles and the woods sparkle with life…it feels 
                radiant and the fresh air renews your energy with each and 
                every breath you take.  Take a few moments to continue down 
                your path, walking along at a comfortable pace, following your 
                curiosity and losing yourself in the sounds, the smells, and the colors all around.
                Off in the distance, you start to pick up on the sound of tumbling water 
                and it sparks your curiosity as to where it’s coming from, it might even be a waterfall … 
                so you take off in a new direction, not sure what you’ll find … and lo and behold, 
                you discover a beautiful creek that is gurgling and chuckling by…the water cascades 
                constantly over the rocks like a dance…and the water’s surface glimmers and glows… 
                being aware of the water as it streams on by… If you wish, you dip into the refreshing
                stream of water and it feels exhilarating …and you feel invigorated with energy…
                Relishing each and every moment…and you are reminded that this very creek 
                gradually flows into the river that eventually joins the oceans of the earth.
                Back on your path again, notice how the canopy of trees is protective and comforting 
                and how the leaves whisper in the soft breeze…. And the sunlight sparkles through, 
                bringing its warmth and wonder to everything it shines upon, and you drink in 
                its beauty…soaking it’s magic into your heart of hearts.

                And now you become aware that there’s a clearing up ahead and as you enter
                there is a hushed silence that is felt…the clearing is carpeted in softness…
                and it feels magical, and enchanted.
                Take some time to explore this special place…how large is it…what do you notice
                in the horizon…what is the air like…what sort of plant and animal life are present?
                And now your attention is captured with watching the squirrels and rabbits darting about …
                noticing the birds flying and hopping from place to place, singing their songs … 
                and noticing all the other wildlife at work and at play.

                Notice how boundless energy begins surging through you so you feel like joining in all the activity … 
                feeling the urge to enjoy yourself and play, just like the animals.  
                So, imagine enjoying yourself and having fun, exploring and discovering and playing… 
                perhaps you’d like to fly like a bird or climb a tree like a raccoon, and be carefree.
                And off in the distance, you notice a special place that has a hammock…and a park bench… 
                and a swing and you seem to glide on over and settle into one or the other for a while… 
                enjoying yourself completely and allowing yourself to daydream.

                And from this extraordinary space, you begin feeling lighter and more free and easy, 
                feeling the surge of life pulsing through you … replenishing your energy … 
                and each time you breathe, you can tell you are being completely restored from deep inside, 
                from an unending and powerful source of energy and vitality …and you feel your energy 
                and enthusiasm pouring back to you, to continue on with courage, and a willingness to trust, 
                knowing you can more than handle what’s up ahead with a knowing confidence.
                
                Having come full circle now, it’s time to come back from your woodland walk… 
                noticing how your energy and resourcefulness has grown and expanded… 
                and knowing you can come back, again and again…and each time you do, 
                your experience will deepen and grow…
                Whenever you’re ready, you can begin to stretch and move… 
                feeling full of life, alert and ready for whatever comes next.
                
                """




    default_text_data = [{
                    "id": 0,
                    "title": "Example Vizualization",
                    "text": only_default_text.split("\n")

             }]


    return default_text_data


if __name__ == "__main__":
    main()
