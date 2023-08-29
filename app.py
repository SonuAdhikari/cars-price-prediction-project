from flask import Flask, request, render_template
import pickle
import requests
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)  # initialising flask app

loaded_model = pickle.load(open('car-price.pkl', 'rb')) # load ml model

model = loaded_model['model']
scaler = loaded_model['scaler']
mileage = loaded_model['mileage']
max_power = loaded_model['max_power']
engine = loaded_model['engine']

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

#@app.route('/', methods=['POST', 'GET'])
@app.route('/', methods=['POST'])
def predict():
    if request.method == 'POST':
        #year_of_purchase = float(request.form['year'])
        #km_driven = int(request.form['distance'])
        car_mileage = float(request.form['mileage'])
        engine = float(request.form['engine'])
        max_power = float(request.form['max_power'])
        input_data = np.array([[car_mileage,engine,max_power]])
        scaled_sample = scaler.transform(input_data)
        prediction = model.predict(scaled_sample)[0]
        #prediction = model.predict([[year_of_purchase, km_driven, car_mileage, engine, max_power]])
        #output = round(prediction[0], 2)
        return render_template("index.html", prediction = np.exp(prediction))
        #*return render_template('index.html', output="{} Lakh".format(output))
if __name__ == '__main__':
    app.run(debug=True)