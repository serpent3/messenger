# Проверка аргументов адреса и порта
import re
import json
import time
  
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

     
        
# Проверка сообщения сервером


# Провека ответа сервера клиентом

#
#