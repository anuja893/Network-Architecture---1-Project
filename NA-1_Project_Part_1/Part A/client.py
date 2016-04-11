import socket               # Import socket module
import sys


text = "y"
while text == "y":
  s = socket.socket()         # Create a socket object
  host = socket.gethostname() # Get local machine name
  port = 12345                # Reserve a port for your service.

  s.connect((host, port))
             
  text=input('Enter your mesage:') #take message input from user
  s.send(text.encode('ascii'))     #send message to client

  msg1=s.recv(1024)          #Recieve message from server
  msg1=msg1.decode('ascii')  #Decode the message from byte to string
 
  if msg1 == "bye from server":
   print("Message received was: " + msg1+".Closing connection !!")
   s.close  	# Close the socket when done
  else:
   pmsg1 = "Message received is: " + str(msg1)
   print(pmsg1)
   msgappend= "Echoed message: " + str(msg1)
   s.send(msgappend.encode('ascii'))
   msg2=s.recv(1024)
   msg2=msg2.decode('ascii')
   print(msg2)
   text = input("Do you want to continue ?(y/n)")#take message input from user
   if text == "y":
    s.send(text.encode('ascii'))
    continue
   else:
    s.send(text.encode('ascii'))
    dmsg=s.recv(1234)
    dmsg=dmsg.decode('ascii')
    if dmsg == "bye from server":
     print("Message received was: " + dmsg+".Closing connection !!")
     text= "bye from client" 
     s.send(text.encode('ascii'))
     s.close 
  


