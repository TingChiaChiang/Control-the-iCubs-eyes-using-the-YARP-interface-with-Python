# Control-the-iCubs-eyes-using-the-IGazeControl-YARP-interface-with-Python

This script allows you to control iCub’s eyes using Python instead of C++ in the official The first one is to look at a fixation point in Cartesian coordinates. The second one is to look at a fixation point in an absolute angular coordinate system. The last one is to retrieve the current fixation point (may used to measure the displacement error). 

## Getting Started

These instructions will get you a copy of the methods and running on your local machine for development and testing purposes.

### Prerequisites

Install YARP and iCub from sources and compile them properly before running the python script.


Follow instructions here to install them:
[http://wiki.icub.org/wiki/Linux:Installation_from_sources](http://wiki.icub.org/wiki/Linux:Installation_from_sources)

Install the YARP and iCub bindings for Python:
[https://www.yarp.it/yarp_swig.html#yarp_swig_configure](https://www.yarp.it/yarp_swig.html#yarp_swig_configure)

### Installing

```
git clone https://github.com/TingChiaChiang/Control-the-iCubs-eyes-using-the-YARP-interface-with-Python.git
```

## Running the test
### Step 1

First step is to have a yarpserver running.

Open a terminal and run: 
   
```
yarpserver
```
The terminal will look like this:
![yarp](https://user-images.githubusercontent.com/41744376/55685218-c0019e80-5953-11e9-9686-1b5cbf56657e.png)

### Step 2
To run an iCub simulator, open a second terminal and type:
```
iCub_SIM
```
The simulator should look like this:
![icub](https://user-images.githubusercontent.com/41744376/55685172-65684280-5953-11e9-809d-41096314acdc.png)

### Step 3
To use the iKinGazeCtrl module in the simulator, you need to select the proper configuration file. 

Open another terminal and type:

```
iKinGazeCtrl --from configSim.ini
```
### Step 4
Finally, go the the directory where you downloaded the python script and run

```
python python_igaze_control.py
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## References
1. [http://www.icub.org/doc/icub-main/icub_gaze_interface.html#sec_gaze_runningserver](http://www.icub.org/doc/icub-main/icub_gaze_interface.html#sec_gaze_runningserver)

## Authors

* **Ting-Chia Chiang**




