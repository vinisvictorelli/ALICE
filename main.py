from ia_alice import predict_speak
from voice_generate.app import voice
from datetime import datetime
from voice_recognition.app import reconhecimento_audio
from api_alice_online.googlebardapi import GoogleBard

def main():
    comando = reconhecimento_audio()
    print(comando)
    resposta = GoogleBard(comando)
    print(resposta)
    voice(resposta)

main()
