from archuni import Archuni
import time
from server import OPCUAServer

'''
op = Archuni()


config = {
    'ip_address' : '192.168.0.1',
    'namespace' : 'archuni',
    'node' : 'projekt',
    'folder' : 'roller',
    'variable' : {'speed' : '100'}
}

#op.server.loadConfig(config)
op.server.start()

try:
    run = 0
    while True:
        op.server.push(10)
        print("Run: " + str(run))
        run = run + 1

        time.sleep(1)
except KeyboardInterrupt:
    op.server.stop()
'''

srv = OPCUAServer()

srv.start()

srv.debug()

try:
    run = 0
    while True:
        srv.push(10)
        #temperaturdaten
        print("Run: " + str(run))
        run = run + 1

        time.sleep(1)
except KeyboardInterrupt:
    srv.stop()