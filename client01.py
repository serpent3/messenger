#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import argparse
import lib
import json
from message import Message
from threading import Thread

def client(addr='localhost', port=7777):
    # Подключение к сокету
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((addr, port))
    name = input('You name: ')
    user = Message(name)
    json_message = json.dumps(user.authenticate())
    byte_message = json_message.encode('utf-8')
    sock.send(byte_message)
    # Сообщение серверу
    while True:
        new_message = Add_message(sock)
        new_message = new_message.new()
        new_message.start()
        
        add_message(user, sock)
        

def add_message(user, sock):
    user.action = 'msg'
    user.mess = input('\n')
    user.send(sock)


def listner(sock):
    while True:
        mess = sock.recv(1024).decode('utf-8')
        if mess:
            print(mess)       


class Add_message():
    def __init__(self, sock):
        self.cl = Thread(target=lambda: listner(sock))
    def new(self):
        return self.cl

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-a', action='store', nargs='?', const=1, \
                        type=str, help='IP адрес')
    parser.add_argument('-p', action='store', nargs='?', const=1, \
                        type=int, help='Номер порта')
    args = parser.parse_args()
    client(args.a if args.a else '', args.p if args.p else 7777)




























