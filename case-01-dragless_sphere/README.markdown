
# Case 1: Dragless Sphere

The initial atmospheric check-case scenario called for a small sphere to be
dropped from an initial position located 30,000 ft over the Equator/Prime
Meridian intersection. Its initial linear velocity should have matched the
Earth’s eastward rotation rate at that altitude so that it was initially
motionless (in a linear sense) with respect to the still atmosphere; however,
it should have had zero inertial rotation; thus it had a small residual
rotation relative to the Earth below and the atmosphere surrounding it.

The sphere’s orientation was chosen such that the body x-axis was pointed north,
the body z-axis was initially pointed down, with the body y-axis completing the
orthogonal right-hand-rule by pointing east. Thus the vehicle would have had a
small amount of ‘roll rate’ with respect to the rotating Earth. The sphere is
imagined to have no reaction with the atmosphere - no damping, and no drag; it
will accelerate downward toward the ellipsoidal Earth in response to
second-harmonic (J2) gravitation as a function of its geometric height. This is
achieved by setting the coefficient of drag (CD) to zero for this scenario.


 Condition                              | Type
 -------------------------------------- | ------------------------------------
 **Vehicle**                            | Dragless sphere
 **Geodesy**                            | WGS-84 rotating
 **Atmosphere**                         | US 1976 STD; no wind
 **Gravitation**                        | J<sub>2</sub>
 **Duration**                           | 30 s
 **Initial states:**                    | Geodetic, Local-relative Body axes
  &mdash; Position [deg, deg, ft MSL]   | `[0, 0, 30000]`
  &mdash; Velocity [ft/s]               | `[0, 0, 0]`
  &mdash; Attitude [deg]                | `[0, 0, 0]`
  &mdash; Rate [deg/s]                  | `[-0.004178073, 0, 0]`
  **Notes**                             | CD set to zero


# Simulation Results

First look at provided NASA test case:



/usr/lib/python2.7/dist-packages/matplotlib/__init__.py:874: UserWarning: axes.color_cycle is deprecated and replaced with axes.prop_cycle; please use the latter.
  warnings.warn(self.msg_depr % (key, alt_key))



![](results_files/results_1_1.png)


Looks like the sphere fell. Great! We'll investigate the other numbers later.


# JSBSim Output

And now we look at our output:




![](results_files/results_3_0.png)


So our ball also dropped. Looks like it's working. In all cases, the data should be so close that looking at the raw output won't be useful. Instead we want to look at the difference between the NASA data and our simulation:

# Comparisons

Pointwise diff the two results:




![](results_files/results_5_0.png)


JSBSim Last Position Diff: -0.00013 ft


JSBsim ended up off by about `-0.00013` feet (~`-0.04` mm) over a fall of 14,000 feet!




![](results_files/results_7_0.png)


Looks like numerical noise (IEEE float round error). Nothing to see here...




![](results_files/results_9_0.png)


There was a fair amount of divergence in the sim tools for this value. It didn't seem to bother the authors at this scale.




![](results_files/results_11_0.png)





![](results_files/results_12_0.png)



