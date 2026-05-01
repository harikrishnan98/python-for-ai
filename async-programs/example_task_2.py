import asyncio
import time


async def fetch_data(param):
    print(f"Do something with {param}")
    await asyncio.sleep(param)
    print(f"Done with {param}")
    return f"Result of {param}"


async def main():
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))

    # Instead of awaiting task1 , we are going to await task2 first
    result2 = await task2
    print("Task 2 fully completed")

    result1 = await task1
    print("Task 1 fully completed")
    return [result1, result2]


t1 = time.perf_counter()

if __name__ == "__main__":
    results = asyncio.run(main())

print(results)

t2 = time.perf_counter()

print(f"Time take to complete the fetch {t2 - t1:.2f} second(s)")
