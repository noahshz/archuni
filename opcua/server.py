from opcua import ua, uamethod, Server
from opcua.ua import ObjectIds
import netifaces as ni

import time
import datetime
import board
import adafruit_dht
import RPi.GPIO as GPIO

server=Server()
#Get the ip address
IPV4_Address = "10.26.10.1"
ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']
url="opc.tcp://"+IPV4_Address+":4840"
server.set_endpoint(url)

server.set_security_policy([
    ua.SecurityPolicyType.NoSecurity
])

#OPCUA Namensraum festleben
name="OPCUA_Musterplatine"
addspace=server.register_namespace(name)

node = server.get_objects_node()

#Objekt Raspi im Namensraum festlegen
Raspi=node.add_object(addspace,"Raspi")

#Ordner für das Objekt Raspi anlegen
myfolder = Raspi.add_folder(addspace, "Temperatursensor")
myfolder2 = Raspi.add_folder(addspace, "Luefter")

#OPUA Datenpunkte "TempSensor1" festlegen
Sensor1 = myfolder.add_variable(addspace,"DHT22",20.1)
Luefter1 = myfolder2.add_variable(addspace,"Luefter1",0)
Time = node.add_variable(addspace,"Time",0)

Luefter1.set_writable()

#OPCUA-Server starten
server.start()
print(f"Server startet auf {url}")

# Definition der GPIOs
sensorPIN = 4
luefterPIN = 13
ledPIN = 23

# Zählweise der Pins festlegen
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#GPIO Eingänge festlegen
GPIO.setup(sensorPIN, GPIO.IN)

#GPIO Ausgänge festlegen
GPIO.setup(luefterPIN, GPIO.OUT)
GPIO.setup(ledPIN, GPIO.OUT)

TIME = datetime.datetime.now()

GPIO.output(luefterPIN,GPIO.LOW)	
GPIO.output(ledPIN,GPIO.LOW)

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)
temperature_c = 0
humidity = 0

while True:
    try:
        TIME = datetime.datetime.now()
        temperature_c = dhtDevice.temperature
        humitidy = dhtDevice.humidity

        print(
            "Temp: {:.1f} C    Humidity: {}%  Zeit:{:s}".format(
                temperature_c, humidity, TIME.strftime("%d-%b-%Y (%H:%M:%S.%f)")
            )
        )

        Sensor1.set_value(temperature_c)
        if Luefter1.get_value() == 1:
            GPIO.output(luefterPIN,GPIO.HIGH)
        else:
            GPIO.output(luefterPIN,GPIO.LOW)
        pass
    except:
        pass

    
    time.sleep(1)
    pass
