from flask import Flask, render_template, request, jsonify
from src.predict import predict_severity


# ============================================================
# FLASK APP
# ============================================================

app = Flask(__name__)


# ============================================================
# HOME PAGE
# ============================================================

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


# ============================================================
# PREDICTION API
# ============================================================

@app.route("/predict", methods=["POST"])
def predict():

    try:
        data = request.get_json()

        if not data:
            return jsonify({
                "error": "No input data provided"
            }), 400

        result = predict_severity(data)

        return jsonify(result)

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ============================================================
# RUN APP
# ============================================================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )