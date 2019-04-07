# Control-the-iCubs-eyes-using-the-IGazeControl-YARP-interface-with-Python

I created three methods to control iCub’s eyes using a Python scprit. The first one is to look at a fixation point in Cartesian coordinates. The second one is to look at a fixation point in an absolute angular coordinate system. The last one is to retrieve the current fixation point (may used to measure the displacement error). 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Install YARP and iCub from sources and compile them properly before running the python script.
[a link](http://wiki.icub.org/wiki/Linux:Installation_from_sources)

```
http://wiki.icub.org/wiki/Linux:Installation_from_sources
```

### Installing

```
git clone https://github.com/TingChiaChiang/Control-the-iCubs-eyes-using-the-YARP-interface-with-Python.git
```

## Running the tests
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


## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.


