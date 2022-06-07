from opcua import Client
import time

class OPCUAClient:
    _client = None

    def __init__(self) -> None:
        self._client = None
        pass
    def connect(self, ipaddress: str) -> bool:
        self._client = Client(f"opc.tcp://{ipaddress}:4840")

        try:
            self._client.connect()
            return True
        except:
            print("[Error] : Keine Verbindung möglich.")
            return False
    def disconnect(self) -> bool:
        try:
            self._client.disconnect()
            return True
        except:
            print("[Error] : Verbindungsabbrcuh nicht möglich.")
            return False
    def pull(self, nodeid: str) -> str:
        if 'ns=' not in nodeid or ';i=' not in nodeid:
            print("[Error] : NodeID invalid. Bitte überprüfen.")
            return None
        data = self._client.get_node(nodeid)

        return data.get_value()

opc = OPCUAClient()
opc.connect("127.0.0.1")

print(opc.pull("ns=2;i=3"))

opc.disconnect()