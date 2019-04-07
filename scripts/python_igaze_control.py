#!/usr/bin/python
import yarp
# Initialize YARP
yarp.Network.init();

"""Class for controlling iCub's eyes using the IGazeControl
   YARP interface from a Python script."""
class iGazeController:
    def __init__(self):
        # prepare a property object
        props = yarp.Property()
        props.put("device","gazecontrollerclient")
        props.put("local","/client/gaze")
        props.put("remote","/iKinGazeCtrl")

        # create remote driver
        self.clientGaze = yarp.PolyDriver(props)
        # open the view
        self.iGaze = self.clientGaze.viewIGazeControl()

    # look at a fixation point in Cartesian Coordinates
    def LookAtPoint(self, x, y, z):
        self.fp= yarp.Vector(3)
        self.fp[0] = x
        self.fp[1] = y
        self.fp[2] = z
        self.iGaze.lookAtFixationPoint(self.fp)
        self.iGaze.setTrackingMode(True)
        self.iGaze.waitMotionDone()
        print "I am looking at", self.fp[0], self.fp[1], self.fp[2]

    # look at a fixation point in Absolute Angular Coordinate System
    def LookAtAngle(self, x, y, z):
        self.fa= yarp.Vector(3)
        self.fa[0] = x
        self.fa[1] = y
        self.fa[2] = z
        self.iGaze.lookAtAbsAngles(self.fa)
        self.iGaze.setTrackingMode(True)
        self.iGaze.waitMotionDone()

    # retrieve the current fixation point
    def GetCurrentPoint(self):
        self.fp_get = yarp.Vector()
        self.iGaze.getFixationPoint(self.fp_get);
        print self.fp_get[0], self.fp_get[1], self.fp_get[2]




if __name__ == "__main__":
    gaze_object = iGazeController()
    # gaze_object.LookAtPoint(0, -5.0, -2)
    gaze_object.LookAtPoint(0, -5.0, 4)
    gaze_object.LookAtAngle(10, -5.0, 10)
    gaze_object.clientGaze.close()

    # gaze_object2 = iGazeController()
    # gaze_object2.GetCurrentPoint()
