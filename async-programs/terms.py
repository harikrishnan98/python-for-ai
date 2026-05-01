import time
import asyncio


def sync_function(test_params: str) -> str:
    print("This is synchronous function")

    time.sleep(0.1)

    return f"Sync Result: {test_params}"


# ASYNC Function
# Also known as Co-routine function


async def asyn_function(test_param: str) -> str:
    print("This is an asynchronous co-routine")

    await asyncio.sleep(0.1)

    return f"Async Results: {test_param}"


async def main():
    # sync_result = sync_function("Test-SYNC")
    # print(sync_result)
    #
    # loop = asyncio.get_event_loop()
    # future = loop.create_future()  # A promise like object (New Promise())
    # print(f"Empty Future: {future}")

    # # future.set_result("Future Result: Test")
    #
    # future.set_exception(ValueError("Invalid input"))
    # future_result = await future
    # print(future_result)
    # print(f"Future: {future}")

    ### CO-ROUTINE ######
    # coroutine_obj = asyn_function("ASYNC-TEST")
    # print(f'CO-ROUTINE-OBJ {coroutine_obj}')
    #
    # coroutine_result = await coroutine_obj
    # print(f'Co-routine-Res = {coroutine_result}')


    #### TASK #####
    task = asyncio.create_task(asyn_function("Test"))
    print(f"TASK01: {task}")

    task_result = await task
    print(f"TASK-RESULT01: {task_result}")

if __name__ == "__main__":
    asyncio.run(main())
