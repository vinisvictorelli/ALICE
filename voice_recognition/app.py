import speech_recognition as sr

def reconhecimento_audio():
    audio = sr.Recognizer()
    with sr.Microphone() as source:
        print('Ouvindo..')
        voz = audio.listen(source)
        comando = audio.recognize_google(voz, language='pt-BR')
        comando = comando.lower()
    return comando