# This is the flask application to deploy the model

# Here we are using Flask framework to deploy our model
# We are using pickle to load the model
# so here we are writing the flask code    

import pickle
from flask import Flask, request, app, jsonify, url_for, render_template  
import numpy as np
import pandas as pd

app = Flask(__name__)
## Load the model
lin_reg = pickle.load(open('california_housing_model.pkl', 'rb'))
scaler = pickle.load(open('scaling.pkl', 'rb'))
@app.route('/')
def home():                                      
    return render_template('home.html')                                      


@app.route('/predict_api', methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1, -1))
    new_data=scaler.transform(np.array(list(data.values())).reshape(1, -1))
    output = lin_reg.predict(new_data)
    print(output[0])
    return jsonify(output[0]) 


@app.route('/predict', methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input=scaler.transform(np.array(data).reshape(1, -1))
    print(final_input)
    output=lin_reg.predict(final_input)[0]  
    return render_template("home.html", prediction_text="The House Price Prediction is {}".format(output))
                    
# here prediction_test is the placeholder in home.html page where we are showing the prediction value
# and output variable contains the prediction value 

if __name__=="__main__":
    app.run(debug=True)
    



