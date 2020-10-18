import sys
from bluetooth import *

service_matches = find_service(name="Bluetooth Serial Port",uuid=SERIAL_PORT_CLASS)

if len(service_matches)==0:
    print("couldn't find the service")
    sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("connecting to ",host)

sock = BluetoothSocket(L2CAP)
sock.connect((host,port))

sock.send("Hello!!")

sock.close()