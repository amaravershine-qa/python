import ipaddress

def validate_ip_address(address):
    ip = ipaddress.ip_address(address)
    if ip.version == 4:
        return True
    return False

print(validate_ip_address("192.168.1.1"))