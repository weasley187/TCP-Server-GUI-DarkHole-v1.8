# tcp server darkhole open source made by @weasleyRonald
# import required modules
import socket
import threading

# client binds
bind_port = 12
bind_ip = '1.1.1.1'

# create sockets
print('Server screened! {}:{}'.format(bind_ip, bind_port))
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)

# receive and send connection from the client
def handle_client_connection(client_socket):
    request = client_socket.recv(1024)
    client_socket.send('Welcome to DarkHole!')

while True:
    client_sock, address = server.accept()
    print ('{}:{} Has connected!'.format(address[0], address[1]))
    client_handler = threading.Thread(
        target=handle_client_connection,
        args=(client_sock,))
    client_handler.start()