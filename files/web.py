import asyncio
import websockets
import socket
import os
import time

async def chat(websocket, path):
    while(True):
    	msg = await websocket.recv()
    	os.system(msg)

asyncio.get_event_loop().run_until_complete((websockets.serve(chat, "localhost", 8765)))
asyncio.get_event_loop().run_forever()





