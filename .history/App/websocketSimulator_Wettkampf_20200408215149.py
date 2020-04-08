import asyncio
import websockets
import time
async def hello():
    uri = "wss://connect.websocket.in/v3/2020?apiKey=QzgZkL5bFpyd2NvfdGzM8ew9E5eckIjozEcj8FoXP8acerv63jd7uAFKcv97"
    async with websockets.connect(uri) as websocket:
        #name = input("What's your name? ")
        n = 5
        await websocket.send("Christian Stückrath; 20.5°C; 18.5°C")
        await asyncio.sleep(n)
        await websocket.send("Christian Weber; 20.5°C; 18.5°C")
        await asyncio.sleep(n)
        await websocket.send("Daniel Gering; 20.5°C; 18.5°C")
        await asyncio.sleep(n)
        await websocket.send("Tobias Hofmann; 20.5°C; 18.5°C")
        await asyncio.sleep(n)
        await websocket.send("Simon Berger; 20.5°C; 18.5°C")
        await asyncio.sleep(n)
        await websocket.send("Sarah Anne; 20.5°C; 18.5°C")
        await asyncio.sleep(n)
        await websocket.send("Vincent Spiegel; 20.5°C; 18.5°C")
        await asyncio.sleep(n)
        await websocket.send("Christian Vogt; 20.5°C; 18.5°C")
        await asyncio.sleep(n)
        await websocket.send("Matthias Süß; 20.5°C; 18.5°C")
        await asyncio.sleep(n)
        await websocket.send("Silas Lotter; 20.5°C; 18.5°C")

      #  greeting = await websocket.recv()
      #  print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello())
