import threading  # Importa biblioteca que permite que a aplicação execute tarefas de forma assíncrona
import socket # Importa a biblioteca socket

host = '127.0.0.1'  # localhost
port = 5000    # Porta

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Implementa o TCP
servidor.bind((host, port)) # Servidor enxerga o IP e a porta
servidor.listen()  # Servidor escuta

clientes = []  # Lista para agregar os clientes
usernames = []  # Lista para agregar os nomes de usuários

def broadcast(mensagem):  # Envia mensagens em broadcast
    for cliente in clientes:
        cliente.send(mensagem)

def tratamento(cliente):  # Tratamento das mensagens
    while True:
        try:
            mensagem = cliente.recv(1024) # Mensagem em broadcast

        #    if (mensagem == 'sair'):
#
        #        quit()
#
        #    else:
        #        destinatario = mensagem.split('')[0]
        #        if destinatario.starswith('/'):
        #            destino = destinatario.string[1, len(destinatario) - 1]
        #            envio_mensagem(cliente, destinatario, mensagem)
        #            continue

            broadcast(mensagem)
        except:
            index = clientes.index(cliente)
            clientes.remove(cliente)
            cliente.close()
            username = usernames[index]
            broadcast('{} saiu'.format(username).encode('utf-8'))
            usernames.remove(username)
            break

#def busca_destino(clientes, destinatario):
#    for destinatario in clientes:
#        return destinatario in clientes
#
#def busca_remetente(clientes, remetente):
#    for remetente in clientes:
#        return remetente in clientes
#
#def env_priv(remetente, destinatario, mensagem):
#    if remetente == destinatario:
#        mensagem = 'Você não pode enviar um mensagem para si mesmo!'
#    else:
#        mensagem = '<' + remetente + '> <Privado> : ' + mensagem
#
#    envio_mensagem(cliente, destinatario, mensagem)
#
#def envio_mensagem(cliente, username, mensagem):
#    try:
#        cliente.send(mensagem.encode('utf-8'))
#    except:
#        pass

def recebe():  # Função para receber mensagens
    while True:
        cliente, endereco = servidor.accept()  # Aceitando conexão
        print('{} foi conectado!'.format(str(endereco)))

        cliente.send('Apelido'.encode('utf-8')) # Requerimento do nome de usuário
        username = cliente.recv(1024).decode('utf-8')
        usernames.append(username)
        clientes.append(cliente)

        print('Usuário é {}'.format(username))
        broadcast('{} entrou!'.format(username).encode('utf-8'))
        cliente.send('Conectado no servidor!'.encode('utf-8'))

        thread = threading.Thread(target=tratamento, args=(cliente,))
        thread.start()

recebe()
