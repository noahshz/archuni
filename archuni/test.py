from opcua import Client

client = Client("opc.tcp://127.0.0.1:4840")
try:
    client.connect()
except:
    print("Error. Keine Verbindung möglich.")



client.disconnect()
print("uzasgd")