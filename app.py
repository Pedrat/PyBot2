# coding=utf-8
import os
import sys
import json
import random
from datetime import datetime
listasender=[]
import requests
from flask import Flask, request
date=datetime.now().strftime("%d/%m")
app = Flask(__name__)

if date == "25/02":
    for x in listasender:
        send_message(x,"Parabéns!!!")




@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200


@app.route('/', methods=['POST'])
def webhook():

    # endpoint for processing incoming messaging events

    data = request.get_json()
    log(data)  # you may not want to log every incoming message in production, but it's good for testing

    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                exemplos = ["Não sei essa palavra :c Desculpa! Mas os nossos donos foram avisados!","Bolas, peço imensa desculpa mas não consigo lhe ajudar..."]
                if messaging_event.get("message"):  # someone sent us a message
                    if messaging_event['message'].get('text'):
                        sender_id = messaging_event["sender"]["id"]        # the facebook ID of the person sending you the message
                        save(sender_id)
                        recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
                        message_text = messaging_event["message"]["text"]  # the message's text
                        if message_text == "Ajuda!":
                            send_message(sender_id,"Com o que podemos ajudar?")
                        elif message_text == "Que dia e hoje?":
                            send_message(sender_id,("{}".format(datetime.now().strftime("%d/%m/%Y"))))
                        else:
                            msg = random.choice(exemplos)
                            send_message(sender_id, msg)

                    if messaging_event['message'].get('attachments'):
                        sender_id = messaging_event["sender"]["id"]        # the facebook ID of the person sending you the message
                        recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
                            #message_text = messaging_event["message"]["text"]  # the message's text
                        msg = get_message()
                        send_message(sender_id,msg)
                if messaging_event.get("delivery"):  # delivery confirmation
                    pass

                if messaging_event.get("optin"):  # optin confirmation
                    pass

                if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
                    pass

    return "ok", 200


def send_message(recipient_id, message_text):

    log("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

    params = {
        "access_token": os.environ["PAGE_ACCESS_TOKEN"]
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message_text
        }
    })
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
        log(r.text)

def save(id):
    listasender.append(id)
    file = open("ID.txt","a")
    #for x in listasender:
    file.write(id)
    file.close()



def log(msg, *args, **kwargs):  # simple wrapper for logging to stdout on heroku
    try:
        if type(msg) is dict:
            msg = json.dumps(msg)
        else:
            msg = (msg).format(*args, **kwargs)
        print "{}: {}".format(datetime.now(), msg)
        print "TESTE DE DEBUGGING:"
        print date
        for x in listasender:
            print x
    except UnicodeEncodeError:
        pass  # squash logging errors in case of non-ascii text
    sys.stdout.flush()

def get_message():
    exemplos= ["Lindo/a","Que giro","Wow"]
    return random.choice(exemplos)

if __name__ == '__main__':
    app.run(debug=True)
