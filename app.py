##from django.shortcuts import render
from flask import Flask, request, jsonify,app,render_template,redirect,url_for
import numpy as np
import pandas as pd
import pickle
app = Flask(__name__)
# Load the trained model (replace 'model.pkl' with your actual model file)
regmodel = pickle.load(open('linear_reg.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict_api', methods=['POST'])
def predict_api():
    # Get the input data from the form
    #  input_data = [float(x) for x in request.form.values()]
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1, -1))
    # Convert the input data to a numpy array and reshape it for prediction
    input_array = np.array(list(data.values())).reshape(1, -1)
    # Make a prediction using the loaded model
    prediction = regmodel.predict(input_array)
    print(prediction[0])
    # Render the result on the webpage
    return jsonify({'prediction': prediction[0]})
    #return render_template('index.html', prediction_text='Predicted Sales: {:.2f}'.format(prediction[0]))
   

if __name__ == "__main__":
    app.run(debug=True)     
