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
loop.call_soon(main, 1)
loop.call_soon(main, 2)

# wait some time and eventually
time.sleep(2)

# simply run the eventloop. During the sleep operation the 'call_soon' functions are called emediately after the loop started running
loop.run_until_complete(asyncio.sleep(5))

main(3)
