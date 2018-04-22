#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import socket
import lib
from threading import Thread

clients_list = []

def server(addr='localhost', port=7777):   
    # Подключение к сокету
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((addr, port))
    sock.listen(5)
    
    while True:
        # Слушает порт
        client, addr = sock.accept()
        clients_list.append(client)
        mmm = 'Получен запрос на соединение от ' + str(addr)
        print(mmm)
        #print('Получен запрос на соединение от ' + str(addr))
        new_client = Add_client(client, addr)
        new_client = new_client.new()
        new_client.start()
        
        # Реагирует на добавление нового клиента!
        for c in clients_list:
            c.send(mmm.encode('utf-8'))


class Add_client():
    def __init__(self, client, addr):
        self.cl = Thread(target=lambda: client_threading(client, addr))
    def new(self):
        return self.cl
    

def client_threading(client, addr):
    while True:
        # Отправляет последнее сообщение всем ото всех
        for c in clients_list:
            c.send((str(lib.messages[-1])).encode('utf-8'))

        # Принимает сообщение от клиента
        message = lib.get_message(client)
        
        if 'action' not in message \
        or 'user' not in message:
            client.send(lib.invalid_query.encode('utf-8'))
            #client.close()

        if message['action'] == 'presense':
            lib.presense(message, client)
            
        if message['action'] == 'msg':
            lib.msg(message, client)
             
    
if __name__ == '__main__':
    print('...connect...')
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-addr', action='store', nargs='?', const=1, \
                        type=str, help='IP адрес')
    parser.add_argument('-port', action='store', nargs='?', const=1, \
                        type=int, help='Номер порта')
    args = parser.parse_args()
    server(args.addr if args.addr else '', args.port if args.port else 7777)
    
    





