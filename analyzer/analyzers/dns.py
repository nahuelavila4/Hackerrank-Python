import pyshark
from common_fields import add_common_fields

def filter_dns_packets(packets):
    dns_packets = []
    for packet in packets:
        if "DNS" in packet:
            try:
                common_fields = add_common_fields(packet)
                name = packet.dns.qry_name
                qtype = packet.dns.qry_type
                response = packet.dns.a
                dns_packets.append({
                    "query_name": name,
                    "query_type": qtype,
                    "response": response
                })
            except AttributeError:
                continue
    return {**common_fields, **dns_packets}



