#necessary import for opcua connection
from opcua import Server

class Archuni:
    server = None
    client = None

    def __init__(self) -> None:
        self.server = Server()
        self.client = Client()

class Server:
    def __init__(self) -> None:
        # required variables for server config
        # ip address where server is running
        # namespace
        # objektname 
        # ordnernamen (temperatur, messdaten etc.)
        print("Server...")

class Client:
    def __init__(self) -> None:
        print("Client...")