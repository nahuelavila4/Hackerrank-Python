import pyshark

def add_common_fields(packet):
    common_fields = {
        "src_ip": packet.ip.src,
        "dst_ip": packet.ip.dst,
    }
    return common_fields