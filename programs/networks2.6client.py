import socket


def main():
    my_socket = socket.socket()
    my_socket.connect(('127.0.0.1', 8820))

    while True:
        print("Please enter one of the next orders: TIME, WHORU, RAND, EXIT.")
        order = input()
        # if order != 'TIME' and order != 'WHORU' and order != 'RAND' and order != 'EXIT':
        # print("Invalid order")
        # break

        # else:
        length = str(len(order))
        zfill_length = length.zfill(2)
        order1 = zfill_length + order
        my_socket.send(order1.encode())

        resp = my_socket.recv(1024).decode()
        print("Server sent: ", resp)
        if order == 'EXIT':
            break

    print("Closing\n")
    my_socket.close()


main()
