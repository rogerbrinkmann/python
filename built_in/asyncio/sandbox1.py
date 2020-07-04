"""
simple coroutine
"""
import asyncio

async def coro(num):
    """
    Coroutine function, run by the eventloop
    It uses await keyword on time consuming operations,
    so that the evantloop can schedule different operations during that time
    """
    print(f"Start {num}")

    # await: means the eventloop could switch execution to another operation and continue here later
    await asyncio.sleep(1)
    print(f"Stop {num}")
    return str(num)

# python 3.7+
# asyncio.run(mycoro1(1))


# python 3.6
# create a task to run
task = asyncio.ensure_future(coro(1))

# get handle on the eventloop
loop = asyncio.get_event_loop()

# hand the task to the eventloop and run it until it is complete
retval = loop.run_until_complete(coro(1))

# close the eventloop
loop.close()

print(retval)