#necessary import for opcua connection
from opcua import Server

class Archuni:
    server = None
    client = None

    def __init__(self) -> None:
        self.server = Server()
        self.client = Client()

class Server:
    _config = None

    def __init__(self) -> None:
        # required variables for server config
        # ip address where server is running
        # namespace
        # objektname 
        # ordnernamen (temperatur, messdaten etc.)
        print("Server...")
    def loadConfig(self) -> bool:
        print("Sh")

class Client:
    def __init__(self) -> None:
        print("Client...")