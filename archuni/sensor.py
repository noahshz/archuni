import board
import adafruit_dht
import RPi.GPIO as GPIO
import time

class Sensor:
    _sensorPIN = 0
    _dhtDevice = None
    _temperature = 0

    def __init__(self) -> None:
        pass
    def setPIN(self, pin) -> None:
        self._sensorPIN = pin
        pass
    def prepare(self) -> None:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(True)

        GPIO.setup(self._sensorPIN, GPIO.IN)

        self._dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)
        self._temperature = 0

        print(f"Sensor prepared with sensor-pin {self._sensorPIN}")
        pass    
    def getTemp(self) -> float:
        try:
            self._temperature = self._dhtDevice.temperature
        except RuntimeError as error:
            print(error.args[0])
            time.sleep(1.0)
            return 0.0
        return self._temperature
