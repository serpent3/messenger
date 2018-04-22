#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import time
# Делатель сообщений
class Message():
    def __init__(self, name, action='presense', passw='', \
                 to='', room='', mess=''):
        self.action = action
        self.user = name
        self.passw = passw
        self.to = to
        self.mess = mess
        
    def authenticate(self):
        self.message = {
        'action': self.action, # authenticate
        'time': time.time(),
        'user': {
            'account_name': self.user,
            'password': self.passw
            }
        }            
        return self.message        
    
    def presense(self):
        self.message = {
        'action': self.action, # presense
        'time': time.time(),
        'message': self.mess,
        'user': {
            'account_name': self.user,
            'status': self.passw
            }
        }            
        return self.message     
    
    def user_to_user(self):
        self.message = {
        'action': self.action, # msg
        'time': time.time(),
        'to': self.to,
        'from': self.user,
        'message': self.mess
        }
        return self.message      
      
    # Старый общий метод 
    def form(self):
        self.message = {
        'action': self.action,
        'time': time.time(),
        'user': {
            'account_name': self.user,
            'status': self.passw
            }
        }             
        return self.message
    
    def send(self, sock):
        json_message = json.dumps(self.presense())
        byte_message = json_message.encode('utf-8')
        sock.send(byte_message)        
    