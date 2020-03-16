import asyncio
import websockets


async def hello(uri):
    uri = "ws://localhost:9030/"
    async with websockets.connect(uri) as websocket:
        while(1):
          name = input("What's your name? ")
          await websocket.send(name)
          print(f"> {name}")
          greeting = await websocket.recv()
          print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello('ws://localhost:9030/'))
# asyncio.get_event_loop().run_forever(hello())
