from flask import Flask, request, jsonify
import pandas as pd
from predict import predict_fraud
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data
    input_data = request.json
    new_data = pd.DataFrame(input_data)
    
    # Make predictions
    predictions = predict_fraud(new_data)
    
    # Return predictions as JSON
    return jsonify({'predictions': predictions.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
