# asynchronus method

import asyncio
import time


async def slow_task_async(name, seconds):
    print(f"Starting {name}......")
    await asyncio.sleep(seconds)
    print(f"Ending {name}......")
    return f"{name} result"

async def run_all():
    start = time.time()
    results = await asyncio.gather(
        slow_task_async("Task A", 2),
        slow_task_async("Task B", 2),
        slow_task_async("Task C", 2),
    )
    end = time.time()
    print(f"Total time taken : {end - start:.2f} seconds.")
    print(f"Results : {results}")


# await run_all() in jupyter note book
asyncio.run(run_all())  # in normal .py file