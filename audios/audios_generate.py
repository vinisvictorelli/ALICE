import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from voice_generate.app import voice
from audios.audio_templates import audio_templates

for key in audio_templates():
    voice(audio_templates().get(key).get('text'), audio_templates().get(key).get('audio_name'))