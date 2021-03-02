import socket
import time

def main():
    my_socket = socket.socket()
    port = 8111
    my_socket.bind(('0.0.0.0', port))
    my_socket.listen()
    print("Side A listening to port", port)
    is_server = True
    (client_socket, client_address) = my_socket.accept()

    while True:
        # time.sleep(6)
        cmsg = client_socket.recv(1024).decode()
        if cmsg == 'exit':
            break
        words = cmsg.split()
        length = len(words)
        print(length, words)
        next_port = words[length - 1]
        words[length-1] = ''
        print("Side B:", ''.join(words))
        my_socket.close()
        my_socket = socket.socket()
        is_server = False
        # time.sleep(4)
        # print("lalalalallala" , next_port)
        # my_socket.connect(('127.0.0.1', int(next_port)))
        msg = input("Enter a message to send side B and end with the port number this side will connect to "
                    "when becoming the server:\n")
        time.sleep(3)
        my_socket.connect(('127.0.0.1', int(next_port)))
        my_socket.send(msg.encode())
        if msg == 'exit':
            break
        my_socket.close()
        my_socket = socket.socket()
        print("Side A disconnected")
        words1 = msg.split()
        length1 = len(words1)
        next_port1 = words1[length1 - 1]
        my_socket.bind(('0.0.0.0', int(next_port1)))
        my_socket.listen()
        print("Side A listening to port", next_port1)
        is_server = True
        (client_socket, client_address) = my_socket.accept()

    print("Closing\n")
    client_socket.close()
    my_socket.close()


if __name__ == '__main__':
    main()
