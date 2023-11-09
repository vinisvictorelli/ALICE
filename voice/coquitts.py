from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer

path = "./TTS/TTS/.models.json"

model_manager = ModelManager(path)

model_path, config_path, model_item = model_manager.download_model("tts_models/pt/cv/vits")

voc_path, voc_config_path, _ = model_manager.download_model(model_item["default_vocoder"])