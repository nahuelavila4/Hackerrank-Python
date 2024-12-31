# Maneja interaccion de .pcap usando el modulo pyshark

# workday: por cada analizador crear una función que reciba
# lista con los paquetes y devuelva solo los que coincidan con el protocolo
# y atributos que correspondan

import pyshark, os

ruta = os.path.dirname(os.path.abspath(__file__)) # Ruta de script


def load_pcap():
    ruta_archivo = os.path.join(ruta, "files_test/captura.pcapng")
    capture = pyshark.FileCapture(ruta_archivo)
    count = 0
    max_packets = 10
    for packet in capture:
        if count >= max_packets:
            break
        paquete_id = packet.number
         
        if hasattr(packet, "tcp"):
            puerto_origen, puerto_destino = packet.tcp.srcport, packet.tcp.dstport
        if hasattr(packet, "udp"):
            puerto_origen, puerto_destino = packet.udp.srcport, packet.udp.dstport            
        if hasattr(packet, "ip"):
            ip_origen, ip_destino = packet.ip.src, packet.ip.dst
            protocolo = packet.ip.proto
            print(f"Paquete {paquete_id}: Protocolo {protocolo}, IP Origen: {ip_origen}, IP Destino: {ip_destino}")
        count += 1


load_pcap()

