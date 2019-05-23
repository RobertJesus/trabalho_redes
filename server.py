from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread


# classe para manipular o socket
class Send:
    def __init__(self):
        self.__message = ''
        self.new = True
        self.connection = None

    def put(self, message):
        self.__message = message
        if self.connection != None:
            # envia um mensagem atravez de uma connectionexão socket
            self.connection.send(str.encode(self.__message))

    def get(self):
        return self.__message

    def loop(self):
        return self.new


# função wait - Thread
def wait(tcp, send, host='', port=5000):
    origem = (host, port)
    # cria um vinculo
    tcp.bind(origem)
    # deixa em espera
    tcp.listen(1)

    while True:
        # aceita um connectionexão
        connection, client = tcp.accept()
        print('cliente ', client, ' conexao')
        # atribui a conexão ao manipulador
        send.connection = connection

        while True:
            # aceita uma mensagem
            message = connection.recv(1024)
            if not message: break
            print(str(message, 'utf-8'))


if __name__ == '__main__':
    # cria um socket
    tcp = socket(AF_INET, SOCK_STREAM)
    send = Send()
    # cria um Thread e usa a função wait com dois argumentos
    process = Thread(target=wait, args=(tcp, send))
    process.start()

    print('Iniciando o servidor!')
    print('Aguardando conexão do cliente!')

    message = input()
    while True:
        send.put(message)
        message = input()

    process.join()
    tcp.close()
    exit()