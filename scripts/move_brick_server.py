#!/usr/bin/env python

import rospy
import math
from std_msgs.msg import Float64MultiArray, MultiArrayDimension
from move_one_brick.srv import MoveBrick, MoveArm

#provide service for moving one brick

#Comunicates with who ever
rospy.wait_for_service('move_arm')
move_arm = rospy.ServiceProxy('move_arm', MoveArm)

def move_brick(req):
    b_x = req.goal_x # (x, y, z, theta)
    b_y = req.goal_y # (x, y, z, theta)
    b_z= req.goal_z
    b_wz= req.goal_theta

    move_arm(b_x,b_y,b_z,0,90,b_wz)
    move_arm(b_x,b_y,b_z,0,90,b_wz)

    # Do what ever it takes to move the brick from start to end here

    # query move it to go to the brick position + some height

    # query to move to the brick height


    return True
def add_two_ints_server():
    rospy.init_node('move_brick_server')
    s = rospy.Service('move_brick', MoveBrick, move_brick)
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
