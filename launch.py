from flask import Flask, render_template, request, jsonify
from utils import predictSentiments
import json
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", title='Home')

@app.route("/login")
def login():
    return render_template("login.html", title='login')

@app.route("/result",methods=['POST'])
def result():
    req_PDs = int(request.form.get('PDs'))
    req_ASTV = int(request.form.get('ASTV'))
    req_POTWALTV = int(request.form.get('POTWALTV'))
    route='/predict'
    url='http://127.0.0.1:5000'+route
    param={ 'PDs': req_PDs,
    'ASTV': req_ASTV,
    'POTWALTV': req_POTWALTV }

    r=requests.post(url,data=param)
    predicts = r.json()
    

    return render_template("index.html", title='Prediction', PDs = req_PDs, ASTV = req_ASTV, POTWALTV = req_POTWALTV,
    avis = predicts['Résultat'], proba = predicts['Proba'])

@app.route("/predict",methods=['POST'])
def predict():
    req_PDs = int(request.form.get('PDs'))
    req_ASTV = int(request.form.get('ASTV'))
    req_POTWALTV = int(request.form.get('POTWALTV'))
    predictResult = predictSentiments(req_PDs, req_ASTV, req_POTWALTV)
    if(predictResult[0] == 1.0):
        strAvis = "Normal"
    elif(predictResult[0] == 2.0) :
        strAvis = "Suspected"
    else :
        strAvis = "Pathological"
     
    return jsonify({'Résultat': strAvis, 'Proba': predictResult[1]})

if __name__ == "__main__":
    app.run()