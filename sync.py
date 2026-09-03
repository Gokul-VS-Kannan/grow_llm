# synchronous function

import time


def slow_task(name, seconds):
    print(f"Starting {name}......")
    time.sleep(seconds)
    print(f"Ending {name}......")
    return f"{name} result"

start = time.time()
result1 = slow_task("Task A", 2)
result2 = slow_task("Task B", 2)
result3 = slow_task("Task C", 2)
end = time.time()

print(f"Total time taken : {end - start:.2f} seconds. expected~6")