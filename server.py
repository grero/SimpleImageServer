import asyncio
import websockets
import time
import random
import numpy as np
import base64

image_urls = ["/Users/roger/Downloads/radom-clipart-14.jpg.png",
              "/Users/roger/Downloads/333-3331136_cartoon-clipart-png-download-random-object-battle-royal.png"]

images = [base64.b64encode(open(img,"rb").read()) for img in image_urls]

async def handle_websocket(websocket, path):
    try:
        while True:
            r = int(np.round(random.random()))
            print(images[r][:10])
            await websocket.send(images[r])
            time.sleep(1.0)
          
    except websockets.ConnectionClosed:
        pass



if __name__ == "__main__":
    # Start the WebSocket server
    start_server = websockets.serve(handle_websocket, "localhost", 8765)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
