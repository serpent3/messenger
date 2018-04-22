#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import time
import server01

     
        
def send_message(sock, message):
    json_message = json.dumps(message.form())
    byte_message = json_message.encode('utf-8')
    # Отправка сообщения
    sock.send(byte_message)
    
    
def get_message(client):
    from_client = client.recv(1024)
    json_message = json.loads(from_client.decode('utf-8'))
    #message = Message(name=json_message['user'], action=json_message['action'])
    return json_message


# Функция для действий при action == 'presense'
def presense(message, client):
    client.send(valid_query.encode('utf-8') )
    
messages = ['']
def msg(message, client):
    m = '\n{} написал(а): {}'.format(message['user']['account_name'], \
         message['message'])
    messages.append(m)


# Стандартные ответы
valid_query = json.dumps(
    {
        "response": 200,
        "time": time.time()
    })

invalid_query = json.dumps(
    {
        "response": 400,
        "time": time.time()
    })

probe_query = json.dumps(
    {
        "action": "probe",
        "time": time.time()
    })




    
    
    
    
    
    
    
