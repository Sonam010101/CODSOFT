from flask import Flask, request, jsonify, render_template
from chatbot import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("chatbotui.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    bot_reply = get_response(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)

