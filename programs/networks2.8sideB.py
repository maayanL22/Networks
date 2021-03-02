import socket
import time

def main():
    my_socket = socket.socket()
    port = 8111
    # my_socket.bind(('0.0.0.0', 8111))
    # my_socket.listen()
    is_server = False
    my_socket.connect(('127.0.0.1', port))
    print("Side B connected to port", port)

    while True:
        msg = input("Enter a message to send side A and end with the port number this side will listen to "
                    "when becoming the server:\n")
        my_socket.send(msg.encode())
        if msg == 'exit':
            break
        my_socket.close()
        my_socket = socket.socket()
        print("Side B disconnected")
        words = msg.split()
        length = len(words)
        next_port = words[length - 1]
        # print(int(next_port))
        # my_socket.bind(('0.0.0.0', int(next_port)))
        # print("Side B listening to port", next_port)
        is_server = True
        # print("lullulullululu")
        time.sleep(2)
        my_socket.bind(('0.0.0.0', int(next_port)))
        my_socket.listen()
        print("Side B listening to port", next_port)
        (client_socket, client_address) = my_socket.accept()
        cmsg = client_socket.recv(1024).decode()
        if cmsg == 'exit':
            break
        words1 = cmsg.split()
        length1 = len(words)
        next_port1 = words1[length1 - 1]
        words1[length1-1] = ''
        print("Side A:", ''.join(words1))
        my_socket.close()
        my_socket = socket.socket()
        is_server = False
        time.sleep(2)
        my_socket.connect(('127.0.0.1', int(next_port1)))

    print("Closing\n")
    client_socket.close()
    my_socket.close()


if __name__ == '__main__':
    main()
