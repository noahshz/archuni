import time
from server import OPCUAServer
from sensor import Sensor

#Sensor wird vorbereitet
sensor = Sensor()
sensor.setPIN(4)
sensor.prepare()

srv = OPCUAServer()
srv.start()
#srv.debug()

try:
    run = 0
    while True:
        temp = sensor.getTemp()
        #push sensor daten
        srv.push(temp)
        #temperaturdaten
        print(f"Run: {str(run)} Temp: {temp}")
        run = run + 1

        time.sleep(1)
except KeyboardInterrupt:
    srv.stop()