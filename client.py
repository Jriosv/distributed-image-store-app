import socket
#import cv2
import pickle


HEADERSIZE = 10

IP = "127.0.0.1"
PORT = 50000

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((socket.gethostname(),1234))
#logo.jpg{0:pc1,1:pc2:2:pc3}

response = {}

while True:
    full_msg = b''
    new_msg = True
    while True:

        msg = client_socket.recv(1024)

        if(new_msg):
            msglen = int(msg[:HEADERSIZE].strip())
            new_msg = False
        full_msg += msg

        if len(full_msg)-HEADERSIZE == msglen:

            menu_option = input(full_msg[HEADERSIZE:].decode("utf-8"))
            if menu_option == '1':
                image_name = input("Enter the name of image that will be saved: ")
            if menu_option == '2':
                image_name = input("Enter the name of image that you want to download: ")

        response["client"] = '1'
        response["image_name"] = image_name
        response["action"] = menu_option
        response["state"] = 'request'

        encoded_msg = pickle.dumps(response)
        msg = bytes(f'{len(encoded_msg):<{HEADERSIZE}}',"utf-8") + encoded_msg
        client_socket.send(msg)
        print("message sended: ",msg)

        #d = pickle.loads(full_msg[HEADERSIZE:])
        #cv2.imshow('Logo OpenCV',d)
        #cv2.waitKey(5000)
        #cv2.destroyAllWindows()
        new_msg = True
        full_msg = b''

    print(full_msg)