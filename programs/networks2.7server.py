import socket
import protocol27
import glob
import os
import shutil
import subprocess
import os.path

IP = '0.0.0.0'


def check_request(cmd):
    cmd_list = cmd.split()
    head = cmd_list[0]
    if head == 'EXIT' and len(cmd_list) < 2:
        return True
    param = cmd_list[1]
    if head != 'DIR' and head != 'DELETE' and head != 'COPY' and head != 'EXECUTE':
        return False
    elif not os.path.exists(param):
        print("lalalala")
        return False

    return True


def handle_request(cmd):
    cmd_list = cmd.split()
    head = cmd_list[0]
    if head == 'EXIT':
        return 'EXIT'
    param = cmd_list[1]
    if head == 'DIR':
        fin = cmd_list[1] + r'\*.*'
        files_list = glob.glob(fin)
        fstr = ''
        for file in files_list:
            fstr += str(file)
            fstr += '\n'
        return fstr
        # return "files list"
    elif head == 'DELETE':
        os.remove(cmd_list[1])
        return "File deleted"
    elif head == 'EXECUTE':
        subprocess.call(cmd_list[1])
        return "Executed"
    elif head == 'COPY':
        param1 = cmd_list[2]
        shutil.copy(param, param1)
        return "Copied"


def main():
    server_socket = socket.socket()
    server_socket.bind((IP, 8820))
    server_socket.listen()
    print("Server is up and running")

    (client_socket, client_address) = server_socket.accept()
    print("Client connected")

    while True:
        chk, length = protocol27.extract_msg(client_socket)
        if chk:
            req = client_socket.recv(length).decode()
            if check_request(req):
                response = handle_request(req)
                if req == 'EXIT':
                    client_socket.send("Exiting server".encode())
                    break
                else:
                    cmd_list = req.split()
                    head = cmd_list[0]
                    # print(cmd_list, "  ", head)
                    # print(response)
                    client_socket.send(response.encode())
            else:
                cmd_list = req.split()
                head = cmd_list[0]
                resp = "Invalid command or params, please enter a valid command " + head + " m " + req
                # print(cmd_list)
                client_socket.send(resp.encode())
        else:
            response = 'Packet not according to protocol'
            client_socket.send(response.encode())
            client_socket.recv(1024)

    print("Closing\n")
    client_socket.close()
    server_socket.close()


main()
