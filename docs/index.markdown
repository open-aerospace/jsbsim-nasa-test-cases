---
layout: project
title: "JSBSim: NASA Test Cases"
description: Doing it
page: jsbsimtest
---

# JSBSim: NASA Test Cases

In 2015 NASA [published a paper][testcases] that compared many different internal simulation tools, used on real missions, plus one open source tool ([JSBSim][jsbsim]).

This project is an attempt to reproduce the published results independently. JSBSim is the only tool that is publicly available, so it is the only simulation run.

Hopefully this will server as a good example of setting up and running simple JSBSim projects. Most of the test cases are very simple, like a falling sphere. Later cases in the study are increasingly complicated. The original paper also includes all the assumptions (models) that went into the test cases. So while this doesn't help learn how to construct a model from scratch, it does help show how to run one and analyze the output.


## Cases:

 - [Case 1: Dragless Sphere](case-01)




[testcases]: http://nescacademy.nasa.gov/flightsim/ "Six degree-of-freedom (6-DOF) Flight Simulation Check-cases"
[jsbsim]: http://jsbsim.sourceforge.net/  "JSBSim Flight Dynamics Model software library"
