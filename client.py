import socket
import cv2
import pickle


HEADERSIZE = 10

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(),1236))
#logo.jpg{0:pc1,1:pc2:2:pc3}

while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(1024)
        if(new_msg):
            print(f"new message length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False
        full_msg += msg
        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg recvd")
            print(full_msg[HEADERSIZE:])
            d = pickle.loads(full_msg[HEADERSIZE:])
            cv2.imshow('Logo OpenCV',d)
            cv2.waitKey(5000)
            cv2.destroyAllWindows()
            new_msg = True
            full_msg = b''
    print(full_msg)