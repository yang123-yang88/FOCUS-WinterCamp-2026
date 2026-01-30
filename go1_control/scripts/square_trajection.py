#!/usr/bin/env python3
import rospy
import time
from geometry_msgs.msg import Twist

def move_square():
    rospy.init_node('square_precise')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.sleep(1)
    
    # 根据测试结果优化的参数
    side_duration = 4.0      # 前进4秒
    turn_duration = 3.25     # 转弯3.25秒
    forward_speed = 0.6      # 0.6 m/s
    turn_speed = 1.2         # 1.2 rad/s
    
    rate = rospy.Rate(30)
    
    for side in range(4):
        # 前进
        start_time = time.time()
        while time.time() - start_time < side_duration:
            twist = Twist()
            twist.linear.x = forward_speed
            pub.publish(twist)
            rate.sleep()
        
        # 停止
        pub.publish(Twist())
        rospy.sleep(0.3)
        
        start_time = time.time()
        while time.time() - start_time < turn_duration:
            twist = Twist()
            twist.angular.z = turn_speed
            pub.publish(twist)
            rate.sleep()
        
        # 停止
        pub.publish(Twist())
        rospy.sleep(0.3)
    
    print("正方形轨迹完成")

if __name__ == '__main__':
    move_square()