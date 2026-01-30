#!/usr/bin/env python3
import rospy
import time
import math
from geometry_msgs.msg import Twist

class SquareTrajectoryController:
    def __init__(self):
        rospy.init_node('square_trajectory_node')

        self.cmd_pub=rospy.Publisher('/cmd_vel',Twist,queue_size=10)
        rospy.sleep(1.0)
 
        #控制参数
        self.linear_vel=0.5
        self.angular_vel=0.8
        self.side_time=2.5
        self.target_angle=math.pi/2

        #Gazebo延迟补偿
        self.delay_factor=1.15
        self.run_time=(self.target_angle/self.angular_vel)*self.delay_factor

    def send_vel(self,linear_x,angular_z,duration):
        """发送速度命令"""
        twist=Twist()
        twist.linear.x=linear_x
        twist.angular.z=angular_z

        start=time.time()
        rate=rospy.Rate(20)

        while(time.time()-start)<duration and not rospy.is_shutdown():
            self.cmd_pub.publish(twist)
            rate.sleep()

        stop_cmd=Twist()
        self.cmd_pub.publish(stop_cmd)
        rospy.sleep(0.2)
    def run_square(self,cycles=1):
        """执行正方形轨迹"""
        for _ in range(cycles):
            self.send_vel(self.linear_vel,0.0,self.side_time)
            self.send_vel(0.0,-self.angular_vel,self.run_time)
            self.send_vel(self.linear_vel,0.0,self.side_time)
            self.send_vel(0.0,-self.angular_vel,self.run_time)
            self.send_vel(self.linear_vel,0.0,self.side_time)
            self.send_vel(0.0,-self.angular_vel,self.run_time)
            self.send_vel(self.linear_vel,0.0,self.side_time)
            self.send_vel(0.0,-self.angular_vel,self.run_time)
            
    def run(self):
        
            rospy.sleep(2.0)
            self.run_square(cycles=2)

            stop_cmd=Twist()
            for _ in range(3):
                self.cmd_pub.publish(stop_cmd)
                rospy.sleep(0.1)

if __name__=='__main__':
    try:
        controller =SquareTrajectoryController()
        controller.run()
    except rospy.ROSInterruptException:
        pass
