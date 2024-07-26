import asyncio
import websockets
import time
import random
import numpy as np
import base64
import glob

def get_images():
    img_files = glob.glob("*.png")
    img_files.extend(glob.glob("*.jpg"))
    images = [base64.b64encode(open(img,"rb").read()) for img in img_files]
    return images


images = get_images()

async def handle_websocket(websocket, path):
    try:
        while True:
            r = int(np.round(random.random()))
            await websocket.send(images[r])
            time.sleep(1.0)
          
    except websockets.ConnectionClosed:
        pass



if __name__ == "__main__":
    # Start the WebSocket server
    start_server = websockets.serve(handle_websocket, "localhost", 8765)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
