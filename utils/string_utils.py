import base64


def int_to_bytes(integer):
    firstByte = integer & 0xff
    secondByte = integer >> 8 & 0xff
    third = integer >> 16 & 0xff
    fourth = integer >> 24 & 0xff

    b = bytearray()
    b.append(firstByte)
    b.append(secondByte)
    b.append(third)
    b.append(fourth)
    return b


def bytes_to_int(bytearray):
        integer = 0
        i = 0
        for b in bytearray:
            integer = integer | (b << i)
            i = i+8
        return integer


# returns an integer given a base64 string
def decode_id(base64string):
    base64string += "="*((4-len(base64string) % 4) % 4)
    print(base64string)
    id = bytes_to_int(base64.b64decode(str(base64string)))
    print(id)
    return id


# encodes an integer to base64
def encode_id(integer_id):
    x = base64.encodebytes(int_to_bytes(integer_id))
    a = len(x)
    # since base64.encode bytes appends \n and replace returns a byte array
    return x[0:a - 2].decode('utf-8')
