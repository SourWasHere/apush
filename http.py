import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 8080))
server.listen(10)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 8080))
client.send("._.".encode("UTF-8"))
clientdata = client.recv(1024)

while True:
    connection, address = server.accept()
    data = server.recv(1024).decode()
    if len(data) > 0:
        print(data)
        connection.close()
        break
