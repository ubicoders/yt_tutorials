# Always run this file to start the bridge between the Virtual Robot and the Web Server.
import asyncio
from ubicoders_vrobots import run_servers

if __name__ == "__main__":
    try:
        asyncio.run(run_servers())
    except KeyboardInterrupt:
        print("Server stopped by user.")

