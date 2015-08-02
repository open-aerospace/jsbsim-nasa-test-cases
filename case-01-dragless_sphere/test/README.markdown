# NASA Test Case Data

The approach in the paper is to set up many different simulations engines to
compute the same conditions. Instead of comparing to a known output (in general
there isn't any way to come up with a perfect answer) the simulations were
compared to each other. The goal is good agreement between simulations.


## Data

NASA has provided the raw output data from six different simulators. A
[download of the raw data is available from NASA][1]. All six outputs
are also hosted here unedited. They are `NASA_Data_Atmos_01_sim_01.csv`
through `NASA_Data_Atmos_01_sim_06.csv`.

A script is provided `average.py` that will average all the cases output.
This was used to produce `NASA-testcase_atmos_01.csv` that is used in
[our overview of JSBSim's output][2]

[1]: http://nescacademy.nasa.gov/flightsim/ "Six degree-of-freedom (6-DOF) Flight Simulation Check-cases"
[2]: https://github.com/natronics/jsbsim-nasa-test-cases/blob/master/case-01-dragless_sphere/results.ipynb "IPython Notebook compairing NASA to JSBSim"
