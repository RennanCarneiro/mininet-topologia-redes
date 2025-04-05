# -*- coding: utf-8 -*-
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.cli import CLI
from mininet.log import setLogLevel

class Router(Node):
    def config(self, **params):
        super(Router, self).config(**params)
        self.cmd('sysctl -w net.ipv4.ip_forward=1')  # Habilita roteamento
    def terminate(self):
        self.cmd('sysctl -w net.ipv4.ip_forward=0')
        super(Router, self).terminate()

class CustomTopo(Topo):
    def build(self):
        # Hosts
        h1 = self.addHost("h1", ip="192.168.1.10/24")
        h2 = self.addHost("h2", ip="192.168.2.10/24")
        h3 = self.addHost("h3", ip="192.168.3.10/24")
        h4 = self.addHost("h4", ip="192.168.4.10/24")
 	# Roteadores
        r1 = self.addNode("r1", cls=Router)
        r2 = self.addNode("r2", cls=Router)
        r3 = self.addNode("r3", cls=Router)
	# Conexões hosts → roteadores
	self.addLink(h1, r1, intfName2='r1-eth0')
	self.addLink(h2, r2, intfName2='r2-eth0')
	self.addLink(h3, r3, intfName2='r3-eth1')
	self.addLink(h4, r3, intfName2='r3-eth2')
 	# Conexões entre roteadores
        self.addLink(r1, r2,
                     intfName1='r1-eth1', params1={'ip': '10.0.0.1/30'},
                     intfName2='r2-eth1', params2={'ip': '10.0.0.2/30'})
        self.addLink(r2, r3,
                     intfName1='r2-eth2', params1={'ip': '10.0.1.1/30'},
                     intfName2='r3-eth0', params2={'ip': '10.0.1.2/30'})

def run():
    topo = CustomTopo()
    net = Mininet(topo=topo, controller=None)
    net.start()

# Acesso aos roteadores
    r1 = net.get('r1')
    r2 = net.get('r2')
    r3 = net.get('r3')

# Acesso aos hosts
    h1 = net.get('h1')
    h2 = net.get('h2')
    h3 = net.get('h3')
    h4 = net.get('h4')

 # IPs nos roteadores
    r1.setIP('192.168.1.1/24', intf='r1-eth0')
    r1.setIP('10.0.0.1/30', intf='r1-eth1')

    r2.setIP('192.168.2.1/24', intf='r2-eth0')
    r2.setIP('10.0.0.2/30', intf='r2-eth1')
    r2.setIP('10.0.1.1/30', intf='r2-eth2')

    r3.setIP('10.0.1.2/30', intf='r3-eth0')
    r3.setIP('192.168.3.1/24', intf='r3-eth1')
    r3.setIP('192.168.4.1/24', intf='r3-eth2')

# Configurações de gateway nos hosts
    h1.cmd('ip route add default via 192.168.1.1')
    h2.cmd('ip route add default via 192.168.2.1')
    h3.cmd('ip route add default via 192.168.3.1')
    h4.cmd('ip route add default via 192.168.4.1')

# Rotas no r1
    r1.cmd('ip route add 192.168.2.0/24 via 10.0.0.2')
    r1.cmd('ip route add 192.168.3.0/24 via 10.0.0.2')
    r1.cmd('ip route add 192.168.4.0/24 via 10.0.0.2')
    r1.cmd('ip route add 10.0.1.0/30 via 10.0.0.2') 

# Rotas no r2
    r2.cmd('ip route add 192.168.1.0/24 via 10.0.0.1')
    r2.cmd('ip route add 192.168.3.0/24 via 10.0.1.2')
    r2.cmd('ip route add 192.168.4.0/24 via 10.0.1.2')

# Rotas no r3
    r3.cmd('ip route add 192.168.1.0/24 via 10.0.1.1')
    r3.cmd('ip route add 192.168.2.0/24 via 10.0.1.1')
    r3.cmd('ip route add 10.0.0.0/30 via 10.0.1.1')


# Adicionar rotas estáticas aqui
    
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
