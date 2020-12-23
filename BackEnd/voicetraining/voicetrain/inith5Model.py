from keras.models import load_model
from django.apps import AppConfig
model_path = ''
model = load_model(model_path)
class loadModel(AppConfig):
    pass