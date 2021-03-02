import socket
import select
import msvcrt

IP = '127.0.0.1'
PORT = 5555

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect((IP, PORT))
print("Connected to localhost on port {}".format(PORT))

sock_list = [my_socket]
messages = []
text = []

print("Enter message to the chat whenever you want, enter exit to disconnect")

while True:
    rlist, wlist, xlist = select.select(sock_list, sock_list, [])

    if rlist:
        # print('hola')
        message = my_socket.recv(2048).decode()
        print(message)

    if msvcrt.kbhit():
        data = msvcrt.getch().decode()
        # print(data)
        # if data == "":
        # break
        if data == '\r':
            if ''.join(text) == 'exit':
                break
            messages.append(''.join(text) + '\n')
            text = []
            print("$$", messages, "$$")
        else:
            text.append(data)

    if wlist:
        for m in messages:
            my_socket.send(m.encode())
            messages.remove(m)

print("closing")
my_socket.close()
