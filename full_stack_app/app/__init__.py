# __init__.py

from flask import Flask
from flask_restful import Api
from keras.models import load_model
from app.config import Config
import os

app = Flask(__name__)
app.config.from_object('app.config')

api = Api(app)

def load_pretrained_model():
    # Import inside the function to avoid circular imports
    from app.routes import PredictionResource

    model_file_path = os.path.join(os.path.dirname(__file__), 'models', 'optimal_model_ann.h5')
    model = load_model(model_file_path)

    # Add the resource to the API with a specific endpoint name
    api.add_resource(PredictionResource, '/api/predict', endpoint='prediction_resource')

    return model

model = load_pretrained_model()