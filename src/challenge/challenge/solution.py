import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import pose
PI = 3.1415926535897

import time
from std_srvs.srv import Empty
import math

x = 0
y = 0
theta = 0

def poseCallback(pose_message):
	global x
	global y, theta
	x = pose_message.x
	y = pose_message.y
	if pose.theta < 0:
		alpha = req - (pose.theta + (2 * math.pi))
	else:
		alpha = req - pose.theta
	alpha = 2 * math.pi - alpha
	theta = alpha


def turtle_sin():
	global theta
	rospy.init_node('turtle_sine', anonymous = True)
	velocity_pub = rospy.Publisher('/turtle1/cmd_vel', Twist,
		queue_size = 10)
	rospy.Subscriber("/turtle1/pose", Pose, poseCallback)
	time.sleep(2)
	vel_msg = Twist()

	speed = 0.3
	radius = 1
	vel_msg.linear.x = speed
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	vel_msg.angular.x = 0
	vel_msg.angular.z = 0
	vel_msg.angular.y = speed/radius

	rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		vel_msg.linear.x = speed * math.cos(theta)
		vel_msg.angular.y = math.sin(theta)
		velocity_publisher.publish(vel_msg)

		rospy.loginfo("Sine function")
		print(theta)
		rate.sleep()
	print("Finished")
	vel_msg.linear.x = 0
	vel_msg.angular.y = 0
	velocity_publisher.publish(vel_msg)
	rospy.spin()


def main():
	print("here")


if __name__ == '__main__':
	try:
		time.sleep(2)
		turtle_sin()

	except rospy.ROSInterruptException:
		rospy.loginfo("Node terminated.")
