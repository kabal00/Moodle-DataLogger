import asyncio
import websockets

async def hello():
    uri = "wss://connect.websocket.in/v2/2020?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6Ijc1ZGZjOTA3OWJjMGJkNmY4NWQ5YWM4NDA2YmE5ZmM4YzBmMDkxNzM0NzBlNTA3ZDNkMDg3ZjI5M2EwZWJkNmUwNDZmZTllZTBhZGJjNTQ3In0.eyJhdWQiOiI4IiwianRpIjoiNzVkZmM5MDc5YmMwYmQ2Zjg1ZDlhYzg0MDZiYTlmYzhjMGYwOTE3MzQ3MGU1MDdkM2QwODdmMjkzYTBlYmQ2ZTA0NmZlOWVlMGFkYmM1NDciLCJpYXQiOjE1ODQyMTE4MjIsIm5iZiI6MTU4NDIxMTgyMiwiZXhwIjoxNjE1NzQ3ODIyLCJzdWIiOiI2NzAiLCJzY29wZXMiOltdfQ.eMtidCxy1LX5JvnZt8yiMZXSPIli0JiVlrUeKz_eV9FGdPClNZY4MxSnzLQPVkk6v4QtyRDRLcx2wfAWm1-jeTnlbe7KOAdyz9jKMcxy3bcmQEzp9TwTATRN78uE_eKuGpKGZcuD8_vYXuyW8N5dehGz4LacXdv9-jfFX9Zn4pHE5DR_bLlLpk0deqf4p4ky-9zvwXQWRDORMZBkQ3PYAtaTx-FWOHM8ZPmrE7ZRpQNCcvVkVwyrtMURXuxQluM8vqhFP9Qw2WNJETj7VjBJamtbXaU42o2mtk9lUDlzLVwho2SGvDM6gG0QKGYJTJH2wqefx-J39TnbSqxeHV6h-TOy_n71lEaJtaDe4-77QDaKFRdA0veQodVV6aHQKwsDBnmICPOUYtWan2ZtRZRE4PHulFVu9nM_fcdIe8376Re-xVMxm7xhM2FtfaUEz_KzaRl_fJ3qhnPH37Wvtk7j8Al8_RK2B1RjrcItqjuHJ1ckH4gJXmYkKvxAIdsxkmfmb9XgMezRC0e6S3cA6W8AbH4nHHt8HGZjAFMseSnrm7EgWSdtjdCKgRt11BCMFqe1kSLDDaJl2AsTA3s9NvVQptXjgCIRadbFVXipN6j6LhKH_lx2GQiPbu6Hnvt1aFvp7bHap4kKD6Cq3vmf_NDbMvnhuq5_EppMH0SmTgtJrSY"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f"> {name}")

      #  greeting = await websocket.recv()
      #  print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello())
