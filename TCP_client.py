# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 15:39:51 2021

@author: Ashok
"""


##Implemented The chatroom using TCP connection using same client code can make another client connection

import socket              
import threading


c = socket.socket()        
                

c.connect(('localhost', 9999))

print ("connected")

name = input('Enter tyour name\n')

def recv():
    while True:
        try:
            message = c.recv(1024).decode()
            if message == 'Enter Your Name':
                c.send(bytes(name,'utf-8'))
            else:
                print(message)
        except:
            print('an error occurred')
            c.close()
            break
            
            
def write():
    while True:
        message = name + ' : '+ input('')
        c.send(bytes(message,'utf-8'))
        
        if message[-4:] == 'exit':
            c.close()
            break


r_thread = threading.Thread(target = recv)
r_thread.start()
w_thread = threading.Thread(target = write)
w_thread.start()

