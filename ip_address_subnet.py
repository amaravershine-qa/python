import ipaddress
def validate_ip_in_subnet(ip:str, cidr:str) -> bool:
    try:
        ip_object = ipaddress.ip_address(ip)
        network_object = ipaddress.ip_network(cidr, strict = False)
        return ip_object in network_object
    except ValueError:
        return False