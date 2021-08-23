import socket
import sys, traceback
import threading
import select
LISTASOCKET=[]
ENVIAR=[]
class Server(threading.Thread):
   def init(self):
        self.sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        self.sock.bind(('',5535))
        self.sock.listen(2)
        LISTASOCKET.append(self.sock)
        print ("Servidor iniciado na porta 5535")

        def run(self):
            while 1:
                read,write,err=select.select(LISTASOCKET,[],[],0)            
                for sock in read:
                    if sock==self.sock:                    
                        sockfd,addr=self.sock.accept()
                        print (str(addr))
                        LISTASOCKET.append(sockfd)
                        print (LISTASOCKET)
                    else:
                        try:
                            s=sock.recv(1024)
                            if s=='':
                                print (str(sock.getpeername()) )                           
                                continue
                            else:
                                ENVIAR.append(s)                                                      
                        except:
                            print (str(sock.getpeername()) )                     
class handle_connections(threading.Thread):
    def run(self):        
        while 1:
            read,write,err=select.select([],LISTASOCKET,[],0)
            for items in ENVIAR:
                for s in write:
                    try:
                        print ("Enviando para:  %s"%(str(s.getpeername())))
                        s.send(items)                                             
                        
                    except:
                        traceback.print_exc(file=sys.stdout)
                ENVIAR.remove(items)                 
if __name__=='main':
    srv=Server()
    srv.init()
    srv.start()
    print (LISTASOCKET)
    handle=handle_connections()    
    handle.start()   
