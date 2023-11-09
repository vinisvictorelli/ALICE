from gtts import gTTS
import os
from gtts.tokenizer.pre_processors import abbreviations, end_of_line
tts = gTTS("Hi,I am alice, and i am your personal assistant",lang="en",slow=False)

tts.save("output.mp3")