import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle

app = Flask(__name__)
model = pickle.load(open("model.pkl",'rb'))

@app.route('/')
def home():
    return render_template("webd.html")

@app.route('/predict',methods = ['POST'])
def predict():
    feature = [int(x) for x in request.form.values()]
    feature = [np.array(feature)]
    prediction = model.predict(feature)
    output = round(prediction[0],2)
    return render_template('webd.html',prediction_text = "Employee Salary should be $ {}".format(output))

if __name__ == '__main__':
    app.run(debug=True)