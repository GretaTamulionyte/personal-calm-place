# personal-calm-place


"Hello! Welcome to Personal Calm Place.

This program lets you create custom relaxation tapes based on vizualization scripts that you yourself write.


You can tap into your creativity and write scripts that are unique to you, reflecting what personally calms you the most.
You can also choose the type of realistic calming voice that will read your creations back to you.
Also, you can add some calming background audio to make the experience even more relaxing.
Your finished audio files will be saved for you to enjoy anytime you feel you need it."

This program is based on the simple notion that vizualization relaxation scripts and 
audio tapes(basically vizualizing a calming place to relax and unwind), while there are plenty of them,
may be more relaxing if a user adds their own personal touch to it.

The idea is that the user can write a personally meaningful soothing text,
then choose a voice that they like, and then choose some background sounds 
that would compliment the custom vizualization relaxation tape.

This is a very very minimalist version of the program, as I am still learning and can see a million ways to improve it.

# Functionality that will be added on later versions:
1. More voices and previews of the voices so that the user can choose with more information at hand
2. Another API that will add more variety and let the user have more control over background sounds - 
basically any AI generated background sound (like birds chirping) with a simple prompt
3. Mixing the two tracks needs improving
4. And lots lots more


For pydub library to work properly, you will need to:

# Install ffmpeg (Windows)
1. Download FFmpeg from https://ffmpeg.org/download.html
2. Extract it to `C:\ffmpeg` or a place of your choice
3. Add `C:\ffmpeg\bin` to **System PATH**
4. Verify installation by running: `ffmpeg -version` in terminal

# Install ffmpeg (Linux/macOS)
sudo apt install ffmpeg   # Ubuntu/Debian
brew install ffmpeg       # macOS


# Other important instructions for the program to work:
1. You will need to sign up at elevenlabs.io and get your API key from https://elevenlabs.io/app/settings/api-keys
Luckily the trial is free and offers more than enough credits to play around with this program
2. You will need to create and activate your virtual environment in VS Code or wherever and 
install all the dependencies from the requirements.txt file to check out the project.
3. You will also need to look at the .env.example file, create .env file and update the environmental variables
with your own valid values accordingly.
4. Make sure to download even the mp3 files.


The command to install dependencies:
pip install -r requirements.txt






