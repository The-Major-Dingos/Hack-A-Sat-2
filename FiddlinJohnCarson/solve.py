#!/usr/bin/env python3
import pwn
from skyfield.api import load
import datetime 
from skyfield.positionlib import ICRF

from astropy import units as u
from astropy import time 
from poliastro.bodies import Earth
from poliastro.twobody import Orbit


"""
Ticket please:
 ticket{papa440612kilo2:GFSCjjPSQF42fWhOZBXHOWfZ7nadoy8AETW-gIpwE88kfVtzzF7oxKfqBwGuLB3hMg} 
         KEPLER        
        CHALLANGE      
       a e i Ω ω υ     
            .  .       
        ,'   ,=,  .    
      ,    /     \  .  
     .    |       | .  
    .      \     / .   
    +        '='  .    
     .          .'     
      .     . '        
         '             
Your spacecraft reports that its Cartesian ICRF position (km) and velocity (km/s) are:
Pos (km):   [8449.401305, 9125.794363, -17.461357]
Vel (km/s): [-1.419072, 6.780149, 0.002865]
Time:       2021-06-26-19:20:00.000-UTC


What is its orbit (expressed as Keplerian elements a, e, i, Ω, ω, and υ)?

"""
datestr = "2021-06-26"
timestr = "19:20:00.00"
tz = "UTC"
print(u)
epoch = time.Time(datestr + " " + timestr)
print(epoch)
r = [8449.401305, 9125.794363, -17.461357] * u.km
v = [-1.419072, 6.780149, 0.002865] * u.km / u.s


#ts = load.timescale()

#eph = load('de421.bsp')
# t = ts.utc(2021, 6, 26, 19, 20)
#earth, sun = eph["earth"], eph["sun"]
# v = ICRF(Pos, Vel, t)


orb = Orbit.from_vectors(Earth, r, v)

print(orb.classical())
a, e, i, delta, w, v =  orb.classical()

print(a, e, i, delta, w, v)


ticket = b'ticket{papa440612kilo2:GFSCjjPSQF42fWhOZBXHOWfZ7nadoy8AETW-gIpwE88kfVtzzF7oxKfqBwGuLB3hMg}'

s = pwn.connect('derived-lamp.satellitesabove.me', 5013)
s.recvuntil('Ticket please:\n')
s.sendline(ticket)
# Semimajor axis, a (km): 12
# Eccentricity, e: 12
# Inclination, i (deg): 12
# Right ascension of the ascending node, Ω (deg): 12
# Argument of perigee, ω (deg): 12
# True anomaly, υ (deg): 12
s.recvuntil('a (km): ')
s.sendline(f'{a.value}'.encode())
s.recvuntil('e: ')
s.sendline(f'{e.value}'.encode())
s.recvuntil('i (deg): ')
s.sendline(f'{i.value}'.encode())
s.recvuntil('(deg): ')
s.sendline(f'{delta.value}'.encode())
s.recvuntil('(deg): ')
s.sendline(f'{w.value}'.encode())
s.recvuntil('(deg): ')
s.sendline(f'{v.value}'.encode())

print(s.recvuntil('}'))