"""
The trampoline pattern
multiple trampolines, scheduled at different/same intervals
"""
import asyncio
import datetime
import time


def trampoline(name, later):
    print(f"{datetime.datetime.now().second}: {name}")

    # re-register to the eventloop to be scheduled in the future again
    loop.call_later(later, trampoline, name, later)


# get the already existing eventloop
loop = asyncio.get_event_loop()

# scheduling
call_soon_handle = loop.call_soon(trampoline, "--", 1)
call_soon_handle = loop.call_soon(trampoline, "----", 2)
call_soon_handle = loop.call_soon(trampoline, "--------", 4)
call_later_handle = loop.call_later(10, loop.stop)

loop.run_forever()
loop.close()
