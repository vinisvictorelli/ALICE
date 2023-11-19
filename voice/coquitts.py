from TTS.api import TTS

api = TTS("tts_models/por/fairseq/vits")
api.tts_with_vc_to_file(
    "Ola, meu nome é alice",
    speaker_wav="output.wav",
    file_path="teste.wav"
)