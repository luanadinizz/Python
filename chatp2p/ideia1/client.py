import socket
import sys
import time
import threading
import select
import traceback
class Server(threading.Thread):
    def initialise(self,receive):
        self.receive=receive
    def run(self):
        lis=[]
        lis.append(self.receive)
        while 1:
            read,write,err=select.select(lis,[],[])
            for item in read:
                try:
                    s=item.recv(1024)
                    if s!='':
                        chunk=s                
                        print (str('')+':'+chunk)
                except:
                    traceback.print_exc(file=sys.stdout)
                    break
class Client(threading.Thread):    
    def connect(self,host,port):
        self.sock.connect((host,port))
    def client(self,host,port,msg):               
        sent=self.sock.send(msg)           
        #print "Sent\n"
    def run(self):
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
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
        receive=self.sock
        time.sleep(1)
        srv=Server()
        srv.initialise(receive)
        srv.daemon=True
        print("Iniciando a comunicacao!")
        srv.start()
        while 1:            
            #print "Waiting for message\n"
            msg=input('>>')
            if msg=='exit':
                break
            if msg=='':
                continue
            #print "Sending\n"
            self.client(host,port,msg)
        return(1)
if __name__=='main':
    print ("Iniciando cliente...")
    cli=Client()    
    cli.start()
