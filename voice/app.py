from gtts import gTTS
from gtts.tokenizer.pre_processors import abbreviations, end_of_line
from gtts.tokenizer.tokenizer_cases import tone_marks
def voice(text):
    tts = gTTS(text=text,lang="pt-br",slow=False,pre_processor_funcs=[abbreviations,end_of_line],tokenizer_func=[tone_marks])
    tts.save("output.mp3")

