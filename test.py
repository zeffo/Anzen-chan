import asyncio

async def check():
    time = 0
    while time<180:
        time+=1
        asyncio.sleep(1)
        return time

hi = input("What to do?")
if hi == "quit":
    time = check.quit()
