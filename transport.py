import os
import sys
from socket import (
    socket,
    AF_INET,
    SOCK_STREAM
)
import argparse
from parser import Parser
from lexer import MSyntaxError
from cache import Cache

class MonoroServer(object):

    def __init__(self, host, port):
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.bind((host, port))
        #configure the socket to be listened
        self.sock.listen()
        
        self.running = True
        self.client = None
        self.parser = None
        self.cache = None
        
    
    def run(self):
        if self.running:
            while True:
                client, addr = self.sock.accept()
                print('Got connection from the %s' % str(addr))
                self.client = client
                if self.client:
                    self.handle_client()
    
    def handle_client(self):
        #wait for the client to senf the command
        self.client.send('Welcome to Monoro DB \n'.encode())
        self.cache = Cache()
        while True:
            self.client.send('>>>>'.encode())
            command = self.client.recv(1000)
            if command.decode().strip() == '':
                continue
        #parse the request
            if command.decode().strip() in ('EXIT', 'QUIT', 'exit', 'quit'):
                self.clean_up()
                break
            try:
                parser = Parser(command.decode().upper())
                message = parser.parse()

            
            except MSyntaxError as e:
                self.client.send(e.val.encode() + b'\n')
            else:
                print(message.proto)
                if message.proto == 'SET':
                    print('set is called')
                    self.cache[message.val.key] = message.val.val
                    print(self.cache)
                    #print(self.cache)
                    response = 'okk'
                if message.proto == 'GET':
                    
                    
                    #print(response)
                    response = self.cache.get(message.val, '')
                self.client.send(response.encode() + b'\n')
        return
        #self.clean_up()
    
    def clean_up(self):
        self.cache = None
        self.client.close()
        self.client = None

    def close(self):
        self.sock.close()
        self.sock = None

                


def main():
    parser = argparse.ArgumentParser(description='Monoro database helper')
    parser.add_argument('--host', dest='host', type=str, default='localhost')
    parser.add_argument('--port', dest='port', type=int, default=5000)

    args = parser.parse_args()
    server = MonoroServer(args.host, args.port)
    server.run()

if __name__ == '__main__':
    main()

