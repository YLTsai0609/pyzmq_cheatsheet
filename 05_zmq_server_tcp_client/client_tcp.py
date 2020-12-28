from socket import socket
client = socket()
#     client.connect(('192.168.0.176', 15679))
client.connect(('', 6555))
client.send(b'Hello')
print(client.recv(1024))
client.close()
