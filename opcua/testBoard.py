from random import randint
import board
import time
import datetime

# Sensor-Library vom Hersteller Adafruit
import adafruit_dht

#GPIOs konfigurieren
import RPi.GPIO as GPIO

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

# alles ausschalten
GPIO.output(luefterPIN,GPIO.LOW)	
GPIO.output(ledPIN,GPIO.LOW)

# Startmeldung
print ("!!! Achtung es geht los !!!")

#GPIO.output(luefterPIN, GPIO.HIGH)

# LED 3 mal blinken lassen
GPIO.output(ledPIN,GPIO.HIGH)
time.sleep(1)
GPIO.output(ledPIN,GPIO.LOW)
time.sleep(1)
GPIO.output(ledPIN,GPIO.HIGH)
time.sleep(1)
GPIO.output(ledPIN,GPIO.LOW)
time.sleep(1)
GPIO.output(ledPIN,GPIO.HIGH)
time.sleep(1)
GPIO.output(ledPIN,GPIO.LOW)

# Test Sensor
print ("!!! Schritt2  -> Lesen des Sensors !!!")

# Device für Sensor
# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)
temperature_c = 0
humidity = 0

while True:
        #Zeit ermitteln
        TIME = datetime.datetime.now()

        # Temperatur messen
        try:
            # Print the values to Console
            temperature_c = dhtDevice.temperature
            humitidy = dhtDevice.humidity
            
            print(
                "Temp: {:.1f} C    Humidity: {}%  Zeit:{:s}".format(
                     temperature_c, humidity, TIME.strftime("%d-%b-%Y (%H:%M:%S.%f)")
                )
            )
            # physikalischen Lüfter anschalten
            GPIO.output(luefterPIN,GPIO.HIGH)
            ## LED anschalten	
            GPIO.output(ledPIN,GPIO.HIGH)
            break
 
        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
            time.sleep(2.0)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error        
        
        time.sleep(2)

print("!!! Schritt 3: Wenn LED an und Lüfter läuft --> Platine ok !!!")
print("\n\n")
print("!!! Warte 5 Sekunden .... !!!")
time.sleep(5)
print("!!! Schalte Lüfter und LED aus !!!")
# physikalischen Lüfter anschalten
#
GPIO.output(luefterPIN,GPIO.LOW)
GPIO.output(ledPIN,GPIO.LOW)

x = input("Beliebige Taste drücken, um das Programm zu beenden ...")
