#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import socket
import json
   
def server(addr='localhost', port=7777):   
    # Подключение к сокету
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((addr, port))
    sock.listen(5)
    while True:
        # Слушает порт
        client, addr = sock.accept()
        print('Получен запрос на соединение от ' + str(addr))
        # Принимает сообщение от клиента
        from_client = client.recv(1024)
        json_message = json.loads(from_client.decode('utf-8'))
        print('Клиент отправил: ' + json_message['action'])
        # Отпрака сообщения клиенту
        to_client = ('Принято: ' + json_message['action']).encode('utf-8')
        client.send(to_client)
        # Закрытие сокета
        client.close()
    
    
if __name__ == '__main__':
    print('...connect...')
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-addr', action='store', nargs='?', const=1, \
                        type=str, help='IP адрес')
    parser.add_argument('-port', action='store', nargs='?', const=1, \
                        type=int, help='Номер порта')
    args = parser.parse_args()
    server(args.addr if args.addr else '', args.port if args.port else 7777)
    
    

