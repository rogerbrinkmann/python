"""
multiple coroutines when using python 3.7+
"""

import asyncio

async def coro1(num):
    print(f"Start {num}")
    await asyncio.sleep(1)
    print(f"Stop {num}")
    return num

async def coro2(num):
    print(f"Start {num}")
    await asyncio.sleep(1)
    print(f"Stop {num}")
    return num

# hands several coroutines to the eventloop and gather the results in the same order the coroutines were handed

async def main(num):
    many = await asyncio.gather(
        coro1(num),
        coro2(num)
    )
    return sum(many)

# or:
# many = asyncio.gather(
#     *(coro1(i) for i in range(100))
# )

# create a task to run
resval = asyncio.run(main(1))

print(resval)