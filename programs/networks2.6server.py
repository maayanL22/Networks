import socket
from datetime import datetime
import random


def main():
    socket_server = socket.socket()
    socket_server.bind(('0.0.0.0', 8820))
    socket_server.listen()
    print("Server is up and running")

    (client_socket, client_address) = socket_server.accept()
    print("Client connected")

    while True:
        length = int(client_socket.recv(2).decode())
        data = client_socket.recv(length).decode()
        if data == 'TIME':
            replay = "Current time: " + str(datetime.now())
            client_socket.send(replay.encode())
        elif data == 'WHORU':
            replay = "My name is yoda :)"
            client_socket.send(replay.encode())
        elif data == 'RAND':
            replay = "Random number between 1 and 10: " + str(random.randint(1, 10))
            client_socket.send(replay.encode())
        elif data == 'EXIT':
            replay = "Exiting server"
            client_socket.send(replay.encode())
            break
        else:
            replay = "Wrong protocol"
            client_socket.send(replay.encode())

    print("Closing\n")
    client_socket.close()
    socket_server.close()


main()
