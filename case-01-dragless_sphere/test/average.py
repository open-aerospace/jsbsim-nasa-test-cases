#!/usr/bin/env python
import numpy as np


# SIM 01
columns = np.loadtxt("NASA_Data_Atmos_01_sim_01.csv", delimiter=',', unpack=True, comments="t")

s1_times              = columns[ 0]
s1_altitudeMsl        = columns[ 7]
s1_longitude          = columns[ 8]
s1_latitude           = columns[ 9]
s1_localGravity       = columns[10]
s1_eulerAngle_Roll    = columns[13]
s1_altRate            = columns[17]
s1_speedSound         = columns[18]
s1_mach               = columns[28]


# SIM 02
columns = np.loadtxt("NASA_Data_Atmos_01_sim_02.csv", delimiter=',', unpack=True, comments="t")

s2_times              = columns[ 0]
s2_altitudeMsl        = columns[ 4]
s2_longitude          = columns[ 5]
s2_latitude           = columns[ 6]
s2_localGravity       = columns[ 7]
s2_eulerAngle_Roll    = columns[10]
s2_altRate            = columns[14]
s2_speedSound         = columns[15]
s2_mach               = columns[25]


# SIM 03
columns = np.loadtxt("NASA_Data_Atmos_01_sim_03.csv", delimiter=',', unpack=True, comments="t")

s3_times              = columns[ 0]
s3_altitudeMsl        = columns[ 7]
s3_longitude          = columns[ 8]
s3_latitude           = columns[ 9]
s3_localGravity       = columns[10]
s3_altRate            = columns[11]
s3_speedSound         = columns[12]


# SIM 04
columns = np.loadtxt("NASA_Data_Atmos_01_sim_04.csv", delimiter=',', unpack=True, comments="t")

s4_times              = columns[ 0]
s4_altitudeMsl        = columns[10]
s4_longitude          = columns[11]
s4_latitude           = columns[12]
s4_localGravity       = columns[13]
s4_eulerAngle_Roll    = columns[16]
s4_speedSound         = columns[20]


# SIM 05
columns = np.loadtxt("NASA_Data_Atmos_01_sim_05.csv", delimiter=',', unpack=True, comments="t")

s5_times              = columns[ 0]
s5_altitudeMsl        = columns[13]
s5_longitude          = columns[14]
s5_latitude           = columns[15]
s5_localGravity       = columns[16]
s5_eulerAngle_Roll    = columns[19]
s5_altRate            = columns[23]
s5_speedSound         = columns[24]


# SIM 06
columns = np.loadtxt("NASA_Data_Atmos_01_sim_06.csv", delimiter=',', unpack=True, comments="t")

s6_times              = columns[ 0]
s6_altitudeMsl        = columns[13]
s6_longitude          = columns[14]
s6_latitude           = columns[15]
s6_localGravity       = columns[16]
s6_eulerAngle_Roll    = columns[19]
s6_altRate            = columns[23]
s6_speedSound         = columns[24]




# Average all sims
averages = []
for i, t in enumerate(s1_times):
    averages.append((
        "%4.1f" % t,
        "%0.16f" % ((s1_altitudeMsl[i]     + s2_altitudeMsl[i]     + s3_altitudeMsl[i]     + s4_altitudeMsl[i]     + np.interp(t, s5_times, s5_altitudeMsl)     +  np.interp(t, s6_times, s6_altitudeMsl)) / 6.0),
        "%0.16f" % ((s1_longitude[i]       + s2_longitude[i]       + s3_longitude[i]       + s4_longitude[i]       + np.interp(t, s5_times, s5_longitude)       +  np.interp(t, s6_times, s6_longitude))   / 6.0),
        "%0.16f" % ((s1_latitude[i]        + s2_latitude[i]        + s3_latitude[i]        + s4_latitude[i]        + np.interp(t, s5_times, s5_latitude)        +  np.interp(t, s6_times, s6_latitude))    / 6.0),
        "%0.16f" % ((s1_eulerAngle_Roll[i] + s2_eulerAngle_Roll[i]                         + s4_eulerAngle_Roll[i] + np.interp(t, s5_times, s5_eulerAngle_Roll) +  np.interp(t, s6_times, s6_eulerAngle_Roll)) / 5.0),
        "%0.16f" % ((s1_localGravity[i]    + s2_localGravity[i]    + s3_localGravity[i]    + s4_localGravity[i]    + np.interp(t, s5_times, s5_localGravity)    +  np.interp(t, s6_times, s6_localGravity)) / 6.0),
        "%0.16f" % ((s1_altRate[i]         + s2_altRate[i]         + s3_altRate[i]                                 + np.interp(t, s5_times, s5_altRate)         +  np.interp(t, s6_times, s6_altRate)) / 5.0),
        "%0.16f" % ((s1_speedSound[i]      + s2_speedSound[i]      + s3_speedSound[i]      + s4_speedSound[i]      + np.interp(t, s5_times, s5_speedSound)      +  np.interp(t, s6_times, s6_speedSound)) / 6.0),

    ))

print "# time [s], Altitude_MSL [ft], Longitude [deg], Latitude [deg], Roll [deg], Local Gravity [ft/s/s], Altitude Rate WRT MSL [ft/min], Speed of Sound [ft/s]"
for line in averages:
    print ','.join(line)
