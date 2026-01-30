项目简介：
本项目为FOCUS 2026冬令营视觉与仿真赛道的完整实现，基于ROS Noetic、Gazebo和Ubuntu 20.04，包含机器人仿真、运动控制、视觉跟踪等功能。
避坑指南：
Gazebo启动黑屏或闪退：务必在VMware中开启3D图形加速
虚拟机卡顿严重：可以尝试分配8GB内存，适当增加处理器个数及每个处理器的核心数目
环境配置：请严格按照教程配置先后顺序
依赖包：参考Github网站unitree_guide,注意：unitree_legged_real包不应成为依赖的一部分
源码修改：修改源码需请重新编译，可先删除原build devel 文件后重新编译，
脚本：编写脚本后需赋予该脚本权限后才可运行，脚本代码需要放在一个包中，否则无法运行
话题通信：请保持订阅者和发布者的话题名称一致
运行指南：
运行前请先编译：在工作空间中运行catkin_make指令
小海龟：#1. 启动ROS核心：roscore 
       #2. 运行小海龟测试：rosrun turtlesim turtlesim_node
       # 3. 新终端中控制小海龟：rosrun turtlesim turtle_teleop_key
机器狗仿真：终端一：source ./devel/setup.bash
                   roslaunch unitree_guide gazeboSim.launch 
            终端二：./devel/lib/unitree_guide/junior_ctrl
ROS通信与运动控制：终端一：source ./devel/setup.bash
                   roslaunch unitree_guide gazeboSim.launch 
                  终端二：./devel/lib/unitree_guide/junior_ctrl
                  终端三：运行pythn脚本（rosrun 包名 脚本名）
AI视觉闭环：暂无
