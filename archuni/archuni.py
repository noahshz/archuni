#necessary import for opcua connection
from opcua import ua, uamethod, Server
from opcua.ua import ObjectIds
import netifaces as ni

import time
import datetime
import board
import adafruit_dht
import RPi.GPIO as GPIO

class Archuni:
    server = None
    client = None

    def __init__(self) -> None:
        self.server = Server()
        self.client = Client()

        print("Hello World!")

class Server:
    def __init__(self) -> None:
        print("Server")

class Client:
    def __init__(self) -> None:
        print("Client")