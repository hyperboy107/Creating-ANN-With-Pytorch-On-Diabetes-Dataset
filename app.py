# from flask import Flask, request,render_template
# import pickle
# import numpy as np
# import pandas as pd
 
# app = Flask(__name__)
# model = pickle.load(open('model.pkl','rb'))
# @app.route('/')
# def index():
#     return render_template("index.html")

# @app.route('/predict', methods=['POST'])
# def predict():
#     input_text = request.form['text']
#     input_text_sp = input_text.split(',')
#     np_data = np.asarray(input_text_sp, dtype=np.float32)
#     pred = model.predict(np_data.reshape(1,-1))

#     if pred == 1:
#         output = "This person has diabetes"
#     else:
#          output = "This person has no diabetes"

#     return render_template("index.html",message=output)
# app.run()

# from flask import Flask, render_template, request

# app = Flask(__name__)

# Replace this function with your actual prediction logic
# def predict_diabetes(details):
#     # Your prediction logic here (e.g., using a machine learning model)
#     # For demonstration, let's assume a simple rule-based prediction
#     if "blood_sugar" in details and int(details["blood_sugar"]) > 140:
#         return "High likelihood of diabetes"
#     else:
#         return "Low likelihood of diabetes"
#     if "insulin" in details and int(details["insulin"]) > 25:
#         return "High likelihood of diabetes"
#     else:
#         return "Low likelihood of diabetes"
#     if "blood_sugar" in details and int(details["blood_sugar"]) > 140:
#         return "High likelihood of diabetes"
#     else:
#         return "Low likelihood of diabetes"
#     if "blood_sugar" in details and int(details["blood_sugar"]) > 140:
#         return "High likelihood of diabetes"
#     else:
#         return "Low likelihood of diabetes"

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     message = None
#     if request.method == 'POST':
#         details = {
#             "blood_sugar": request.form['blood_sugar']
#             "insulin": request.form['insulin']
#             # Add more details as needed for your prediction
#         }
#         message = predict_diabetes(details)
#     return render_template('index.html', message=message)

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template, request, jsonify
# import joblib

# app = Flask(__name__)

# # Load the trained machine learning model
# model = joblib.load("model.pkl")

# @app.route("/predict")
# def home():
#     return render_template("index.html")

# @app.route("/predict", methods=["POST"])
# def predict():
#     try:
#         # Get input values from the form
#         features = [float(x) for x in request.form.values()]

#         # Make a prediction using the loaded model
#         prediction = model.predict([features])[0]

#         result = "Diabetic" if prediction == 1 else "Non-Diabetic"
#         return render_template("index.html", prediction_result=result)
#     except Exception as e:
#         return render_template("index.html", prediction_result="Error: " + str(e))

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, render_template, request, jsonify
from joblib import load
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from the form
        # preg = float(request.form['pregnancies'])
        glucose = float(request.form['glucose'])
        # bp = float(request.form['blood_pressure'])
        # skin_thickness = float(request.form['skin_thickness'])
        # insulin = float(request.form['insulin'])
        blood_pressure = float(request.form['blood_pressure'])
        bmi = float(request.form['bmi'])
        age = float(request.form['age'])

        # Make a prediction
        # prediction = model.predict([[preg, glucose, bp, skin_thickness, insulin, bmi, age]])
        prediction = model.predict([[ glucose, blood_pressure, bmi, age]])

        return render_template('index.html', prediction_text=f'The prediction is {prediction[0]}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run()
