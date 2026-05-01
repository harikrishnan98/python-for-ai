import asyncio
import time

async def fetch_data(param):
    await asyncio.sleep(param)
    return f"Result of {param}"


async def main():
    # Create Task Manually
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))

    result1 = await task1
    result2 = await task2

    print(f"Task 1 and Task2 awaited results: {[result1, result2]}")

    # Gather Co-routines

    coroutines = [fetch_data(i) for i in range(1, 3)]

    results = await asyncio.gather(*coroutines, return_exceptions=True)

    print(f"Gather Coroutine Results: {results}")

    ## Gather Tasks

    tasks = [asyncio.create_task(fetch_data(i)) for i in range(1, 3)]

    task_results = await asyncio.gather(*tasks,return_exceptions=True)

    print(f"Gather Tasks Results: {task_results}")

    ## Task Group

    async with asyncio.TaskGroup() as tg: # async with → acts like "await all"
        grp_results = [tg.create_task(fetch_data(i)) for i in range(1, 3)]

        # All tasks are awaited when the context manager exits.


     # So that we are using res.result() to get the result

    print(f"Task Group Results: {[ res.result() for res in grp_results]}")

    return "Main Coroutine Done"


if __name__ == "__main__":
    t1 = time.perf_counter()
    all_results = asyncio.run(main())
    t2 = time.perf_counter()
    print(all_results)
    print(f"Finished in: {t2-t1: .2f}")
