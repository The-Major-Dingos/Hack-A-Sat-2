from math import acos
import pwn
import numpy
from numpy.core.numeric import cross
from numpy.lib.function_base import angle
from pwnlib.tubes.sock import sock
from pyquaternion import Quaternion

vector_start = numpy.array([0., 0., 1.])
vector_end = numpy.array([0.14129425, -0.98905974, 0.04238827])

v = vector_start + vector_end
axis = numpy.cross(vector_start, vector_end)
rot = acos(vector_start.dot(vector_end))

print(axis, rot)

quat = Quaternion(axis=axis, angle=rot)

ticket = b'ticket{foxtrot535968kilo2:GMxkrTZhvhyyEzR2DBPwn9sLv-eaEbrlXiBAGfxFZrGaHEabAmhbHxo1U0xY539yVg}'

socket = pwn.connect('grave-error.satellitesabove.me', 5020)
socket.recvuntil('Ticket please:\n')
socket.sendline(ticket)
print(socket.recvuntil('Qx = ').decode())
print(f'{quat.x}')
socket.sendline(f'{quat.x}'.encode())
print(socket.recvuntil('Qy = ').decode())
print(f'{quat.y}')
socket.sendline(f'{quat.y}'.encode())
print(socket.recvuntil('Qz = ').decode())
print(f'{abs(quat.z)}')
socket.sendline(f'{abs(quat.z)}'.encode())
print(socket.recvuntil('Qw = ').decode())
print(f'{quat.w}')
socket.sendline(f'{quat.w}'.encode())
print(socket.recvuntil('}').decode())