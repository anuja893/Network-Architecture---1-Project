import socket

HOST =socket.gethostname()
PORT = 12345            
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST,PORT))

g=open('Upload.txt','rb')
data=g.read()
socket.sendall(data)
print("Sending File")

data=socket.recv(3000000)
print("Received file is\n")
print(data)

print('end')



socket.close()
