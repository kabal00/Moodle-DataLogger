import asyncio
import websockets

async def hello():
    uri = "wss://connect.websocket.in/v3/2020?apiKey=QzgZkL5bFpyd2NvfdGzM8ew9E5eckIjozEcj8FoXP8acerv63jd7uAFKcv97"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Christian Stückrath, 12.5°C, 12.5°C; Daniel Gering, 12.5°C, 12.5°C; Simon Berger, 12.5°C, 12.5°C; Christian Vogt, 12.5°C, 12.5°C; Lars Bartetzko, 12.5°C, 12.5°C;Fabian Kaufmann, 12.5°C, 12.5°C;Elke Reinhardt, 12.5°C, 12.5°C;Markus Schimmel, 12.5°C, 12.5°C;Daniel Schelzig, 12.5°C, 12.5°C;Silke Scheliga, 12.5°C, 12.5°C")
asyncio.get_event_loop().run_until_complete(hello())
