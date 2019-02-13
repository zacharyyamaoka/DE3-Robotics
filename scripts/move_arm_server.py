#!/usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String, Float64
from moveit_commander.conversions import pose_to_list
from brick_utils import *
from move_one_brick.srv import MoveArm
# rospy.init_node('arm_controller', anonymous=True)


rospy.init_node('move_arm_server')

publishers = [rospy.Publisher('/franka/joint{}_position_controller/command'.format(i), Float64, queue_size=1) for i in range(1, 8)]
moveit_commander.roscpp_initialize(sys.argv)

# rospy.init_node('move_group_python_interface_tutorial',
#                 anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group_name = "panda_arm"
group = moveit_commander.MoveGroupCommander(group_name)
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                               moveit_msgs.msg.DisplayTrajectory,
                                               queue_size=20)

def move_arm_handler(req):
    # initial = [0, 0, 0, 0, 1, 1, 0.75]
    # for i in range(7):
    #     publishers[i].publish(initial[i])
    #
    # eef_link = group.get_end_effector_link()
    # print "============ End effector: %s" % eef_link
    pose_goal = geometry_msgs.msg.Pose()
    pose_goal.orientation.w = 1.0
    pose_goal.position.x = req.x
    pose_goal.position.y = req.y
    pose_goal.position.z = req.z
    group.set_pose_target(pose_goal)
    plan = group.go(wait=True)
    # Calling `stop()` ensures that there is no residual movement
    group.stop()
    # It is always good to clear your targets after planning with poses.
    # Note: there is no equivalent function for clear_joint_value_targets()
    group.clear_pose_targets()
    return True


s = rospy.Service('move_arm', MoveArm, move_arm_handler)

print "Ready to move arm"
rospy.spin()
