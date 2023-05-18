from flask import Flask
from flask import jsonify
from flask import request
import pandas as pd

from module.insurance_model import InsuranceModel

app = Flask(__name__)


@app.route("/test")
def test():
    return jsonify({
        "status": "OK",
        "code": 200
    })


@app.route("/predict", methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame(data)
    X = InsuranceModel().runModel(df, typed='single')

    return jsonify({
        "status": "Predicted",
        "result": X
    })
