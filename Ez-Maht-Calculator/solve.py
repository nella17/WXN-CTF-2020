from pwn import *

r = remote('final.ctf.bitx.tw', 30003)
r.recvuntil('!\n')
for i in range(500):
    x = r.recvuntil(' =').decode('utf-8').strip().split(' =')[0]
    c = eval(x)
    print(x+' = '+str(c))
    r.sendafter('Answer = ', str(c)+'\n')

r.interactive()
