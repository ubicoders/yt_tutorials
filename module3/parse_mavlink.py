#=================================
# Basic script to connect to PX4 and read mavlink messages.
# Author: Elliot Lee
# Date: 09/08/24
#=================================
from pymavlink import mavutil
from wakeup import wakeup

wakeup()

# Create mavserial
the_connection = mavutil.mavlink_connection('/dev/ttyACM0')# /dev/ttyACM0 for linux

# Keep reading the mavlink messages. i.e attitude and scaled imu
while True:
    attitude = the_connection.recv_match(type='ATTITUDE') # 30
    if attitude is not None:
        print(attitude)
    scaled_imu = the_connection.recv_match(type="SCALED_IMU") # 26
    if scaled_imu is not None:
        print(scaled_imu)