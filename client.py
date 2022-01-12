import socket
import sys
import common_utils

def client(): 
    try:
        socket_obj = socket.socket()
        socket_obj.connect((common_utils.config.get('socket','host'), int(common_utils.config.get('socket', 'port'))))
        print(f"socket clinet is connected with : {common_utils.config.get('socket','host')}:{common_utils.config.get('socket','port')}")
        return socket_obj
    except Exception as e: 
        error = common_utils.get_error_traceback(sys, e)
        print (error)


def test_client():
    msg = str(input("Entter your message : "))
    client().send(msg.encode('utf-8'))

test_client()