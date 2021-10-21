# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 21:45:34 2021

@author: Ashok

"""

#Implemented The chatroom using TCP connection

import socket             #importing socket library  
import threading         #importing thread library

#creating socket for server

s = socket.socket()          

#binding server to adress and port
           
s.bind(('localhost',9999))    
   
print('waiting for connection')

clients = []
names = []

#listening for client connection

s.listen(10000)

#sending message

def msg(message):
    for i in clients:
        i.send(bytes(message,'utf-8'))

#

def box(c):
    while True:
        
        try:
            message = c.recv(1024).decode()
            if message[-4:] == 'exit':
                index = clients.index(c)
                clients.remove(c)
                c.close()
                name=names[index]
                msg( name +' left the chat !!')
                names.remove(name)
                
            else:
                msg(message)
                
        except:
            print('disconnected.. !')
            break

#infinite loop for server to oprn 24x7                

def connection():
    
    while True:
        c, addr = s.accept()     
        print ('Got connection from', addr)
       # c.send(bytes('Thank you for connecting','utf-8'))
        
        c.send(bytes('Enter Your Name','utf-8'))
        name=c.recv(1024).decode()
        print(name, 'joined .')
        
        clients.append(c)
        names.append(name)
        msg(name + ' joined chat !!')
        
        thread=threading.Thread(target = box , args = ((c,) ))
        thread.start()
        

connection()
