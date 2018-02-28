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
    btnmenu = [
        Template.ButtonPostBack("Musica", "MUSIC_PAYLOAD"),
        Template.ButtonPostBack('"Produtos recreativos"',"PROD_PAYLOAD"),
        Template.ButtonPostBack("Ajuda","AJUDA_PAYLOAD")
    ]

class quickReply:
        quick_musica = [{'title': 'Rock', 'payload': 'PICK_ROCK'},
                        {'title': "Rn'B", 'payload': 'PICK_RnB'},
                        {'title': 'Pop', 'payload': 'PICK_POP'},
                        {'title': 'Indie', 'payload': 'PICK_INDIE'},
                        {'title': 'Classic', 'payload': 'PICK_CLASSIC'},
                        {'title': 'Metal', 'payload': 'PICK_METAL'}]
        def get_music(genre):
            if genre == "PICK_ROCK":
                playlist = ["https://www.youtube.com/watch?v=YR5ApYxkU-U&list=RDYR5ApYxkU-U&t=1","https://www.youtube.com/watch?v=fJ9rUzIMcZQ&list=RDEMbHaAxpOZhcVmmF6I3y0siA","https://www.youtube.com/watch?v=s88r_q7oufE&list=RDEMu-D7kEFynn1tn5qmluVnhw","https://www.youtube.com/watch?v=v2AC41dglnM&list=RDEMDs8vWIQKMflBG8QUQQaUrw"]
            elif genre == "PICK_INDIE":
                playlist = ["https://www.youtube.com/watch?v=VEpMj-tqixs&list=RDQMLJaf3zcef1I","https://www.youtube.com/watch?v=A-Tod1_tZdU&list=RDEMhK9GwO7FT3oWyTWGsPuSrg","https://www.youtube.com/watch?v=_DjE4gbIVZk&list=RD_DjE4gbIVZk&t=2","https://www.youtube.com/watch?v=bpOSxM0rNPM&list=RDEMThYJ2VcXXNp3GM7AwT24UQ","https://www.youtube.com/watch?v=_lMlsPQJs6U&list=RD_lMlsPQJs6U&t=2"]
            elif genre == "PICK_POP":
                playlist = ["https://www.youtube.com/watch?v=Zi_XLOBDo_Y&list=RDEMe12_MlgO8mGFdeeftZ2nOQ","https://www.youtube.com/watch?v=EDwb9jOVRtU&list=RDEMaN9C20MoM3K8E1iVi3CAmg","https://www.youtube.com/watch?v=v0KpfrJE4zw&list=RDEM_0ItSElzQ0VS4lssmoXyeg"]
            elif genre == "PICK_RnB":
                playlist = ["https://www.youtube.com/watch?v=rywUS-ohqeE&list=RDEMWzjnvwhEBiIfo26pzdGUgw","https://www.youtube.com/watch?v=0CFuCYNx-1g&list=RD0CFuCYNx-1g"]
            elif genre == "PICK_METAL":
                playlist = ["https://www.youtube.com/watch?v=CD-E-LDc384&list=RDEMAkKpoB62G5Wmtp0nQxfrDg","https://www.youtube.com/watch?v=F_6IjeprfEs&list=RDF_6IjeprfEs&t=1","https://www.youtube.com/watch?v=KF96MQbDkMQ&list=RDKF96MQbDkMQ","https://www.youtube.com/watch?v=Ff54AQaDGbs&list=RDFf54AQaDGbs&t=1","https://www.youtube.com/watch?v=CSvFpBOe8eY&list=RDEMRoCx7NEN4B1lXoHSAiz26w"]
            elif genre == "PICK_CLASSIC":
                playlist = ["https://www.youtube.com/watch?v=O6NRLYUThrY","https://www.youtube.com/watch?v=W-fFHeTX70Q","https://www.youtube.com/watch?v=6JQm5aSjX6g",""]
            return random.choice(playlist)

class Handle:
    def get_num():
        numbergen=[1,2]
        return random.choice(numbergen)
    def get_att(tipo):
        if tipo == 'image':
            exemplos = ["https://cdn.shopify.com/s/files/1/0862/4240/products/1_0d691e32-3771-402a-aaee-dc004ea1b2c3.jpeg?v=1441091543","https://vignette.wikia.nocookie.net/harrypotter/images/2/27/Happy-guy-thumbs-up-300x237.gif/revision/latest?cb=20121019041406"]

        if tipo == 'thumbs':
            exemplos =["http://static.twentytwowords.com/wp-content/uploads/Thumbs-and-Ammo-02.jpg","http://4.bp.blogspot.com/-EGzuN7Jcj0I/UUnR1Y0xWQI/AAAAAAAAA2Q/XMK6_yMNYPo/s1600/ChuckNorristhumbsup+Emil+P.jpg"]
        return random.choice(exemplos)

    def get_message(tipo): #Random msgs
        if tipo == 'image':
            exemplos= ["Lindo/a","Que giro","Wow"]
        elif tipo == 'video':
            exemplos=["ja vejo esse video", "video giro", "spectalucaaah"]
        elif tipo == 'audio':
            exemplos=["já oiço", "voz sexy", "say whaaaaa!"]
        elif tipo == 'smile':
            exemplos=[":D",":)",";)",":P",":P",":v","(^^^)"]
        elif tipo == 'preco':
            exemplos[" os preços vão de 10€ a 100€ dependendo do preco do produto, os meus donos transmitir-lhe-ao essa informação"]        
        elif tipo  == 'text':
            exemplos = ["Peço imensa desculpa, não pense que sou um bot burro.....DITO ISTO.... Não faço ideia do que disse... sorry, mas os nossos donos serão avisados :D","Não sei essa palavra :c Desculpa! Mas os nossos donos foram avisados!","Bolas, peço imensa desculpa mas não o consigo ajudar, os meus donos serão avisados "]
        return (random.choice(exemplos)+' -signed bot')

@page.handle_message
def message_handler(event):
    sender_id = event.sender_id
    timestamp = event.timestamp
    message = event.message
    page.typing_on(sender_id)
    if message.get("attachments"):
        if 'image' in str(message.get("attachments")):
            if '369239263222822' in str(message.get("attachments")):
                image_url=Handle.get_att('thumbs')
                page.send(sender_id,Attachment.Image(image_url))
            else:
                if Handle.get_num() == 1:
                    msg=Handle.get_message('image')
                    page.send(sender_id,msg)
                else:
                    image_url=Handle.get_att('image')
                    page.send(sender_id,Attachment.Image(image_url))
        elif 'video' in str(message.get("attachments")):
            msg=Handle.get_message('video')
            page.send(sender_id,msg)
        elif 'audio' in str(message.get("attachments")):
            msg=Handle.get_message('audio')
            page.send(sender_id,msg)
        elif 'file' in str(message.get("attachments")):
            page.send(sender_id,"Files são dubios")
        else:
            page.send(sender_id,"Já o vou ver! :D")
    elif message.get("quick_reply"):
        video_url=quickReply.get_music((message.get("quick_reply")).get('payload'))
        page.send(sender_id,video_url)
    elif message.get("text"):
        message = event.message_text
        print(message)
        if message.upper() == (':D' or ':P' or ':)' or ';)'):
            page.send(sender_id,Handle.get_message('smile'))
        elif message.lower() == ('quanto custam os produtos'or 'quanto é?' or 'preço'):
            page.send(sender_id,Handle.get_message('preco'))
        elif message.lower() == ('ola' or 'boa tarde' or 'bom dia' or 'boa noite'):            
            page.send(sender_id,"Saudações")
        elif message.lower() == ('qual o segredo da vida?' or 'qual o proposito de viver' or 'existe um suprasumo da sapiencia?'):
            page.send(sender_id, "a resposta é sempre DARIO")
        elif message.lower() == ('como te chamas?' or 'quem és tu?' or 'quem és tú?' or 'qual o teu nome?'):
            page.send(sender_id, "eu sou o Bot, um robot simpático")
        elif message.lower() == ('gostas de coninha?'):
            page.send(user_id, "eu gosto mas o joaquim não, só gosta de se sentar neles")
        else:
            page.send(sender_id, Handle.get_message('text'))


@page.handle_postback
def received_postback(event):
    sender_id = event.sender_id
    recipient_id = event.recipient_id
    time_of_postback = event.timestamp
    #print("AQUI")
    payload = event.postback_payload
    #print("AQUI2")
    print("Received postback for user %s and page %s with payload '%s' at %s"
          % (sender_id, recipient_id, payload, time_of_postback))
    if payload == "START_PAYLOAD":
        page.send(sender_id,Template.Buttons("Nosso menu",buttons.btnmenu))
    elif payload == "MUSIC_PAYLOAD":
        page.send(sender_id,"Qual é o seu genero de música favorito?",quick_replies=quickReply.quick_musica,metadata="TEST")
    elif payload == "AJUDA_PAYLOAD":
        page.send(sender_id,"Eu posso fazer muitas coisas!! Mas não sou o mais esperto, mas tenho, por exemplo, isto:\n",quick_replies=quickReply.quick_musica,metadata="TESTE")
    else:
        #print("AQUI4")
        page.send(sender_id,"Feito")

'''
@page.handle_postback
def received_postback(event):
    sender_id = event.sender_id
    recipient_id = event.recipient_id
    time_of_postback = event.timestamp

    payload = event.postback_payload

    print("Received postback for user %s and page %s with payload '%s' at %s"
          % (sender_id, recipient_id, payload, time_of_postback))

    page.send(sender_id, "Postback called")
'''
@page.callback(['MENU_PAYLOAD/(.+)'])
def click_persistent_menu(payload, event):
  click_menu = payload.split('/')[1]
  if click_menu == 2:
      page.send(sender_id,"Y0")
  print("you clicked %s menu" % click_menu)

@page.handle_delivery
def received_delivery_confirmation(event):
    delivery = event.delivery
    message_ids = delivery.get("mids")
    watermark = delivery.get("watermark")

    if message_ids:
        for message_id in message_ids:
            print("Received delivery confirmation for message ID: %s" % message_id)

    print("All message before %s were delivered." % watermark)



@page.handle_read
def received_message_read(event):
    watermark = event.read.get("watermark")
    seq = event.read.get("seq")

    print("Received message read event for watermark %s and sequence number %s" % (watermark, seq))
