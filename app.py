from flask import Flask, render_template, request, jsonify
from prediction import get_prediction
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")


@app.route("/name")
def name():
    return "Johann"

@app.route("/joke")
def jokes():
    data = { "author": "johann", "joke": "De qué color era el caballo blanco de Artigas?"  }
    return jsonify(data)

@app.route("/john", methods=["GET"])
def john_endpoint():
    # External endpoint to call
    external_url = "https://api.chucknorris.io/jokes/random"

    try:
        # Make a GET request to the external endpoint
        response = requests.get(external_url)
        response.raise_for_status()  # Raise an error for bad HTTP status codes

        # Get the text response from the external API
        chuck_response = response.text

        # Replace "Chuck" with "John" in the response
        john_response = chuck_response.replace("Chuck", "John")

        # Return the modified response
        return john_response, 200

    except requests.exceptions.RequestException as e:
        # Handle errors when calling the external API
        return jsonify({"error": str(e)}), 500

@app.route("/test_post", methods=['POST'])
def test_post():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    return jsonify({"received_data": data}), 200


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()
        class_id, class_name = get_prediction(image_bytes=img_bytes)
        return jsonify({'class_id': class_id, 'class_name': class_name})

