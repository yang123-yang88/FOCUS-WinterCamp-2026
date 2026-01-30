#!/usr/bin/env python3
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

rospy.init_node('camera_test')
bridge = CvBridge()
sub = rospy.Subscriber('/camera_face/color/image_raw', Image, lambda msg: cv2.imshow('Camera', bridge.imgmsg_to_cv2(msg, "bgr8")) or cv2.waitKey(1))

rospy.spin()
cv2.destroyAllWindows()