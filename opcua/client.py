from opcua import Client
from opcua.common import node
import time

client = Client("opc.tcp://10.26.10.1:4840")
try:
    client.connect()
except:
    print("Error. Keine Verbindung möglich.")

root = client.get_root_node()
#print(root)

node_luefter = client.get_node("ns=2;i=5")

node_temperatur = client.get_node("ns=2;i=4")
#print(node_leufter.get_value())


while True:
    if node_temperatur.get_value() > 21:
        print("Lüfter an.")
        node_luefter.set_value(1)
    else:
        print("Lüfter aus.")
        node_luefter.set_value(0)
    time.sleep(1)

#Manuelle Lüftersteuerung durch Input
""""
while True:
    inp = input("1/0: ")
    if inp == "1":
        print("Lüfter an.")
        node_luefter.set_value(1)
    else:
        print("Lüfter aus.")
        node_luefter.set_value(0)
    time.sleep(1)
"""