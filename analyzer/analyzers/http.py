import pyshark
from common_fields import add_common_fields

def filter_http_packets(packets):
    http_packets = []
    for packet in packets:
        try:
            if 'HTTP' in packet:
                common_fields = add_common_fields(packet)
                method = packet.http.request_method
                host = packet.http.host
                uri = packet.http.request_full_uri
                http_packets.append({
                    "method": method,
                    "host": host,
                    "uri": uri
                })
                return {**common_fields, **http_packets} # Combina los dic en uno solo
        except AttributeError:
            continue






