#!/usr/bin/env python

import rospy
from move_one_brick.srv import MoveBrick
from brick_utils import *
from std.msgs import Float64

rospy.init_node('center', anonymous=True)
rospy.wait_for_service('move_brick')

move = rospy.ServiceProxy('move_brick', MoveBrick)

pub_gripper = rospy.Publisher('/franka/gripper_width',
                          Float64, queue_size=1)

def move_wrapper(start, end):
    return move(start.x,start.y,start.z,start.theta,end.x,end.y,end.z,end.theta)


def set_gripper_wrapper(width):
    pub_gripper.pub(width)

rate = rospy.Rate(0.1)


start = BrickPose(0.5, 0.5, 0.5, 180)
end = BrickPose(0.3, 0.3, 0.3, 95)


ready = True
while not rospy.is_shutdown():


    if ready:
        ready = False
        move_wrapper(start,end)
        set_gripper_wrapper(0)
    else:
        ready = True
        move_wrapper(end,start)
        set_gripper_wrapper(0.08)


    rate.sleep()
