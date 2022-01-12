<h1 align="center">Socket Programming in Python </h1>
<h4 align="center">Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket(node) listens on a particular port at an IP, while the other socket reaches out to the other to form a connection. The server forms the listener socket while the client reaches out to the server. </h4>

<h2 align="center">Socket Programming Digram : </h2>
<a href="#"><img width="100%" height="auto" src="https://i.ibb.co/0VYJ0Jf/socket-diagram.png" height="175px"/></a>

<h4 align="left">1:- Server </h4>

```ruby
# first of all import the socket library
import socket
# next create a socket object
socket_obj = socket.socket()
# Next bind to the port
socket_obj.bind(('localhost', 8002))
# put the socket into listening mode
socket_obj.listen(4)
# Establish connection with client.
client_obj,address= socket_obj.accept()
# receive data from client
recv_msg = client_obj.recv(1024)
# Decode data
recv_msg.decode('utf-8')
# Print Data
print(recv_msg)
# Close the connection with the client
socket_obj.close()
```

<h4 align="left">1:- Client </h4>

```ruby
# import the socket library
import socket
# Create a socket object
socket_obj = socket.socket()
# connect to the server using host and port
socket_obj.connect(('localhost', 8002))
# input data
msg = str(input("Entter your message : "))
# encode and send the data from input data
socket_obj.send(msg.encode('utf-8'))
```

<h2 align="center">Here is the final result : </h2>

<a href="#"><img width="100%" height="auto" src="https://i.ibb.co/JxNdRBQ/Screenshot-from-2022-01-12-08-02-32.png" height="175px"/></a>

<a href="#"><img width="100%" height="auto" src="https://i.ibb.co/QdJQRZX/Screenshot-from-2022-01-12-08-02-56.png" height="175px"/></a>