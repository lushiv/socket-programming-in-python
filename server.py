import socket
def sever_conn(): 
    try: 
        socket_obj = socket.socket()
        socket_obj.bind(('localhost', 8002))
        socket_obj.listen(4)
        client_obj,address= socket_obj.accept()
        print("server is ready to accept connection")
        print(f"connected with this address{address}")
        return_conn = {
            'socketObj' : socket_obj,
            'clientObj' : client_obj,
            'address' : address
        }
        return return_conn
    except Exception as e: 
        print ("Socket server connetion error")


def test_server():
    conn = True
    while  conn:
        recv_msg = sever_conn().get('clientObj').recv(1024)
        recv_msg.decode('utf-8')
        print(recv_msg)
        if recv_msg == 'no':
            conn = False
            sever_conn().get('socketObj').close

test_server()