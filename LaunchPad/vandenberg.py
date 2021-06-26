import pwn

ticket = b"ticket{papa357695zulu2:GLhn4-pGFky18DciBZGuJyjhleoS-YTKdL0RrrnyhkpFY0FzlHmF7Xxi7CFaHBI_8w}"
p = pwn.remote('light-fever.satellitesabove.me', 5030)
p.recvuntil(b'Ticket please')
p.sendline(ticket)
challenge = p.recvuntil(b'= ?').decode().split('\n')[1].split(' ')[:3]
result = int(challenge[0]) + int(challenge[2])
p.sendline(str(result).encode())
print(p.recvuntil('}').decode().split('\n')[2])