# Always run this file to start the bridge between the Virtual Robot and the Web Server.
import asyncio
from ubicoders_vrobots import stop_vr_bridge

if __name__ == "__main__":
    try:
        stop_vr_bridge(12740)
        stop_vr_bridge(12741)
    finally:
        print("Server stopped by user.")

