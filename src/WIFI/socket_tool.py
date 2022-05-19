import os
import socket


class Client:
    def __init__(self, ip="127.0.0.0", port=8000, pw=None):
        self.sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(ip, port)
        self.client = self.sk.connect((ip, port))

    def send_msg(self, msg: str):
        self.client.send(msg.encode("utf-8"))
        a = self.client.recv(1024)
        if a.endswith("ack OK"):
            return a
        else:
            return "Wrong message"

    def rev_message(self):
        a= self.client.recv(1024)
        a = a.decode("utf-8")
        return a

class Service:
    def __init__(self, ip="127.0.0.1", port="8000", pw=None, listen=3):
        self.sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind = self.sk.bind((ip, port))
        self.sk.listen(listen)

    def set_listen(self, second=3):
        self.sk.listen(second)

    def rev_message(self):
        msg, b =  self.sk.accept()
        a = msg.recv(1024)
        print(a.decode("utf-8"))


def send_message(client: Client, message=None):
    a = client.send_msg(message)
    if a == "Wrong message":
        return Warning("the Message is Error")
    print("send OK")


def rev_message(ser: Service)-> str:
    temp = ser.rev_message()
    print(temp)