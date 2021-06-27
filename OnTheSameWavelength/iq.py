import pwn

value = '01000011 01110010 01101111 01101101 01110101 01101100 01100101 01101110 01110100 00001010'.split()
answer = ''

def process_bits(b):
    if b == "00":
        return '-1.0 -1.0'
    elif b == "01":
        return '-1.0 1.0'
    elif b == "11":
        return '1.0 1.0'
    else:
        return '1.0 -1.0'

for x in value:
    for i, z in enumerate(x):
        if i % 2 == 0:
            answer += process_bits(f'{z}{x[i+1]}') + " "
answer = answer.strip()

ticket = b'ticket{november372626quebec2:GFj9LZlNE6LRUNwzj7NZdZlnsJ8EjzpZN3Ty61A818lngUPswpemshlhqVvMofulxA}'

s = pwn.connect('unique-permit.satellitesabove.me', 5006)
s.recvuntil('Ticket please:\n')
s.sendline(ticket)

print(s.recvuntil('Input samples: '))
s.sendline(answer.encode())

print(s.recvuntil('}'))
