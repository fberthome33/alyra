
def getVarInt(data):
    firstOctet = str(data[0]);
    firstIndex = 0;
    varint_len = 0;
    if firstOctet == 'fd':
        firstIndex = 1;
        varint_len = 3;
    elif firstOctet == 'fe':
        firstIndex = 1;
        varint_len = 5;
    elif firstOctet == 'ff':
        firstIndex = 1;
        varint_len = 9;
    else:
        firstIndex = 0;
        varint_len = 1;

    return varint_len, int.from_bytes(data[firstIndex:varint_len], byteorder='little');