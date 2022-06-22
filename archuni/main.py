import time
from server import OPCUAServer
from sensor import Sensor

# Sensor wird vorbereitet
sensor = Sensor()
sensor.setPIN(4)
sensor.prepare()

# Server wird vorbereitet und gestartet
con = {
    'ip_address' : '10.62.255.50',
    'namespace' : 'archuni',
    'node' : 'robby',
    'folder' : 'board_sensor',
    'variable1' : 'temperature',
    'variable2' : 'humidity'
}

srv = OPCUAServer()
srv.loadConfig(con)
srv.start()
#srv.debug()

try:
    run = 0
    while True:
        temp = sensor.getTemp()
        humidity = sensor.getHumidity()

        #push temperature
        srv.push('var1', temp)
        #push humidity
        srv.push('var2', humidity)
        #debug
        print(f"Run: {str(run)} Temp: {temp} Humidty: {humidity}")
        run = run + 1

        time.sleep(1)
except KeyboardInterrupt:
    srv.stop()