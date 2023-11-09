from gtts import gTTS
import os
from gtts.tokenizer.pre_processors import abbreviations, end_of_line
tts = gTTS("Oi, eu sou a alice",lang="pt",slow=False,pre_processor_funcs = [abbreviations, end_of_line],tld="com.br")

tts.save("output.mp3")