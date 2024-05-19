from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# load rf.pkl model
model = pickle.load(open('rf.pkl', 'rb'))

# prediction function route
@app.route('/predict', methods=['POST'])
def predict():
    # get the data from the POST request
    data = request.get_json()
    prediction = model.predict([data['features']])
    return jsonify({'prediction': int(prediction[0])})
