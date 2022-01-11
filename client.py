import socket



def client_conn(): 
    try:
        socketObj = socket.socket()
        socketObj.connect(('localhost', 8002))
        return socketObj
    except Exception as e: 
        print ("Socket clinet connetion error")


def test_client():
    conn = True
    while  conn:
        msg = str(input("Entter your message : "))
        client_conn().socketObj.send(msg.encode('utf-8'))
        if msg == 'no':
            conn = False
            client_conn().socketObj.close


test_client()