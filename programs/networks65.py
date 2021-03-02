import socket
import datetime

def main():
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_socket.sendto('Maayan'.encode(), ('127.0.0.1', 8821))
    sendtime = datetime.datetime.now()
    print(sendtime)
    (data, remote_address) = my_socket.recvfrom(1024)
    recvtime = datetime.datetime.now()
    print(recvtime)
    print("The server sent: ", data.decode())
    diff = recvtime - sendtime
    print("Time difference between sending and receiving is: ", diff)

    print("closing")
    my_socket.close()


if __name__ == '__main__':
    main()
