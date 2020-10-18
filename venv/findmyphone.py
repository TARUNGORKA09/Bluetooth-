from bluetooth import *

target_name= "My Phone"
target_address =  None

nearby_devices = discover_devices()

for address in nearby_devices:
    if target_name == lookup_name(address):
        target_address = address
        break

if target_address is not None:
    print("target address found",target_address)
else:
    print("target address not found")
