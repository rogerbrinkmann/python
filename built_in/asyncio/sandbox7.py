"""
The trampoline pattern
"""
import asyncio
import datetime
import time


def trampoline(name, index):
    print(f"{name}{index:>3} - {datetime.datetime.now()}")

    # re-register to the eventloop to be scheduled in the future again
    schedule = loop.call_later(1, trampoline, name, index + 1).when()
    loop_time = loop.time()
    print(f"Loop-time: {loop_time}")
    print(f"Scheduled: {schedule}")
    print(f"Delta: {schedule-loop_time}")


# get the already existing eventloop
loop = asyncio.get_event_loop()

call_soon_handle = loop.call_soon(trampoline, "Trampoline", 1)

# schedule loop.stop in order to limit the runtime
call_later_handle = loop.call_later(5, loop.stop)
call_later_handle = loop.call_later(10, loop.stop)

loop.run_forever()
print("--------------- First run is over")

# the run can be started again, since the call-soon-method is still registered it will run again
# as soon as the loop is running again
loop.run_forever()

