import socket
import sys
import time
import threading
class Server(threading.Thread):
    def run(self):
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print ("Servidor inicializado com sucesso!\n")
        hostname=''
        port=5535
        self.sock.bind((hostname,port))
        self.sock.listen(1)
        print ("Ouvindo porta: %d\n" %port)        
        #time.sleep(2)    
        (clientname,address)=self.sock.accept()
        print ("Conectando com: %s\n" % str(address) )       
        while 1:
            chunk=clientname.recv(4096)            
            print (str(address)+':'+chunk )
class Client(threading.Thread):    
    def connect(self,host,port):
        self.sock.connect((host,port))
    def client(self,host,port,msg):               
        sent=self.sock.send(msg)           
        print ("Enviado!\n")
    def run(self):
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            host=input("Qual o hostname?\n>>")            
            port=int(input("Qual a porta?\n>>"))
        except EOFError:
            print ("Erro!")
            return 1
        print ("Conectando...\n")
        s=''
        self.connect(host,port)
        print ("Conectado!\n")
        while 1:            
            print ("Esperando a mensagem...\n")
            msg=input('>>')
            if msg=='exit':
                break
            if msg=='':
                continue
            print ("Enviando...\n")
            self.client(host,port,msg)
        return(1)
if __name__=='main':
    srv=Server()
    srv.daemon=True
    print ("Iniciando o servidor...")
    srv.start()
    time.sleep(1)
    print ("Iniciando o cliente...")
    cli=Client()
    print ("Inicializacao concluida!")
    cli.start()
