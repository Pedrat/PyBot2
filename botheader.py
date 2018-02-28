# coding=utf-8
import os,sys,json,random,requests
from fbmq import Page, Attachment, QuickReply, utils
from fbmq import template as Template
from datetime import datetime
from flask import Flask, request
from pymessager.message import Messager

token = "EAACoZCnVve74BAAIZCs17iPNPK6pUatUdOKhY2EciLVhTEZAU2Bx1KD3EFYiUvYtFYxNXEOQXYj2VVcme8PmsLBuHQGQgDztJfcjcqVPZBfM8ZArrXgOxvSbgvrUZAIvz34ACTZBhUUfQ6qrlY7KHEN0lBZAng5Oylz58XGtGfmJAd2l9bE4sjS5"
page = Page(token)



class buttons:
    btn1 = [
      Template.ButtonWeb("Open Web URL", "https://www.oculus.com/en-us/rift/"),
      Template.ButtonPostBack("trigger Postback", "DEVELOPED_DEFINED_PAYLOAD"),
      Template.ButtonPhoneNumber("Call Phone Number", "+16505551234")
    ]

class quickReply:
        quick_replies1 = [{'title': 'Rock', 'payload': 'PICK_ROCK'},
                        {'title': "Rn'B", 'payload': 'PICK_RnB'},
                        {'title': 'Pop', 'payload': 'PICK_POP'},
                        {'title': 'Indie', 'payload': 'PICK_INDIE'},
                        {'title': 'Classic', 'payload': 'PICK_CLASSIC'},
                        {'title': 'Metal', 'payload': 'PICK_METAL'}]

class Handle:
    def get_num():
        numbergen=[1,2]
        return random.choice(numbergen)
    def get_att(tipo):
        if tipo == 'image':
            exemplos = ["https://cdn.shopify.com/s/files/1/0862/4240/products/1_0d691e32-3771-402a-aaee-dc004ea1b2c3.jpeg?v=1441091543","https://vignette.wikia.nocookie.net/harrypotter/images/2/27/Happy-guy-thumbs-up-300x237.gif/revision/latest?cb=20121019041406"]

        if tipo == 'thumbs':
            exemplos =["http://4.bp.blogspot.com/-EGzuN7Jcj0I/UUnR1Y0xWQI/AAAAAAAAA2Q/XMK6_yMNYPo/s1600/ChuckNorristhumbsup+Emil+P.jpg"]
        return random.choice(exemplos)

    def get_message(tipo): #Random msg
        if tipo == 'image':
            exemplos= ["Lindo/a","Que giro","Wow"]
        elif tipo == 'video':
            exemplos=["ja vejo esse video", "video giro", "spectalucaaah"]
        elif tipo == 'audio':
            exemplos=["já oiço", "voz sexy", "say whaaaaa!"]
        if tipo == 'smile':
            exemplos=[":D",":)",";)",":P",":P",":v","(^^^)"]
        return (random.choice(exemplos)+' -signed bot')

@page.handle_message
def message_handler(event):
    sender_id = event.sender_id
    timestamp = event.timestamp
    message = event.message
    page.typing_on(sender_id)
    if message.get("attachments"):
        page.send(sender_id,"Imagem")
    elif message.get("quick_reply"):
        page.send(sender_id, "QuickReply")
    elif message.get("text"):
        message = event.message_text
        page.send(sender_id, "Thank you!")




@page.handle_postback
def received_postback(event):
    sender_id = event.sender_id
    recipient_id = event.recipient_id
    time_of_postback = event.timestamp

    payload = event.postback_payload

    print("Received postback for user %s and page %s with payload '%s' at %s"
          % (sender_id, recipient_id, payload, time_of_postback))

    page.send(sender_id, "Postback called")
