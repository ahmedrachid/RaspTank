import socket, threading

LOCALHOST = ""
PORT = 9000

controllers ={}     #robot name/ socket 
robots = {}
#connection = {socketspc : socket robot}
class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("New connection added: ", clientAddress)
    def run(self):
        print ("Connection from : ", clientAddress)
        #self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        msg = ''
        global robots
        global controllers 
        currentRobotName = None
        while True:
            data = self.csocket.recv(2048)
            msg = data.decode()
            if not data :
              break  
            try:
                cmd,param = msg.split(" ")
            except:
                cmd = msg
            if cmd =="connect":
                print('Received:', param)
                # check the name of robot
                #if param not in robots:

                #    self.csocket.sendall("Unkhnown".encode())
                #else :
                controllers[param]= self.csocket
                #    self.csocket.sendall("ok".encode())
                print(controllers)
                print(robots)
            
            elif cmd == "register":
                #if param in robots:
                   # self.csocket.sendall("already used".encode())
                #else :
                print('Received: ', param)
                robots[param]=self.csocket
            elif cmd == 'malus':
                indice = len(list(robots.keys()))-1
                print('Sending malus command to Robot')
                robots[list(robots.keys())[indice]].send('stop'.encode())
            else :
                for k,v in controllers.items():
                    if v == self.csocket:
                        currentRobotName = k 
                print('Sending command {} to Robot {}'.format(cmd, currentRobotName))
                robots[currentRobotName].send(str(cmd).encode())
                #currentSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                #currentSocket.connect(("192.168.1.200", 10223))
                #currentSocket.send("forward".encode())
                

                    
    

            ##print ("from client", msg)
            
            self.csocket.send(bytes(msg,'UTF-8'))
        print ("Client at ", clientAddress , " disconnected...")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()
