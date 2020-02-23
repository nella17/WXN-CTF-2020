from hashlib import *
from string import printable

def enc(s):
    #s = s.encode()
    s224 = int(sha224(s).hexdigest(), 16)
    s256 = int(sha256(s).hexdigest(), 16)
    s384 = int(sha384(s).hexdigest(), 16)
    s512 = int(sha512(s).hexdigest(), 16)
    return (s224^s256^s384^s512) & 0xFFFFFFFF

can = printable
mp = {}
for i in can:
    for j in can:
        s = str(i)+str(j)
        mp[enc(s.encode())] = s

output = [int(x) for x in open('output', 'r').read().split()]
flag = ''.join([mp[x] for x in output])
print(flag)
