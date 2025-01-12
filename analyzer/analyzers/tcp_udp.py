import pyshark
from common_fields import add_common_fields

def filter_tcp_packets(packets):
    for packet in packets:
        tcp_packets = []
        udp_packets = []
        common_fields = add_common_fields(packet)
        try:
            if "TCP" in packet:
                tcp_info = analyze_tcp(packet)
                tcp_packets.append({**common_fields, **tcp_info})
            elif "UDP" in packet:
                udp_info = analyze_udp(packet)
                udp_packets.append({**common_fields, **udp_info})
        except AttributeError:
            continue
    return tcp_packets, udp_packets

def analyze_tcp(packet):
    return {
        "src_port": packet.tcp.srcport,
        "dst_port": packet.tcp.dstport,
        "flags": packet.tcp.flags,
        "seq_num": packet.tcp.seq,
        "ack_num": packet.tcp.ack
    }

def analyze_udp(packet):
    return {
        "src_port": packet.udp.srcport,
        "dst_port": packet.udp.dstport,
        "payload": getattr(packet.udp, "payload", "N/A")
    }