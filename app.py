# coding=utf-8
import os,sys,json,random,requests
from fbmq import Page, Attachment, QuickReply, utils
from fbmq import template as Template
from datetime import datetime
from flask import Flask, request
#from classes import TemplateTest
page = Page("EAACoZCnVve74BAAIZCs17iPNPK6pUatUdOKhY2EciLVhTEZAU2Bx1KD3EFYiUvYtFYxNXEOQXYj2VVcme8PmsLBuHQGQgDztJfcjcqVPZBfM8ZArrXgOxvSbgvrUZAIvz34ACTZBhUUfQ6qrlY7KHEN0lBZAng5Oylz58XGtGfmJAd2l9bE4sjS5")
date=datetime.now().strftime("%d/%m")
app = Flask(__name__)
numbergen=[1,2]

@app.route('/', methods=['GET'])
def verify():
    # Vai ao endpoint e verifica os tokens, para o webhook
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200



class button:
    def test_buttons(self):
        btns1 = Template.Buttons(text="Title", buttons=[
            {'type': 'web_url', 'title': 'title', 'value': 'https://test.com'},
            {'type': 'postback', 'title': 'title', 'value': 'TEST_PAYLOAD'},
            {'type': 'phone_number', 'title': 'title', 'value': '+82108011'},
        ])

        btns2 = Template.Buttons(text="Title", buttons=[
            Template.ButtonWeb(title="title", url="https://test.com"),
            Template.ButtonPostBack(title="title", payload="TEST_PAYLOAD"),
            Template.ButtonPhoneNumber(title="title", payload="+82108011")
        ])

        self.assertEquals(utils.to_json(btns1), utils.to_json(btns2))




@app.route('/', methods=['POST'])
def webhook():
    # Processa msg
    data = request.get_json()
    log(data)
    if data["object"] == "page":
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                exemplos = ["Peço imensa desculpa, não pense que sou um bot burro.....DITO ISTO.... Não faço ideia do que disse... sorry :D","Não sei essa palavra :c Desculpa! Mas os nossos donos foram avisados!","Bolas, peço imensa desculpa mas não consigo lhe ajudar..."]
                if messaging_event.get("message"):  # Alguem mandou algo
                    if messaging_event['message'].get('text'):
                        sender_id = messaging_event["sender"]["id"]        # the facebook ID da pessoa
                        recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID da pagina
                        message_text = messaging_event["message"]["text"]  # the text
                        page.typing_on(sender_id)
                        if message_text.lower() == "ajuda!":
                            page.send(sender_id,"Com o que podemos ajudar?")
                        elif message_text.lower() == ("que dia é hoje?" or "que dia e hoje?"):
                            page.send(sender_id,("{}".format(datetime.now().strftime("%d/%m/%Y"))))
                        elif message_text == ':D' or ':P' or ':)' or ';)':
                            msg=get_message('smile')
                            page.send(sender_id,msg)

                        else:
                            msg = random.choice(exemplos)
                            page.send(sender_id, msg)
                            page.send(sender_id, Template.Buttons("hello", button.test_buttons))
                    if messaging_event['message'].get('attachments'):
                        sender_id = messaging_event["sender"]["id"]        # O facebook ID da pessoa
                        recipient_id = messaging_event["recipient"]["id"]  # O recipient's ID da pagina
                        teste=messaging_event["message"]["attachments"] #Para ver o type
                        if 'image' in str(teste[0]):
                            if random.choice(numbergen) == 1:
                                msg=get_message('image')
                                page.send(sender_id,msg)
                            else:
                                image_url=get_att('image')
                                page.send(sender_id,Attachment.Image(image_url))
                        elif 'file' in str(teste[0]):
                            msg="Files são dubios"
                            page.send(sender_id,msg)
                        elif 'video' in str(teste[0]):
                            msg=get_message('video')
                            page.send(sender_id,msg)
                        elif 'audio' in str(teste[0]):
                            msg=get_message('audio')
                            page.send(sender_id,msg)

                        else:
                            msg = "Já o vou ver"
                            page.send(sender_id,msg)
                if messaging_event.get("delivery"):  # delivery confirmation
                    pass

                if messaging_event.get("optin"):  # optin confirmation
                    pass

                if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
                    pass

    return "ok", 200
#Teste
@page.callback(['PICK_ACTION', 'PICK_COMEDY'], types=['QUICK_REPLY'])




def log(msg, *args, **kwargs):  # simple wrapper for logging to stdout on heroku
    try:
        if type(msg) is dict:
            msg = json.dumps(msg)
        else:
            msg = (msg).format(*args, **kwargs)
        print ("{}: {}".format(datetime.now(), msg))
    except:
        pass  # squash logging errors in case of non-ascii text
    sys.stdout.flush()

def get_att(tipo):
    if tipo == 'image':
        exemplos = ["https://cdn.shopify.com/s/files/1/0862/4240/products/1_0d691e32-3771-402a-aaee-dc004ea1b2c3.jpeg?v=1441091543","https://vignette.wikia.nocookie.net/harrypotter/images/2/27/Happy-guy-thumbs-up-300x237.gif/revision/latest?cb=20121019041406"]
    return random.choice(exemplos)

def get_message(tipo): #Random msg
    if tipo == 'image':
        exemplos= ["Lindo/a","Que giro","Wow"]
    elif tipo == 'video':
        exemplos=["ja vejo esse video", "video giro", "spectalucaaah"]
    elif tipo == 'audio':
        exemplos=["já oiço", "voz sexy", "say whaaaaa!"]
    if tipo == 'smile':
        exemplos=[":D",":)",";)",":P",":3"]
    return (random.choice(exemplos)+' -signed bot')

if __name__ == '__main__':
    app.run(debug=True)
