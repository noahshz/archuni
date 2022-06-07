import time
from opcua import Server

class OPCUAServer:
    _config = {
        'ip_address' : '127.0.0.1',
        'namespace' : 'archuni',
        'node' : 'robby',
        'folder' : 'temp_sensor',
        'variable' : {'key' : 'temperatur', 'value' : '0.0'}
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

        '''
        self._server.set_security_policy([
            "asduizgas786t7td6as7t6asd7ftdas7fgt"
        ])
        '''

        #initialise opcua namespace
        self._namespace = self._server.register_namespace(self._config['namespace'])

        #initialise object (node) and add to namespace
        self._node = self._server.get_objects_node()
        self._object = self._node.add_object(self._namespace,self._config['node'])

        #create folder for object (node)
        self._folder = self._object.add_folder(self._namespace, self._config['folder'])

        #create opcua variable for sensor
        self._variable = self._folder.add_variable(self._namespace, self._config['variable']['key'],self._config['variable']['value'])
        self._variable.set_writable()

        print("-" * 100)
        print('Prepared server with config: ')
        for item in self._config:
            if item == 'variable':
                print('\t' + item + ' : ' + self._config[item]['key'] + " => " + self._config[item]['value'])
            else:
                print("\t" + item + " : " + self._config[item])
        print("-" * 100)
        pass
    def start(self) -> None:
        try:
            self._server.start()
        except:
            print("[Error] : Starting server failed...")
            pass
    def stop(self) -> None:
        self._server.stop()
        pass
    def push(self, value) -> None:
        self._variable.set_value(value)
        pass
    def loadConfig(self, config: dict) -> bool:
        if 'ip_address' in config and 'namespace' in config and 'node' in config and 'folder' in config and 'variable' in config:
            self._config = config
            return True
        else:
            print("[Error] : Missing parameter in passed config")
            return False
    def debug(self) -> None:
        print("Namespaces: " + ''.join(self._server.get_namespace_array()))
        #print("TEST: " + self._server.get_node_class())
