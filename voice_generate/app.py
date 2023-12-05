from gtts import gTTS
from gtts.tokenizer.pre_processors import abbreviations, end_of_line
from gtts.tokenizer.tokenizer_cases import tone_marks
from pydub import AudioSegment

def voice(text):
    text = str(text)
    tts = gTTS(text=text,lang="pt-br",slow=False)
    tts.save("output.mp3")

def voice(text, audio_name):
    tts = gTTS(text=text,lang="pt-br",slow=False)
    tts.save(audio_name)
