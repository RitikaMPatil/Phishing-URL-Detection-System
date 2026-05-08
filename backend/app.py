from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load trained model
model = joblib.load("url_model.pkl")


# Feature extraction function
def extract_features(url):

    features = {
        "url_length": len(url),
        "valid_url": 1,
        "at_symbol": 1 if "@" in url else 0,
        "sensitive_words_count": sum(
            word in url.lower()
            for word in ["login", "secure", "bank", "verify", "update"]
        ),
        "path_length": len(url.split("/")),
        "isHttps": 1 if "https" in url else 0,
        "nb_dots": url.count("."),
        "nb_hyphens": url.count("-"),
        "nb_and": url.count("&"),
        "nb_or": url.count("|"),
        "nb_www": 1 if "www" in url else 0,
        "nb_com": 1 if ".com" in url else 0,
        "nb_underscore": url.count("_"),
    }

    return pd.DataFrame([features])


# Prediction route
@app.route("/predict", methods=["POST"])
def predict():

    data = request.json
    url = data["url"]

    features = extract_features(url)

    prediction = model.predict(features)[0]

    result = "Phishing URL" if prediction == 1 else "Safe URL"

    return jsonify({
        "prediction": result
    })


if __name__ == "__main__":
    app.run(debug=True)