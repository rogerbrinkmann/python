"""
multiple coroutines before python 3.7
"""

import asyncio

async def coro1(num):
    print(f"Start {num}")
    await asyncio.sleep(1)
    print(f"Stop {num}")
    return str(num)

async def coro2(num):
    print(f"Start {num}")
    await asyncio.sleep(1)
    print(f"Stop {num}")
    return (str(num))

# hands several coroutines to the eventloop and gather the results in the same order the coroutines were handed

many = asyncio.gather(
    coro1(1),
    coro2(2)
)

# or:
# many = asyncio.gather(
#     *(coro1(i) for i in range(100))
# )

# create a task to run
task = asyncio.ensure_future(many)

# get handle on the eventloop
loop = asyncio.get_event_loop()

# hand the task to the eventloop and run it until it is complete
loop.run_until_complete(task)

# close the eventloop
loop.close()

# get the results in the order their coroutines were handed to the loop
print(many.result())