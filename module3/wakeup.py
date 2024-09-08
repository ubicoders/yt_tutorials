#=================================
# Pixhawk Wakeup
# Author: Elliot Lee
# Date: 09/08/24
#=================================
from pymavlink import mavutil

def wakeup():
    # Create mavserial
    the_connection = mavutil.mavlink_connection('/dev/ttyACM0')# /dev/ttyACMX for linux

    # Sending a message creates PX4's streamer to serial.
    the_connection.mav.heartbeat_send(
        0, #type
        0, #autopilot
        0, #base_mode
        0, #custom_mode
        0, #system_status
        0, #mavlink_version
    )

    # Check the heartbeat
    the_connection.wait_heartbeat()
    print(f"Heartbeat from target_system: {the_connection.target_system}, MAV_TYPE: {the_connection.mav_type}")
    ## mav_type: https://mavlink.io/en/messages/common.html#MAV_TYPE_QUADROTOR

if __name__ == "__main__":
    wakeup()