import time, random
from secret import flag
from string import printable

f = open('out.txt', 'w')

seed = int(time.time())
f.write(f'seed = {seed}\n')
random.seed(seed)

def rand():
    rnd = int(random.random() * (10 ** 5))
    print(f'rnd = {rnd}')
    while rnd:
        random.random()
        rnd -= 1
    return int(random.random() * 10 ** 5) & ((1 << 16) - 1)
    
def calc(ch, rnd):
    high = ch >> 4
    low = ch & 0xF

    _00 = (low << 4) | low
    _01 = (low << 4) | high
    _10 = (high << 4) | low
    _11 = (high << 4) | high
    
    val = 0
    val |= _00 << 12
    val |= _11 << 8
    val |= _01 << 4
    val |= _10 << 0

    res = 0
    res |= 0b0000111100001111 & (val ^ rnd)
    res |= 0b1111000011110000 & (val ^ rnd)
    res |= 0b0101010101010101 & (val ^ rnd)
    res |= 0b1010101010101010 & (val ^ rnd)

    return bin(res).lstrip('0b').zfill(16)

def all_different(val):
    lst = []
    for ch in printable:
        lst.append(calc(ord(ch), val))
    return len(lst) == len(set(lst))

for i in flag:
    _rand = rand()
    assert(all_different(_rand))
    res = calc(ord(i), _rand)
    f.write(f'{res}\n')


