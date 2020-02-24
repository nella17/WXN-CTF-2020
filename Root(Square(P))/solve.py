from Crypto.Util.number import *
from topic import *
def sqrt(x):
    l = 1
    r = x
    while l != r-1:
        m = (l+r)//2
        if m**2 > x:
            r = m
        else:
            l = m
    return l
p = 3231660450893985129787028139151018035610437467522069485447060736495328441321407792079915113733222842630322770984020297415912649518117481856420586639729
phi_n = n*(p-1)//p
d = inverse(e, phi_n)
m = pow(c, d, n)
print(long_to_bytes(m).decode())
