# Проверка аргументов адреса и порта
import re
import json

def addr_check(addr):
    if re.findall(r'^\d*\.\d*\.\d*\.\d*$', addr) \
    or re.findall(r'^localhost$', addr) \
    or re.findall(r'', addr):
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
        self.message = {
        'action': action,
        'user': name
        }
        self.action = action
        self.user = name
    def form(self):
        return self.message
     
def send_message(sock):
    message = Message('Max')
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
    if message.action == 'presense':
        to_client = ('Вызов presense(message)'.encode('utf-8'))
        
    client.send(to_client)
     
        
# Проверка сообщения сервером


# Провека ответа сервера клиентом

#
#