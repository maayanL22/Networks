import socket

IP = '127.0.0.1'
PORT = 5555

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect((IP, PORT))
print("Connected to localhost on port {}".format(PORT))

while True:
    name = input("Please enter your message:\n")
    my_socket.send(name.encode())
    if name == "":
        break
    data = my_socket.recv(1024).decode()
    print(data)

print("Closing")
my_socket.close()
