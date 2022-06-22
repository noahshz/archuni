import time
from opcua import ua,Server

class OPCUAServer:
    _config = {
        'ip_address' : '127.0.0.1',
        'namespace' : 'archuni',
        'node' : 'robby',
        'folder' : 'board_sensor',
        'variable1' : 'temperature',
        'variable2' : 'humidity'
    }

    def __init__(self) -> None:
        # required variables for server config
        # ip address where server is running
        # namespace
        # objektname
        # ordnernamen (temperatur, messdaten etc.)

        #initialise opcua server
        self._server = Server()
        self._server_url = "opc.tcp://"+ self._config['ip_address'] +":4840"
        self._server.set_endpoint(self._server_url)

        self._server.set_security_policy([
            ua.SecurityPolicyType.NoSecurity
        ])

        #initialise opcua namespace
        self._namespace = self._server.register_namespace(self._config['namespace'])

        #initialise object (node) and add to namespace
        self._node = self._server.get_objects_node()
        self._object = self._node.add_object(self._namespace,self._config['node'])

        #create folder for object (node)
        self._folder = self._object.add_folder(self._namespace, self._config['folder'])

        #create opcua variable for sensor temp and humidty
        # todo
        self._var1 = self._folder.add_variable(self._namespace, self._config['variable1'],'0')
        self._var2 = self._folder.add_variable(self._namespace, self._config['variable2'],'0')
        # self._var1.set_writable()
        # self._var2.set_writable()
        

        # self._variable = self._folder.add_variable(self._namespace, self._config['variable']['key'],self._config['variable']['value'])
        # self._variable.set_writable()

        print("-" * 100)
        print('Prepared server with config: ')
        for item in self._config:
            print("\t" + item + " : " + self._config[item])
        print("-" * 100)
        pass
    def start(self) -> bool:
        try:
            self._server.start()
            return True
        except:
            print("[Error] : Starting server failed...")
            return False
    def stop(self) -> bool:
        try:
            self._server.stop()
            return True
        except:
            print("[Error] : Verbindungsabbruch nicht möglich.")
            return False
    def push(self, var: str, value: float) -> None:
        if var == "var1":
            self._var1.set_value(value)
        if var == "var2":
            self._var2.set_value(value)
        pass
    def loadConfig(self, config: dict) -> bool:
        if 'ip_address' in config and 'namespace' in config and 'node' in config and 'folder' in config and 'variable1' in config and 'variable2' in config:
            self._config = config
            self.__init__()
            return True
        else:
            print("[Error] : Missing parameter in passed config")
            return False
    def debug(self) -> None:
        print("Namespaces: " + ''.join(self._server.get_namespace_array()))
        #print("TEST: " + self._server.get_node_class())
