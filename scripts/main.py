#!/usr/bin/env python

import rospy
from move_one_brick.srv import MoveBrick
from brick_utils import *

rospy.init_node('center', anonymous=True)
rospy.wait_for_service('move_brick')

move = rospy.ServiceProxy('move_brick', MoveBrick)

def move_wrapper(start, end):
    return move(start.x,start.y,start.z,start.theta,end.x,end.y,end.z,end.theta)

rate = rospy.Rate(1)


start = BrickPose(0.1, 0, 0.3, 0)
end = BrickPose(0.3, 0.3, 0.3, 0)


ready = True
while not rospy.is_shutdown():


    if ready:
        ready = False
        print(move_wrapper(start,end))
    rate.sleep()
    rospy.loginfo("ok")
