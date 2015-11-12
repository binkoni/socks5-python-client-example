import socket
host = '127.0.0.1'
port = 9050
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect((host, port))
    print('connected')
    print('sent')
    sock.send(b'\x05\x01\x00')
    print(sock.recv(2))
    print('sent')
    sock.send(b'\x05\x01\x00\x03\x0Agonapps.io\x00\x50')
    print(sock.recv(10))
    sock.send(b'GET / HTTP/1.1\r\nHost: gonapps.io\r\n\r\n')
    print(sock.recv(1024))
    sock.close()

except OSError as error_message:
    print(error_message)
