import time
from server import OPCUAServer


srv = OPCUAServer()
srv.start()
#srv.debug()

try:
    run = 0
    while True:
        srv.push(10.0)
        #temperaturdaten
        print("Run: " + str(run))
        run = run + 1

        time.sleep(1)
except KeyboardInterrupt:
    srv.stop()