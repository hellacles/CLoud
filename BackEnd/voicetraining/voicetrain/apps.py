from django.apps import AppConfig
from keras.models import load_model
model_path = '/home/lab09/voicetraining/voicetrain/predictionModel/best_model.h5'

class VoicetrainConfig(AppConfig):
    name = 'voicetrain'
    model = load_model(model_path)
