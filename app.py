from flask import Flask
from flask import request
from pymessenger.bot import Bot

bot = Bot("EAADO2hMODGMBAFIcH9BewjmCNQ1cwIzyH9YtS5aUnpNaSLC454CKFjSMsIGGyr74UpxZAT4xLdvNkRFR84pHwbazuBrvgMTmKtBhY7ywwlcNOto3HWVUz7QoUJynloQziSnjlgA9koHuQv9urE8ZCvCJ3G2t7lTs2jUz7lnZAKEFdlJExXU")

app = Flask(__name__)
@app.route("/", methods = ["GET"])
def verify():
    if request.args.get("hub.challenge"):
        return request.args.get("hub.challenge")
    else :
        return "PLESE GO BACK"
@app.route("/", methods = ["POST"])
def message():

    data = request.get_json()

    print(data)

    for entry in data["entry"]:
        for messaging in entry["messaging"]:
            text = messaging["message"]["text"] + " by bot"
            user = messaging["sender"]["id"]
            bot.send_text_message(user, text)
            bot.send_image_url(user, "https://assets-cdn.github.com/images/modules/open_graph/github-octocat.png")



    return "MESSAGE RECEIVED"