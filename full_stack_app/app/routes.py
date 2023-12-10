from flask import jsonify, request
from flask_restful import Resource
from app import api
from app import load_pretrained_model
import numpy as np

class PredictionResource(Resource):
    def get(self):
        # Implement your prediction logic here
        return jsonify({'message': 'Hello, this is your prediction endpoint!'})

    def post(self):
        try:
            #Index(['First Term GPA', 'Second Term GPA', 'First Language', 'Funding', 'Fast Track', 'Residency', 'Previous Education', 'Age Group', 'Math Score'], dtype='object')
            # Use the provided array as test data
            test_input_data = [2.18, 1.566667, 1.0, 2.0, 2.0, 1.0, 1.0, 2.0, 32.0]

            # Preprocess the input data
            processed_input = preprocess_input(test_input_data)

            # Assuming your model expects input_data to be a numpy array
            # Replace the following line with your actual prediction logic
            predictions = load_pretrained_model().predict(processed_input)
            predicted_class = 1 if predictions[0, 0] > 0.5 else 0

            # Return the predictions as JSON
            return jsonify({'predictions': predictions.tolist(), 'predicted_class': predicted_class})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

# Example function to preprocess numerical data
def preprocess_input(input_data):
    # Perform any necessary preprocessing steps based on your model's requirements
    # For example, convert a list of numerical features to a numpy array
    return np.array(input_data)

api.add_resource(PredictionResource, '/api/predict')