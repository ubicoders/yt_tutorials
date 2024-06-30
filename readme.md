# Ubicoders Virtual Robot - Multirotor

The virtual robot is here [Virtual Multitor](https://www.ubicoders.com/virtualrobots/) 
![Virtual Robots](https://raw.githubusercontent.com/ubicoders/yt_tutorials/main/images/vrobot_mr.png "vr")



Requirements:
- Python 3

## Once you have Python 3

```
pip install ubicoders-vrobots matplotlib
```

## Turn on Virtual Robots Bridge
```
python vr_bridge.py
```


## Axis Convention
x front, y right, z down.

## Units

### actuators.pwm 
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