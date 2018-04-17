#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import json
import argparse
import lib

def client(addr='localhost', port=7777):
    # Подключение к сокету
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((addr, port))
    # Сообщение серверу
    message = {
        'action': 'presense',
        'user': 'Max'
    }
    json_message = json.dumps(message)
    to_server = json_message.encode('utf-8')
    # Отправка сообщения
    sock.send(to_server)
    # Приём сообщения от сервера
    from_server = sock.recv(1024)
    print('Сервер отправил: ' + from_server.decode('utf-8'))
    # Закрытие сокета
    sock.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-a', action='store', nargs='?', const=1, \
                        type=str, help='IP адрес')
    parser.add_argument('-p', action='store', nargs='?', const=1, \
                        type=int, help='Номер порта')
    args = parser.parse_args()
    #print(lib.args_check(args.a, '1'))
    print(lib.addr_check(args.a))
    client(args.a if lib.addr_check(args.a) else '', \
           args.p if lib.port_check(args.p) else 7777)






