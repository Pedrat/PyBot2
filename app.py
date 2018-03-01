# coding=utf-8
import os,sys,json,random,requests
from fbmq import Page, Attachment, QuickReply, utils
from fbmq import template as Template
from datetime import datetime
from flask import Flask, request
from pymessager.message import Messager
from botheader import buttons, Handle, quickReply
import botheader

page = botheader.page
app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify():
    # Vai ao endpoint e verifica os tokens, para o webhooksad
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == os.environ["VERIFY_TOKEN"]:
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "Hello world", 200

@app.route('/', methods=['POST'])
def webhook():
    page.greeting("Bem vindo, a nossa loja de produtos recreativos, por favor, pergunte-me algo!")
    page.show_starting_button("START_PAYLOAD")
    page.show_persistent_menu([Template.ButtonWeb('Website', 'http://www.cwstudio.pt/'),Template.ButtonPostBack('menu','MENU_PAYLOAD')])
    payload = request.get_data(as_text=True)
    print(payload)
    # Processa msg
    page.handle_webhook(payload)
    return "ok", 200

if __name__ == '__main__':
    app.run(debug=True)
