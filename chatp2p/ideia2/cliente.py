import threading  # Importa biblioteca que permite que a aplicação execute tarefas de forma assíncrona
import socket # Importa a biblioteca socket

host = '127.0.0.1'  # localhost
port = 5000 # Porta

username = input('Entre com seu username: ')  # Usuário escolhe seu apelido

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Implementa o TCP
cliente.connect((host, port))   # Conecta ao servidor

def recebe():   # Ouve o servidor e envia apelido para ele
    while True:
        try:
            mensagem = cliente.recv(1024).decode('utf-8')  # Recebe mensagem do servidor
            if mensagem == 'Apelido':
                cliente.send(username.encode('utf-8'))
            else:
                print(mensagem)
        except:
            print('Ocorreu um erro!')  # Quando ocorre erro encerra a conexão
            cliente.close()
            break

def escreve():  # Envia mensagens para o servidor
    while True:
        mensagem = '{}: {}'.format(username, input(''))
        cliente.send(mensagem.encode('utf-8'))

recebe_thread = threading.Thread(target=recebe)  # Inicia o Thread para ouvir o servidor
recebe_thread.start()

escreve_thread = threading.Thread(target=escreve)  # Inicia o Thread para escrever para o servidor
escreve_thread.start()
