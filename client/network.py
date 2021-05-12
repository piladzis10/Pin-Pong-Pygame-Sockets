import socket
import pickle
class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.102"
        self.port = 5558
        self.addr = (self.server, self.port)


    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048*8))
        except:
            pass

    def send_recieve(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048*8))
        except socket.error as e:
            print(e)


