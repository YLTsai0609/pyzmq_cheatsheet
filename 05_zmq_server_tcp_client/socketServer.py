from socket import socket, SOCK_STREAM, AF_INET, SOL_SOCKET, SO_REUSEADDR
from datetime import datetime
from time import sleep


# +

def main():
    server = socket(family=AF_INET, type=SOCK_STREAM)
    print('Socket created')
    HOST = ''
    PORT = 6555
    server.bind((HOST, PORT))
    server.listen(512)
    print('Start listening...')
    while True:
        client, addr = server.accept()
        print(str(addr) + 'get connection...')
        client.send(str(datetime.now()).encode('utf-8'))
        client.close()


# -

if __name__ == "__main__":
    main()


# ## send msh to non exist client?
# * client斷線了還能傳訊息嗎
# * 看起來default還可以傳兩次，之後會產生OSError - Broken Pipe

# +
def SingleThreadHeartBeat():
    server = socket(family=AF_INET, type=SOCK_STREAM)
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    print('Socket created')
    HOST = ''
    PORT = 6555
    server.bind((HOST, PORT))
    server.listen(5)
    print('Start listening...')
    try:
        while True:
            client, addr = server.accept()
            print(str(addr) + 'get connection...')
            while True:
                print('sending msg...')
                client.send(str(datetime.now()).encode('utf-8'))
                sleep(5)
    except OSError as e:
        print(e)
        client.close()


SingleThreadHeartBeat()
# -
