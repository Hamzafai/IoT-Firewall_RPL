# detector/extractor.py

def extract_features(packet):
    """
    packet: dictionary containing packet fields
    return: list of features in EXACT training order
    """

    features = [
        packet.get("packet_duration", 0.0),
        packet.get("second_frame", 0),
        packet.get("length", 0),
        packet.get("src_ip_int", 0.0),
        packet.get("dest_ip_int", 0.0),
        packet.get("protocol_ICMPv6", 0),
        packet.get("protocol_IEEE_802_15_4", 0),
        packet.get("protocol_UDP", 0),
        packet.get("info_Ack", 0),
        packet.get("info_RPL_DIO", 0),
        packet.get("info_RPL_DIS", 0),
        packet.get("info_RPL_DAO", 0),
        packet.get("info_ultraseek_rrac", 0),
        packet.get("info_Unknown_17", 0)
    ]

    return [packet.get("second_frame", 0)]

