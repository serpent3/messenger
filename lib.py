# Проверка аргументов адреса и порта
import re
import json
import time

def addr_check(addr):
    if re.findall(r'^\d*\.\d*\.\d*\.\d*$', str(addr)) \
    or re.findall(r'^localhost$', str(addr)) \
    or re.findall(r'', str(addr)):
        return addr
    else:
        return False
    
def port_check(port):
    if type(port) == int \
    and port > 1024 and port < 49151:
        return port
    else:
        return False
    
# Делатель сообщений
class Message():
    def __init__(self, name, action='presense', mess=''):
        self.action = action
        self.user = name
        
    def form(self):
        self.message = {
        'action': self.action,
        'time': time.time(),
        'user': self.user  
        }            
#        self.message = json.dumps(self.message)
#        self.message = self.message
        return self.message
     
def send_message(sock, message):
    json_message = json.dumps(message.form())
    byte_message = json_message.encode('utf-8')
    # Отправка сообщения
    sock.send(byte_message)
    
def get_message(client):
    from_client = client.recv(1024)
    json_message = json.loads(from_client.decode('utf-8'))
    message = Message(name=json_message['user'], action=json_message['action'])
    return message

def presense(message, client):
    client.send(('200' + str(message.form())).encode('utf-8'))
     
        
# Проверка сообщения сервером


# Провека ответа сервера клиентом

#
#