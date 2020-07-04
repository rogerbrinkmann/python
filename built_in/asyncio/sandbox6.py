"""
The eventloop
"""
import asyncio
import datetime
import time

def main(num):
    print(f"{num} {datetime.datetime.now()}")


# get the already existing eventloop
loop = asyncio.get_event_loop()

# registere the function to be called twice by the eventloop
# start as soon as possible after the loops starts running
loop.call_soon(main, 1)

# register the function but schedule it to run 3 sec. after registration
# sleep 2 sec, start the loop and eventually after 1 more second the call_later loop is registered to run
loop.call_later(3, main, 2)

# this function is registered to run after 8 sec.,
# but at that time the loop is already complete and this function never gets executed
# 2 sec. before the loop starts running, the loop runs for 5 sec. and stops,
# 8 sec. after registration the function is scheduled to run but the loop is already complete
loop.call_later(8, main, 3)

# the registered functions don't get executed until (2 sec. later) the eventloop starts running
time.sleep(2)

# simply run the eventloop. During the sleep operation the 'call_soon' functions are called emediately after the loop started running
loop.run_until_complete(asyncio.sleep(5))

# executed after the loop completed (5 sec.)
main(4)
