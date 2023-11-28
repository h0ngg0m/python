import asyncio

async def coro1():
    print('C1: Start') # 1
    await asyncio.sleep(1) # 2
    print('C1: Stop') # 5

async def coro2():
    print('C2: Start') # 3
    await asyncio.sleep(2) # 4
    print('C2: Stop') # 6

loop = asyncio.get_event_loop()
loop.create_task(coro1())
loop.create_task(coro2())
loop.run_forever()
