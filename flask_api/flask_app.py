from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np


app = Flask(__name__)

def load_object(filename):
    with open(filename ,'rb') as f:
        loaded = joblib.load(f)
    return loaded

cols_to_scale = ["mileage_kmpl", "engine", "max_power", "km_driven_log", "age"]

def get_price(features):
    print(features)
    model, _ = load_object('model.pkl')
    scalers = load_object('scalers.pkl')
    # for col in cols_to_scale:
    #     # scale the features and rehape (1, -1)
    #     features[col] = scalers[col].transform(np.array(features[col]).reshape(1, -1))
    df = pd.DataFrame([features])
    prediction = np.exp(model.predict(df))
    return int(prediction[0])

# prediction function route
@app.route('/predict', methods=['POST'])
def predict():
    features = request.get_json()
    return jsonify({'prediction': get_price(features)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
