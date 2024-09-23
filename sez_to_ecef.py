# sez_to_ecef.py
#
# Usage: sez_to_ecef.py o_lat_deg o_lon_deg o_hae_km s_km e_km z_km
#  Text explaining script usage
# Parameters:
#  o_lat_deg:
#  o_lon_deg: 
#  o_hae_km:
#  s_km: 
#  e_km: 
#  z_km:
#
# Output:
#  A description of the script output
#
# Written by: Alwaleed Alrashidi
#
#
# import Python modules
# e.g., import math # math module
import sys # argv
import math
import numpy #matrix math

# "constants"
# e.g., R_E_KM = 6378.137

# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
o_lat_deg = float('nan') # Origin Latitude in Degrees
o_lon_deg = float('nan') # Origin Longitude in Degrees
o_hae_km = float('nan') # Origin Height above ellipsoid in km
s_km = float('nan') # South Coordinate
e_km = float('nan') # East Coordinate
z_km = float('nan') # Zenith Corrdinate

# parse script arguments
if len(sys.argv)==7:
    o_lat_deg = float(sys.argv[1])
    o_lon_deg = float(sys.argv[2])
    o_hae_km  = float(sys.argv[3])
    s_km = float(sys.argv[4])
    e_km = float(sys.argv[5])
    z_km = float(sys.argv[6])
else:
    print(\
     'Usage: '\
     'python3 sez_to_ecef.py o_lat_deg o_lon_deg o_hae_km s_km e_km z_km'\
    )
    exit()

o_lat_rad = math.radians(o_lat_deg)
o_lon_rad = math.radians(o_lon_deg)

# write script below this line
R_y = numpy.array([[math.sin(o_lat_rad), 0,math.cos(o_lat_rad)], 
                   [0.0,1.0,0.0],
                   [-math.cos(o_lat_rad),0,math.sin(o_lat_rad)]]) 
R_z = numpy.array([[math.cos(o_lon_rad),-math.sin(o_lon_rad),0],
                   [math.sin(o_lon_rad), math.cos(o_lon_rad),0],
                   [0.0,0.0,1.0]]) 
sez_vector = numpy.array([[s_km],
                          [e_km],
                          [z_km]]) 
first_rotation = R_y.dot(sez_vector)
second_rotation = R_z.dot(first_rotation)
ecef_x_km = second_rotation[0]
ecef_y_km = second_rotation[1]
ecef_z_km = second_rotation[2]

print(ecef_x_km)
print(ecef_y_km)
print(ecef_z_km)
