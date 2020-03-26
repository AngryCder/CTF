a =[72,73,75,84,85,87,104,105,107,116,117,119]
b =[97,98,99,100,101,102,103]
c =[97,98,99,100,101,103,106]
d =[65,72,74,75,77,79,90,97,104,106,107,109,111,122]
e =[66,67,78,79,84,85,88,89,98,99,110,111,116,117,120,121]
f =[104,105,106,107,108,109,110,111]
g =[112,113,114,117,118,119]

res = [bytearray([a1, b1, c1, d1, e1, f1, g1]) for a1 in a for b1 in b for c1 in c for d1 in d for e1 in e for f1 in f for g1 in g]

enc_bytes = bytearray([13,23,6,25,0,95,27,13,80,16,14,23,5,69,17,8,13,12,13,7,70,6,81,83,9,58,59,51,28,9,82,24,0,92,20,26])

def xor(data, key):
    l = len(key)
    decoded = bytearray()
    for i in range(0, len(data)):
        decoded.append(data[i]^key[i % l])
    return decoded.decode("ascii")
for key in res:
    ka =  xor(enc_bytes,key)
    if "n00bCTF"in ka:
        print(ka)
        break
