![](https://raw.githubusercontent.com/ubicoders/yt_tutorials/main/images/banner.png)

#  [Ubicoders Youtube Tutorials](https://github.com/ubicoders/yt_tutorials/)

Tutorials presented in the youtube channel: [Ubicoders Youtube Channel](https://www.youtube.com/channel/UC2RxqAYQt-LBs3paWv78rLA)
 This repository is prepared for specific youtube video.

## 🚀 Install Virtual Robot Python
![Virtual Robots](https://raw.githubusercontent.com/ubicoders/yt_tutorials/main/images/vrobot_mr.png "vr")
The virtual robot is here: [Virtual Multitor](https://www.ubicoders.com/virtualrobots/) 



## ✈️ 1. Getting Started


Requirements:
- Python 3.9+

```
pip install ubicoders-vrobots ipython numpy matplotlib psutil
```


To quickly run the demo script, follow the modeuls! For instance, [module 1](https://github.com/ubicoders/yt_tutorials/blob/main/module1/height_control.ipynb) That's it! Very simple right?



## 🐧 2. For ROS2

docker-compose.yml to use ubicoders ROS2 Humble image.
```
version: "3.8"

services: 
  ubicoders_yt:
      container_name: ubicoders_yt_cnt
      image: ubicoders/ros:base            #ros2 humble
      network_mode: host
      privileged: true
      stdin_open: true # docker run -i
      tty: true        # docker run -t
```

In your ROS2 environment, make sure to install the above pip packages.

### 1. Under the workspace/src clone the following repos:
```
git clone https://github.com/ubicoders/ros2vr_interface
git clone https://github.com/ubicoders/ros2vr_bridge
git clone https://github.com/ubicoders/ros2vr_swarm
```
### 2. Then, build it at your workspace/
```
colcon build --symlink-install
```
### 3. Run the virtual robot bridge
```
ros2 run ros2vr_bridge run_bridge
```
### 4. Run the launch script
```
ros2 launch ros2vr_swarm swarm.launch.py # this will control all drones in the built-in mission.
```



## 🚥 Virtual Robots Axis Convention
x front, y right, z down.

## 🍨 Units - States & sensors

### actuators - pwm 
Integer representing micro seconds. The range between 1100 to 2000 microseconds. This range is a typical operation range of ESC of the actual drones.

### states - accelerometer
Raw accelerometer values for x, y, and z axis. 1g (9.8m/s^2) represents 16384.

### states - gyroscrope
250 deg/second for 32768. To convert to radians per second, (sensor.gyro) * 250/32768 * pi/180

### states - magnetometer
in micro Tesla (uT)

### states - angularVelocity
in radians per second (rad/s)

### states - eulerAngles
in degrees (deg)

### states - linearVelocity
in meters per second (m/s)

### states - position
in meters (m)
