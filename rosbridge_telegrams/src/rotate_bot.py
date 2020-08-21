#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Twist
import math
import sys

roll = pitch = yaw = 0
target = 0
kP = 1.0

def getOdom(odom):
    global roll, pitch, yaw
    orientation = odom.pose.pose.orientation
    orientation_list = [orientation.x, orientation.y, orientation.z, orientation.w]
    (roll, pitch, yaw) = euler_from_quaternion(orientation_list)

rospy.init_node('rotate_bot')
sub = rospy.Subscriber('/odom', Odometry, getOdom)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
r = rospy.Rate(10)
twist = Twist()
args = rospy.myargv(argv = sys.argv)
target = 180 - float(args[1])
print(float(args[1]))

while not rospy.is_shutdown():
    # rotate_bot()

    target_radians = target * math.pi/180
    twist.angular.z = kP * (target_radians - yaw)
    pub.publish(twist)

    print("Target={}   Current={}".format(target_radians, yaw))
    
    if round(target_radians, 2) == round(yaw, 2):
        # exit()
        sys.exit(1)

    r.sleep()