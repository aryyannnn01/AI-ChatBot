from flask import Flask, render_template, request, jsonify
from chatbot import get_bot_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "").strip()

    if not message:
        return jsonify({"response": "Please enter a question."})

    response = get_bot_response(message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)