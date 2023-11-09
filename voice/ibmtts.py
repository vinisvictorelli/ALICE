url  = "https://api.us-east.text-to-speech.watson.cloud.ibm.com/instances/caf28be4-8b98-4536-9448-4f7e1e9a7c23"
api_key = "CGJsJ4KjPqGOe8QMW_eD-lb8v6APR-Kwtuo08Zbvfejg"

from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#Setando os autenticadores para funcionar com o IBM Watson
authenticator = IAMAuthenticator(api_key)
tts =  TextToSpeechV1(authenticator)
tts.set_service_url(url)

with open('./speech.mp3', 'wb') as audio_file:
    res = tts.synthesize('Hi i am alice', accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)

