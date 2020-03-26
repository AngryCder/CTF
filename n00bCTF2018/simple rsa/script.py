import rsa,gmpy2

n = 697334695917848011908017064620798769199
e = 11
c= 589000442361955862116096782383253550042
p=24659183668299994531
q=28278904334302413829
phi=(p-1)*(q-1)
d = int(gmpy2.divm(1, e, phi))

def int2Text(number, size):
    text = "".join([chr((number >> j) & 0xff) for j in reversed(range(0, size << 3, 8))])
    return text.lstrip("\x00")

s=str(rsa.core.decrypt_int(c,d,n))

print(int2Text(int(s),len(s)))
