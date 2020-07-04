"""
The trampoline pattern
clogging the loop with a processing intensive hog function
"""
import asyncio
import datetime
import time


def hog():
    print(f"Hog Start: {datetime.datetime.now()}")
    s = 0
    for i in range(10_000):
        for j in range(10_000):
            s += j
        s += i
    print(f"Hog Stop: {datetime.datetime.now()}")

def trampoline():
    print(f"Trampoline: {datetime.datetime.now()}")
    loop.call_later(1, trampoline)

loop = asyncio.get_event_loop()

loop.call_soon(trampoline)

# the hog is scheduled after 5 sec and then runs for ca. 18 sec
# since it's a processing-intense task it will block the loop during it's execution
# an io-task could be interrupted by the loop
# also the loop.stop is scheduled while the hog is still running. Still it will run until the end
# and even execute the Trampoline once more
loop.call_later(5, hog)

# schedule to stop after 10 sec, but actual stop is as soon as reasonable
loop.call_later(10, loop.stop)
loop.run_forever()
print("First stopped, restarting, scheduled to stop in 4 sec")
loop.call_later(4, loop.stop)
loop.run_forever()

