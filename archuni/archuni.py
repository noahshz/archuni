#necessary import for opcua connection
from opcua import Server

class Archuni:
    server = None
    client = None

    def __init__(self) -> None:
        self.server = Arch_Server()
        self.client = Arch_Client()

class Arch_Server:
    _config = {
        'ip_address' : '127.0.0.1',
        'namespace' : 'archuni',
        'node' : 'robby',
        'folder' : 'temp_sensor',
        'variables' : {'temperatur' : '0.0'}
    }

    def __init__(self) -> None:
        # required variables for server config
        # ip address where server is running
        # namespace
        # objektname
        # ordnernamen (temperatur, messdaten etc.)
        
        self._server_url = "opc.tcp://"+ self._config['ip_address'] +":4840"

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



        pass
    def loadConfig(self, config: dict) -> bool:
        if 'ip_address' in config and 'namespace' in config and 'node' in config and 'folder' in config and 'variables' in config:
            self._config = config
        else:
            print("[Error] : Missing parameter in passed config")
            exit()

class Arch_Client:
    def __init__(self) -> None:
        pass