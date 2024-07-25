import asyncio
import websockets

async def handle_websocket(websocket, path):
    try:
        while True:
            response = f"Received"
            url = "http://localhost/images/image1.png"
            await websocket.send(url)
          
    except websockets.ConnectionClosed:
        pass



if __name__ == "__main__":
    # Start the WebSocket server
    start_server = websockets.serve(handle_websocket, "localhost", 8765)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
