import time
from multiprocessing import Process
import concurrent.futures


st = time.perf_counter()


def do_some(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    return f"Done sleeping...at {seconds}s"


if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        sec = [5, 4, 3, 2, 1]
        results = executor.map(do_some, sec)
    # for res in results:
    #     print(res)
# if __name__ == "__main__":
#     for _ in range(10):
#         p = Process(target=do_some, args=(2,))
#         p.start()
#         process.append(p)
#     for p in process:
#         p.join()
fin = time.perf_counter()

print(f"Finished in L: {fin - st} second(s)")
