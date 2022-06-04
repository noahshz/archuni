from opcua import Client
import time

client = Client("opc.tcp://127.0.0.1:4840")
try:
    client.connect()
except:
    print("Error. Keine Verbindung möglich.")
    exit()



root = client.get_root_node()

test = client.get_node('ns=2;i=84')

print(test.get_value())

#print(test.get_value())

client.disconnect()