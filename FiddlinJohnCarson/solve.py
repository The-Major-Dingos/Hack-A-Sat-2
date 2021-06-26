#!/usr/bin/env python3
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



