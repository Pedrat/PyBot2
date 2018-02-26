# coding=utf-8
import os
import sys
import json
import random
import fb
from datetime import datetime
listasender=["1838746479497346"]
#TESTE CATIA
moderators=[]
token= 351316092049412
facebook=fb.graph.api(token)

import requests
from flask import Flask, request
date=datetime.now().strftime("%d/%m")
app = Flask(__name__)
'''
if date == "26/02":
    print("AQUI")
    for x in listasender:
        send_message(x,"Parabéns!!!")
'''



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
                exemplos = ["Peço imensa desculpa, não pense que sou um bot burro.....DITO ISTO.... Não faço ideia do que disse... sorry :D","Não sei essa palavra :c Desculpa! Mas os nossos donos foram avisados!","Bolas, peço imensa desculpa mas não consigo lhe ajudar..."]
                if messaging_event.get("message"):  # someone sent us a message
                    if messaging_event['message'].get('text'):
                        sender_id = messaging_event["sender"]["id"]        # the facebook ID of the person sending you the message
                        recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
                        message_text = messaging_event["message"]["text"]  # the message's text
                        if message_text == "Ajuda!":
                            send_message(sender_id,"Com o que podemos ajudar?")
                        elif message_text == "Que dia e hoje?":
                            send_message(sender_id,("{}".format(datetime.now().strftime("%d/%m/%Y"))))
                        elif message_text == "Publica-me isto sff":
                            send_message(sender_id,"Ok! :D")
                            friends_and_education=facebook.get_object(cat='single', id='me', fields=['friends', 'education'])
                            print friends_and_education
                            #facebook.publish(cat="feed", id="me", message="My facebook status")
                        else:
                            msg = random.choice(exemplos)
                            send_message(sender_id, msg)

                    if messaging_event['message'].get('attachments'):
                        sender_id = messaging_event["sender"]["id"]        # the facebook ID of the person sending you the message
                        recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
                        #print messaging_event, "TESTE TESTE TESTE"
##                        typeatt= messaging_event["attachments"]["type"]
##                        print typeatt
##                            #message_text = messaging_event["message"]["text"]  # the message's text
                        #typeatt= messaging_event["type"]
                        #print typeatt
                        teste=messaging_event["message"]["attachments"]
                        #print teste, "FUCK THIS SHIT"
                        #print teste, "TESTE"
                        fkth= str(teste[0])

                        if 'image' in fkth:
                            msg=get_message()
                        elif 'file' in fkth:
                            msg="Files são dubios"
                        else:
                            msg = "Já o vou ver"
                        #msg = get_message()
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
            "text": message_text+' -bot'
        }
    })
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
        log(r.text)



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
