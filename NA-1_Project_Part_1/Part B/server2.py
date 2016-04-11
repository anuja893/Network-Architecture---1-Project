import socket
import sys

text=bytes("***********************ADDITIONAL LINE*****************************",'UTF-8')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)    
print ('Server listening....')

conn, addr = s.accept()
print ('Got connection from', addr)

with open('myTransfer.txt', 'wb+') as file_to_write:
    while True:
        print("Received File is:")
        data = conn.recv(3000000)
        print (data)
        if not data:
            break
        print ("\nDone !!\n")
        file_to_write.write(data)
        file_to_write.write(text)
		
        xyz=file_to_write.read()
        print (xyz)
        conn.sendall(data + text)
conn.close()