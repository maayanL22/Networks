import socket
import protocol27

IP = '127.0.0.1'


def handle_response(my_socket, cmd):
    response = my_socket.recv(1024).decode()
    cmd_list = cmd.split()
    chk = cmd_list[0]
    if chk == 'DIR' and len(cmd_list) > 1:
        # print("123", cmd_list[1])
        # for file in response:
        # print(file, 'gh')
        print(response)
    elif chk == 'DELETE' or chk == 'COPY' or chk == 'EXECUTE':  # or chk == 'TAKE_SCREENSHOT':
        print(response)
    # elif chk == 'SEND_PHOTO':


def main():
    my_socket = socket.socket()
    my_socket.connect((IP, 8820))

    while True:
        print("Valid commands: DIR, DELETE, COPY, EXECUTE, EXIT")
        msg = input("Please enter the wanted command:\n")
        """
        instead in create_valid_msg in protocol
        
        length = str(len(msg))
        zfill_length = length.zfill(4)
        msg1 = zfill_length + msg
        """
        if protocol27.check_cmd(msg):
            packet = protocol27.create_valid_msg(msg)
            # print(packet)
            my_socket.send(packet)
            handle_response(my_socket, msg)
            if msg == 'EXIT':
                break
        else:
            cmd_list = msg.split()
            chk = cmd_list[0]
            print("Invalid command, please enter a valid command", cmd_list, "the message: ", msg)

    print("Closing")
    my_socket.close()


main()
