from archuni import Archuni

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