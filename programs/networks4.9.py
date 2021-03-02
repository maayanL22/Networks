import socket
import os

PORT = 80
REDIRECTION_DICTIONARY = {

}
FORBIDDEN_LIST = []


def handle_client_request(resource, client_socket):
    url = resource

    if url in REDIRECTION_DICTIONARY:
        # TO DO: send 302 redirection response
        response = "HTTP/1.0 302 - Moved Temporarily, please redirect to-" + REDIRECTION_DICTIONARY[url] + "\r\n"
        client_socket.send(response.encode())
        return

    if url in FORBIDDEN_LIST:
        client_socket.send("HTTP/1.0 403 - Forbidden\r\n".encode())
        return

    if 'html' in url:
        # print("line 41 html")
        filetype = 'html'
    elif 'jpg' in url:
        filetype = 'jpg'
    elif 'js' in url:
        filetype = 'js'
    elif 'css' in url:
        filetype = 'css'
    else:
        filetype = 'queryparams'

    if filetype == 'html':
        http_header = "HTTP/1.0 200 OK\r\n Content-Type: text/html; charset=utf-8\r\n"
    elif filetype == 'jpg':
        http_header = "HTTP/1.0 200 OK\r\n Content-Type: image/jpeg\r\n"  # TO DO: generate proper jpg header
    # TO DO: handle all other headers
    elif filetype == 'js':
        http_header = "HTTP/1.0 200 OK\r\n Content-Type: text/javascript; charset=UTF-8\r\n"
    elif filetype == 'css':
        http_header = "HTTP/1.0 200 OK\r\n Content-Type: text/css\r\n"
    else:  # unknown request
        # print("line 63")
        http_header = "HTTP/1.0 200 OK Content-Type: text/queryparams"
        # print("line 65")


    if '\\calculate-area' in url:
        urlist = url.split('?')
        if len(urlist) == 2:
            numl = urlist[1].split('&')
            if len(numl) == 2:
                heightlist = numl[0].split('=')
                widthlist = numl[1].split('=')
                if len(heightlist) != 2 or len(widthlist) != 2:
                    client_socket.send("400 - Bad Request".encode())
                    return
                elif not heightlist[1].isnumeric() or not widthlist[1].isnumeric():
                    client_socket.send("400 - Bad Request".encode())
                    return
                else:
                    area = (int(heightlist[1]) * int(widthlist[1])) / 2
                    response = http_header + str(area)
                    client_socket.send(str(area).encode())
                    return
            else:
                client_socket.send("400- Bad Request".encode())
                return
        else:
            client_socket.send("400- Bad Request".encode())
            return

    client_socket.send("500 - unknown server error".encode())
    return

def validate_http_request(request):
    if "\r" not in request or "\n" not in request:
        print("Illegal request protocol, closing server")
        return False, ''
    words = request.split()
    if len(words) < 3:
        print("Sorry, wrong request, disconnecting")
        return False, ''
    req = words[0]
    if req != 'GET':
        print("Wrong request, closing server")
        return False, ''
    ver = words[2]
    if 'HTTP/' not in ver or '1.1' not in ver:
        print("Wrong app protocol or version, disconnecting")
        return False, ''
    path = words[1]
    change = list(path)
    # for char1 in chng:
    # if char1 == '/':
    # char1 = '\''
    length = len(change)
    i = 0
    while i < length:
        if change[i] == '/':
            change[i] = '\\'
        i += 1
    winpath = ''.join(change)
    check = '\\calculate-area?height={}&width={}'
    if '\\calculate-area' not in winpath or '?height=' not in winpath or '&width=' not in winpath or '?' not in winpath:
        return False, '400'
    return True, winpath


def handle_client(client_socket):
    print('Client connected')
    while True:
        # TO DO: insert code that receives client request
        client_request = client_socket.recv(1024)
        valid_http, resource = validate_http_request(client_request.decode())
        if valid_http:
            print('Got a valid HTTP request')
            handle_client_request(resource, client_socket)
            break
        else:
            print('Error: Not a valid HTTP request')
            if resource == '400':
                client_socket.send("400 - Bad Request\r\n".encode())
            break
    print('Closing connection')
    client_socket.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', PORT))
    server_socket.listen()
    print("Server listening on port {}".format(PORT))
    while True:
        (client_socket, client_address) = server_socket.accept()
        print('New connection received')
        handle_client(client_socket)


main()
