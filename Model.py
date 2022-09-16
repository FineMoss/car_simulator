# The class CarSimulator is a simple 2D vehicle simulator.
# The vehicle states are:
# - x: is the position on the x axis on a xy plane
# - y: is the position on the y axis on a xy plane
# - v is the vehicle speed in the direction of travel of the vehicle
# - theta: is the angle wrt the x axis (0 rad means the vehicle
#   is parallel to the x axis, in the positive direction;
#   pi/2 rad means the vehicle is parallel
#   to the y axis, in the positive direction)

import numpy as np


class CarSimulator():

    def __init__(self, wheelbase=4, v0=0, theta0=0):
        # INPUTS:
        # the wheel base is the distance between the front and the rear wheels
        self.wheelbase = wheelbase
        self.x = 0
        self.y = 0
        self.v = v0
        self.theta = theta0


    #  - a: commanded vehicle acceleration
    #  - wheel_angle: steering angle, measured at the wheels;
    #    0 rad means that the wheels are "straight" wrt the vehicle.
    #    A positive value means that the vehicle is turning counterclockwise
    #  - dt: duration of time after which we want to provide
    #    a state update (time step)
    def simulatorStep(self, a, wheel_angle, dt):

        # compute displacement
        ds = self.v*dt + 0.5*a*dt**2

        # rotate velocity vector clockwise
        # y-component of velocity is ignored since dim(v)=1
        self.x += np.cos(-self.theta) * ds
        self.y += np.sin(-self.theta) * ds

        # update velocity
        self.v += a * dt

        if wheel_angle != 0 and self.wheelbase != 0:

            # compute angular_velocity
            turn_radius = self.wheelbase / (np.tan(wheel_angle))
            angular_velocity = ds / turn_radius

            # update theta
            self.theta += angular_velocity * dt

        self.print_state(wheel_angle)


    def print_state(self, wheel_angle):

        output = "V="+str(self.v)
        output+= " wheel_angle="+str(round(wheel_angle, 1))
        output+= " theta="+str(round(self.theta, 2))

        print(output)






