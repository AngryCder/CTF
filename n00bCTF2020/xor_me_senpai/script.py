encryp_f = open("secretzz.png","rb")
enc_bytes =bytearray(encryp_f.read())
img = open("flag.png", "wb")

def xor(data, key):
    l = len(key)
    decoded = bytearray()
    for i in range(0, len(data)):
        decoded.append(data[i]^key[i % l])
    return decoded


decry_b = xor(enc_bytes,bytearray(b'n00b=='))
img.write(decry_b)
