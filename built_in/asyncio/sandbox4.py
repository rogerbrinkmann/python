"""
The eventloop
"""
import asyncio

async def main():
    """
    main:   function
    main(): coroutine object
    """
    print(loop)
    
    await asyncio.sleep(1)
    return 'done'

# get the already existing eventloop
loop = asyncio.get_event_loop()

# simply run the eventloop until a coroutine object / future is done
result = loop.run_until_complete(main())

print(loop)
print(result)

loop.close()
