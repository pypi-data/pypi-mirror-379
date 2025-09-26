import socket
import threading
import errno
import logging
from polypacket.transport.Transport import Transport

log = logging.getLogger(__name__)


class TcpTransport (Transport):
    def __init__(self, localPort, callback=None): 
        super().__init__(callback)
        self.localPort = localPort
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = 0
        self.mode = 'server'
        self.connection = None 
        self.client_address = None
        self.opened = False

    def __del__(self):
        self.socket.close()
        self.join()

    def close(self):
        self.socket.close()

    def connect(self, hostIp, hostPort):
        log.info(f"TCP trying {hostIp}:{hostPort}")
        self.host = (hostIp, hostPort)
        self.mode = 'client'
        try:
            self.socket.connect(self.host)
            self.opened = True
            log.info("TCP Connected")
            self.start()
        except Exception  as e:
            log.error(f"Connection failed: {e}")

    def listen(self):
        try:
            self.socket.bind(('', self.localPort))
            self.socket.listen(1)
            log.info(f"TCP Listening on port: {self.socket.getsockname()[1]}")
            self.start()
        except Exception  as e:
            log.error(f"Listen failed: {e}")

    def send(self, data):
        try:
            if self.mode == 'server':
                self.connection.sendall(data)
            else:
                self.socket.sendall(data)
        except Exception  as e:
            self.opened = False
            log.error(f"Send failed: {e}")

    def run(self):

        if self.mode == 'server':
            self.opened = True
            while True:
                self.connection, self.client_address = self.socket.accept()
                log.info(f"Connection Accepted: {self.client_address}")
                while True:
                    try:
                        data = self.connection.recv(1024)
                        if data:
                            self.callback(data)
                        else:
                            break
                    except IOError as e:  # and here it is handeled
                        log.debug(f"Server recv exception: {e}")
                        break
                log.info("TCP Disconnected")
                self.connection.close()
        else :#client
            while True:
                try:
                    data = self.socket.recv(1024)
                    if data:
                        self.callback(data)
                except IOError as e:  # and here it is handeled
                    log.debug(f"Client recv exception: {e}")
                    self.opened = False
                    break
                    if e.errno == errno.EWOULDBLOCK:
                        pass

tcpConnectionHelp = """
Invalid connection string. Options:

    [tcp:local-port] to listen on a port
    [tcp:host:remote-port] to target remote port on a host and use the default local port
    [tcp:local-port:host:remote-port] to target remote port on host and specify local hose
    [tcp:remote-port] to target port on local host
    [tcp:local-port:remote-port] to target port on local host, specifying local port
"""

def parseTcpConnectionString(connString):


    try:

        parts = connString.split(":")
        localPort = -1
        remoteHost = None
        remotePort = -1

        if len(parts) == 2:
            try:
                if(parts[1].isnumeric()):           #tcp:local_port
                    localPort = int(parts[1])   
                else:                                #tcp:remote_ip:remote_port
                    remoteHost = parts[1]
                    remotePort = int(parts[2])

            except:
                return None
        elif len(parts) == 3:
            try:
                remoteHost = parts[1]
                remotePort = int(parts[2])
            except:
                return None
        elif len(parts) == 4:
            try:
                localPort = int(parts[1])
                remoteHost = parts[2]
                remotePort = int(parts[3])
            except:
                return None
        else:
            return None
        
        return {'localPort': localPort, 'remoteHost': remoteHost, 'remotePort': remotePort}

    except:

        return None