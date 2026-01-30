/**********************************************************************
 Copyright (c) 2020-2023, Unitree Robotics.Co.Ltd. All rights reserved.
***********************************************************************/
#ifndef KEYBOARD_H
#define KEYBOARD_H

#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <sys/types.h>
#include <unistd.h>
#include <fcntl.h>
#include <termios.h>
#include "interface/CmdPanel.h"
#include "common/mathTools.h"

// 只添加这两个ROS头文件
#include <ros/ros.h>
#include <geometry_msgs/Twist.h>

class KeyBoard : public CmdPanel{
public:
    KeyBoard();
    ~KeyBoard();
    
private:
    static void* runKeyBoard(void *arg);
    void* run(void *arg);
    UserCommand checkCmd();
    void changeValue();
    
    // 新增函数
    void cmdVelCallback(const geometry_msgs::Twist::ConstPtr& msg);

    pthread_t _tid;
    float sensitivityLeft = 0.05;
    float sensitivityRight = 0.05;
    struct termios _oldSettings, _newSettings;
    fd_set set;
    int res;
    int ret;
    char _c;
    
    // 新增成员变量 - 使用下划线保持风格一致
    ros::Subscriber cmd_vel_sub_;
    float cmd_vel_x_;
    float cmd_vel_z_;
    bool use_cmd_vel_;
    bool keyboard_override_;
    ros::Time last_cmd_time_;
};

#endif  // KEYBOARD_H