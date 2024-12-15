from flask import Flask, request, jsonify
from langdetect import detect

app = Flask(__name__)

@app.route('/detect', methods=['POST'])
def detect_language():
    # Ensure the request contains the 'text' key
    if 'text' not in request.json:
        return jsonify({"error": "Aucun texte fourni"}), 400

    text = request.json['text']
    try:
        # Use langdetect to detect the language
        language = detect(text)
        return jsonify({"language": language})
    except Exception as e:
        # Handle any error during language detection
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6002)
