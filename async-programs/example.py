import time

import asyncio
### SYNCHRONOUS CODE

# def fetch_data(param):
#     print(f"Do something with {param}")
#     time.sleep(param)
#     print(f"Done with {param}")
#     return f"Result of {param}"


# def main():
#     result1 = fetch_data(1)
#     print("Fetch 1 fully completed")
#     result2 = fetch_data(2)
#     print("Fetch 2 fully completed")
#     return [result1, result2]


# t1 = time.perf_counter()

# results = main()

# print(results)

# t2 = time.perf_counter()

# print(f"Time take to complete the fetch {t2-t1:.2f} second(s)")


### ASYNCHRONOUS CODE EXAMPLE


async def fetch_data(param):
    print(f"Do something with {param}")
    await asyncio.sleep(param)
    print(f"Done with {param}")
    return f"Result of {param}"


async def main():
    task1 = fetch_data(1)
    task2 = fetch_data(2)

    result1 = await task1
    print("Fetch 1 fully completed")

    result2 = await task2
    print("Fetch 2 fully completed")
    return [result1, result2]


t1 = time.perf_counter()

if __name__ == "__main__":
    results = asyncio.run(main())

print(results)

t2 = time.perf_counter()

print(f"Time take to complete the fetch {t2 - t1:.2f} second(s)")


