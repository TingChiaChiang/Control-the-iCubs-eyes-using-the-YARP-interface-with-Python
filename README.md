# Control-the-iCubs-eyes-using-the-IGazeControl-YARP-interface-with-Python

I created three methods to control iCub’s eyes using a Python scprit. The first one is to look at a fixation point in Cartesian coordinates. The second one is to look at a fixation point in an absolute angular coordinate system. The last one is to retrieve the current fixation point (may used to measure the displacement error). 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

1. Install YARP and iCub from sources and compile them properly 

```
http://wiki.icub.org/wiki/Linux:Installation_from_sources
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

First step is to have a yarpserver running.

Open a terminal and run 
   
```
yarpserver
```
The terminal will look like this:
![yarp](https://user-images.githubusercontent.com/41744376/55685218-c0019e80-5953-11e9-9686-1b5cbf56657e.png)


To run an iCub simulator, open a second terminal and type
```
iCub_SIM
```
The simulator should look like this:
![icub](https://user-images.githubusercontent.com/41744376/55685172-65684280-5953-11e9-809d-41096314acdc.png)


To use the iKinGazeCtrl module in the simulator, you need to select the proper configuration file. 

Open another terminal and type:

```
iKinGazeCtrl --from configSim.ini
```

Finally, go the the directory where you downloaded the python script and run

```
python python_igaze_control.py
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc


