import pyttsx3

voice = pyttsx3.init()
voice.setProperty('voice', 'brazil')
voices = voice.getProperty("voices")
voice.setProperty("voice",voices[1].id)
rate = voice.getProperty('rate')
voice.setProperty('rate', rate-45)
voice.say("Ola, eu sou a alice, sou sua assitente pessoal inteligente")
voice.runAndWait()