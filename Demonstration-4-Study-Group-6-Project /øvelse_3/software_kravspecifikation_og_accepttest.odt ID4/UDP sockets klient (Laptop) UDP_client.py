from socket import socket
from socket import AF_INET
from socket import SOCK_DGRAM
from sys import exit

server_name = input("Input IP address/n>")
server_port = 12000
client_socket = socket(AF_INET, SOCK_DGRAM)

while True:
    try:
        message = input("message to send/n")
        client_socket.sendto(message.encode(), (server_name, server_port))    
        modified_message, server_address = client_socket.recvfrom(2048)
        print(modified_message.decode())
    
        
    except KeyboardInterrupt:
        print("CTRL-C pressed, closing down!")
        client_socket.close()
        exit()