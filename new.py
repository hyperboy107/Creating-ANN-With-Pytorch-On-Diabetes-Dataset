from flask import Flask, request, jsonify
from joblib import load

app = Flask(__name__)

# Load the trained model
model = load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Assuming JSON input
    features = [data['feature1'], data['feature2'], data['feature3'], data['feature4'], data['feature5'], data['feature6'], data['feature7'], data['feature8']]
    prediction = model.predict([features])[0]
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run()
