#!/usr/bin/env python3
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge

rospy.init_node('tracker')
bridge = CvBridge()
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

def callback(msg):
    frame = bridge.imgmsg_to_cv2(msg, "bgr8")
    cmd = Twist()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, np.array([0,100,100]), np.array([10,255,255]))
    
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        cnt = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(cnt)
        if area > 500:
            M = cv2.moments(cnt)
            if M["m00"] > 0:
                cx = int(M["m10"] / M["m00"])
                cmd.angular.z = -0.002 * (cx - 320)
                cmd.linear.x = max(0, 0.0005 * (10000 - area))
                cmd.angular.z = max(-0.5, min(0.5, cmd.angular.z))
                cmd.linear.x = max(0, min(0.3, cmd.linear.x))
    
    pub.publish(cmd)

sub = rospy.Subscriber('/camera_face/color/image_raw', Image, callback)
rospy.spin()