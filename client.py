
"""
__Author__="Abenezer Mario, Yoonjae Gyae"
__Title__= Group Project chat task 2
__Date__="11/20/2020"
Description: This file handles the client It uses 2 modules(Threading , and socket to create connection) 
client will be connected to server according to the number of requestes it gets. more documentation-->>

"""
import socket
import threading
import sys
import os.path

# Choosing Nickname
nickname = input("Choose your nickname: ")
# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 4444))
# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break
# Sending files to the server 
def sendfile():
    text = input("")#takes input from the user 
    if text[0] == ">":#speciy with this character to add the text and open it.
        file = open(text[1:], "rb")#opens a text file based on the user input and change it to a binary
        return file.read(1024)#
    return text#returns a text which is passed to the write function to be sent to the server


#writing and sending messages including file to the server
def write():
    while True:
        message = '{}: {}'.format(nickname, sendfile())
        client.send(message.encode('ascii'))
        # Starting Threads For Listening And Writing
    
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()