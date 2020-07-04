"""
The trampoline pattern
self-stopping
"""
import asyncio
import datetime
import time


def trampoline(index):
    print(f"Trampoline {index:>3}: {datetime.datetime.now()}")
    if index >= 3:
        loop.stop()
    else:
        loop.call_later(1, trampoline, index + 1)

loop = asyncio.get_event_loop()
loop.call_later(10, loop.stop)
loop.call_soon(trampoline, 1)

loop.run_forever()

