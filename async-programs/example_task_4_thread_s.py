import asyncio
import time

from concurrent.futures import ProcessPoolExecutor


def fetch_data(param):
    print(f"Do something with {param}",flush=True)
    time.sleep(param)
    print(f"Done with {param}",flush=True)
    return f"Result of {param}"


async def main():
    # Run the sync code in Thread
    task1 = asyncio.create_task(asyncio.to_thread(fetch_data, 1))
    task2 = asyncio.create_task(asyncio.to_thread(fetch_data, 2))

    result1 = await task1
    print("Thread 1 fully completed")

    result2 = await task2
    print("Thread 2 fully completed")

    # Run the sync code in Process Pool

    loop = asyncio.get_running_loop()

    with ProcessPoolExecutor() as pool:
        task1 = loop.run_in_executor(pool, fetch_data, 1)
        task2 = loop.run_in_executor(pool, fetch_data, 2)

    result1 = await task1
    print("Process 1 fully completed")

    result2 = await task2
    print("Process 2 fully completed")

    return [result1, result2]


t1 = time.perf_counter()

if __name__ == "__main__":
    results = asyncio.run(main())
    print(results)

t2 = time.perf_counter()

print(f"Time take to complete the fetch {t2 - t1:.2f} second(s)")
