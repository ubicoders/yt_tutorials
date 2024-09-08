#=================================
# Websocket server to send mavlink data to the client
# Author: Elliot Lee
# Date: 09/08/24
#=================================
import asyncio
import json
import websockets
import threading
from pymavlink import mavutil
from wakeup import wakeup

GLOBAL_FLIGHT_DATA = {
    "time_boot_ms": 0,
    "roll": 0,
    "pitch": 0,
    "heading": 0,
}

# Websocket server
async def run_ws_server(port=9090):
    async def echo(websocket):
        async for message in websocket:
            # print(f"Received message: {message}")
            await websocket.send(json.dumps(GLOBAL_FLIGHT_DATA))

    # start server
    async with websockets.serve(echo, "localhost", port):
        print(f"\033[92m Mavlink Bridge is running @ port {port}\033[0m")
        while True:
            await asyncio.sleep(1)

def start_server():
    asyncio.run(run_ws_server())

# Mavlink Parser

if __name__ == "__main__":
    try:
        thread = threading.Thread(target=start_server, )
        thread.start()


        wakeup()
        # Create mavserial
        the_connection = mavutil.mavlink_connection('/dev/ttyACM0')# /dev/ttyACM0 for linux

        # Keep reading the mavlink messages. i.e attitude and scaled imu
        while True:
            attitude = the_connection.recv_match(type='ATTITUDE') # 30
            if attitude is not None:
                # print(attitude)
                GLOBAL_FLIGHT_DATA["time_boot_ms"] = attitude.time_boot_ms
                GLOBAL_FLIGHT_DATA["roll"] = attitude.roll
                GLOBAL_FLIGHT_DATA["pitch"] = attitude.pitch
                GLOBAL_FLIGHT_DATA["heading"] = attitude.yaw
        

    except KeyboardInterrupt:
        print("Server stopped by user.")