from gtts import gTTS
from gtts.tokenizer.pre_processors import abbreviations, end_of_line
from gtts.tokenizer.tokenizer_cases import tone_marks
from pydub import AudioSegment
from pydub.playback import play

def voice(text):
    tts = gTTS(text=text,lang="pt-br",slow=False)
    tts.save("output.mp3")
    sound = AudioSegment.from_mp3('output.mp3')
 

