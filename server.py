"""
__Author__="Abenezer Mario"
__Title__= Group Project chat task 2
__Date__="11/20/2020"
Description: This file handles the server It uses 2 modules(Threading , and socket to create connection) 
server is running in a local  more documentation-->>

"""
import threading
import socket
import os.path
import sys

host = "127.0.0.1"

port = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host,port))

server.listen()

clients = []
profilename = []
#THis function handles the brodcasting of the messege sent to the clients
def broadcast(message):
    for client in clients:
        client.send(message)
# Handling Messages From Clients
def handle(client):#exception handleing while brodcasting
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = profilename[index]
            broadcast('{} left!'.format(nickname).encode('ascii'))
            profilename.remove(nickname)
            break
def receive():
    while True:
    
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))
        # Request And Store Nickname

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        profilename.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print("Nickname is {}".format(profilename))
        broadcast("{} joined!".format(profilename).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))


        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
receive()
