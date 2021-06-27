import datetime
from astropy import units as u
from astropy import time as a_time
from astropy.utils import data

from poliastro.bodies import Earth
from poliastro.twobody import Orbit
from poliastro.maneuver import Maneuver

'''
What we know:
    Satellite's x,y,z ICRF corrdinate
    Satellite's Velocity Vector
    Current time at the Satellite's position
    Geostationary orbit is a=42164+/-10km, e<0.001, i<1deg

What we need:
    Time when the maneuver is to be executed
    ∆v of each direction (x, y, z)
    New orbit must have a semimajor axis value of 42164±10
'''

# Data we have
r = [8449.401305, 9125.794363, -17.461357] * u.km
v = [-1.419072, 6.780149, 0.002865] * u.km / u.s
time = a_time.Time.strptime('2021-06-26-19:20:00.000000', '%Y-%m-%d-%H:%M:%S.%f')



orb = Orbit.from_vectors(Earth, r, v, time)

# Find the lowest point, calculate a circular orbit there.
# Once found, calculate the Hohmann transfer between the low orbit and the high orbit
# This should give you the amount of delta-v and time to burn
print(orb)
print(orb.period.value / 2)
print(orb.r_a)
print(orb.r_p)
print(orb.t_p)
# 2021-06-27-00:12:59.166031-UTC
time_since_perigee = orb.t_p.value  # Time since lowest part of the orbit in seconds
duration_to_reach_apogee = orb.period.value / 2  # Time it takes from lowest to highest point in seconds
perigee_distance = orb.r_p.value #  Distance from 0,0,0 to the lowest position in the orbit
apogee_distance = orb.r_a.value #  Distance from 0,0,0 to the highest position in the orbit

time_to_apogee = duration_to_reach_apogee - time_since_perigee
# timestamp_at_apogee = time + datetime.timedelta(0, time_to_apogee)

data_at_apogee = orb.propagate(time_to_apogee * u.s)

my_velocity = data_at_apogee.v
needed_velocity = Orbit.circular(Earth, 42164 * u.km).v

print(my_velocity, needed_velocity)

print(a_time.Time.strftime(data_at_apogee.epoch, '%Y-%m-%d-%H:%M:%S.%f') + "-UTC")

