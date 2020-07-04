"""
nested coroutines calling each other
"""
import asyncio

async def coro1(num):
    print(f"Start coro 1")
    new_num = await coro2(num)
    print(f"Stop coro 1")
    return new_num

async def coro2(num):
    print(f"Start coro 2")
    await asyncio.sleep(1)
    print(f"Stop coro 2")
    return num+1



# create a task to run
task = asyncio.ensure_future(coro1(1))

# get handle on the eventloop
loop = asyncio.get_event_loop()

# hand the task to the eventloop and run it until it is complete and return the result
retval = loop.run_until_complete(task)

# close the eventloop
loop.close()

# get the results in the order their coroutines were handed to the loop
print(retval)