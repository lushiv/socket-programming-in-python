import socket
import sys
import common_utils

def server(): 
    try: 
        socket_obj = socket.socket()
        socket_obj.bind((common_utils.config.get('socket','host'), int(common_utils.config.get('socket', 'port'))))
        print(f"socket server is running on : {common_utils.config.get('socket','host')}:{common_utils.config.get('socket','port')}")
        socket_obj.listen(4)
        return socket_obj
    except Exception as e:
        error = common_utils.get_error_traceback(sys, e)
        print (error)
        
def test_server():
    client_obj,address= server().accept()
    recv_msg = client_obj.recv(1024)
    recv_msg.decode('utf-8')
    print(recv_msg)

test_server()