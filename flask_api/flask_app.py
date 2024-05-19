from flask import Flask, request, jsonify
import joblib


app = Flask(__name__)

<<<<<<< HEAD
def load_object(filename):
    with open(filename ,'rb') as f:
        loaded = joblib.load(f)
    return loaded
=======
# load model
model, _ = joblib.load('model.pkl')
>>>>>>> 21d4ad710cd509a0a54934521173382c0a7adf42

# prediction function route
@app.route('/predict', methods=['POST'])
def predict():
    
    # load the model
    model, _ = load_object('model.joblib')
    
    # get the data from the POST request
    data = request.get_json()
    prediction = model.predict([data['features']])
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
