import time
from server import OPCUAServer
from sensor import Sensor

#Sensor wird vorbereitet
sensor = Sensor()
sensor.setPIN(4)
sensor.prepare()

con = {
    'ip_address' : '10.62.255.50',
    'namespace' : 'archuni',
    'node' : 'robby',
    'folder' : 'temp_sensor',
    'variable' : {'key' : 'temperatur', 'value' : '0.0'}
}


srv = OPCUAServer()
srv.loadConfig(con)
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