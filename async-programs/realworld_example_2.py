import time  # used for measuring execution time
from pathlib import Path  # modern way to handle file paths

import aiofiles
import httpx  # ASYNC HTTP library for downloading images
from PIL import Image  # image processing library

import asyncio

import os

from typing import cast

DOWNLOAD_LIMIT = 4

CPU_WORKERS = os.cpu_count()


from concurrent.futures import ProcessPoolExecutor

# List of image URLs to download
IMAGE_URLS = [
    "https://images.unsplash.com/photo-1516117172878-fd2c41f4a759?w=1920&h=1080&fit=crop",
    "https://images.unsplash.com/photo-1532009324734-20a7a5813719?w=1920&h=1080&fit=crop",
    "https://images.unsplash.com/photo-1524429656589-6633a470097c?w=1920&h=1080&fit=crop",
    "https://images.unsplash.com/photo-1530224264768-7ff8c1789d79?w=1920&h=1080&fit=crop",
    "https://images.unsplash.com/photo-1564135624576-c5c88640f235?w=1920&h=1080&fit=crop",
    "https://images.unsplash.com/photo-1541698444083-023c97d3f4b6?w=1920&h=1080&fit=crop",
    "https://images.unsplash.com/photo-1522364723953-452d3431c267?w=1920&h=1080&fit=crop",
    "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=1920&h=1080&fit=crop",
    "https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99?w=1920&h=1080&fit=crop",
    "https://images.unsplash.com/photo-1516972810927-80185027ca84?w=1920&h=1080&fit=crop",
    "https://images.unsplash.com/photo-1550439062-609e1531270e?w=1920&h=1080&fit=crop",
    "https://images.unsplash.com/photo-1549692520-acc6669e2f0c?w=1920&h=1080&fit=crop",
]

# Directories to store images
ORIGINAL_DIR = Path("original_images")
PROCESSED_DIR = Path("processed_images")


async def download_single_image(
    client: httpx.AsyncClient, url: str, img_num: int, semaphore: asyncio.Semaphore
) -> Path:  # Removed session params
    async with semaphore: # It will limit the maximum concurrent download to four at a time
        print(f"Downloading {url}...")  # log which image is downloading

        ts = int(time.time())  # current timestamp
        url = f"{url}?ts={ts}"  # avoid caching by making URL unique

        # send HTTP request

        # We don't need session here since its not a thread safe, lets it call requests and hit everytime

        response = await client.get(url, timeout=10, follow_redirects=True)

        response.raise_for_status()  # raise error if request failed

        filename = f"image_{img_num}.jpg"  # generate file name
        download_path = ORIGINAL_DIR / filename  # full path

        # using async aiofiles for opening the file async
        async with aiofiles.open(download_path, "wb") as f:
            async for chunk in response.aiter_bytes(chunk_size=8192):
                await f.write(chunk)

        print(f"Downloaded and saved to: {download_path}")
        return download_path  # return saved file path


async def download_images(
    urls: list,
) -> list[
    Path
]:  # Converting this as a async function to create a Task group for a sync fn

    # Adding semaphore to the Task
    dl_semaphore = asyncio.Semaphore(cast(int,DOWNLOAD_LIMIT))
    # Creating a Task Group
    async with httpx.AsyncClient() as client:
        async with asyncio.TaskGroup() as tg:
            # We don't need session since its not thread safe
            tasks = [
                tg.create_task(download_single_image(client, url, img_num,dl_semaphore))
                for img_num, url in enumerate(urls, start=1)  # numbering images
            ]

    img_paths = [t.result() for t in tasks]
    return img_paths


def process_single_image(orig_path: Path) -> Path:
    save_path = PROCESSED_DIR / orig_path.name  # output file path

    with Image.open(orig_path) as img:
        data = list(img.getdata())  # pixel data as list
        width, height = img.size  # image dimensions
        new_data = []  # store processed pixels

        # iterate through each pixel
        for i in range(len(data)):
            current_r, current_g, current_b = data[i]  # current pixel

            total_diff = 0
            neighbor_count = 0

            # check right and bottom neighbors
            for dx, dy in [(1, 0), (0, 1)]:
                x = (i % width) + dx  # column index
                y = (i // width) + dy  # row index

                # ensure within bounds
                if 0 <= x < width and 0 <= y < height:
                    neighbor_r, neighbor_g, neighbor_b = data[y * width + x]

                    # compute color difference
                    diff = (
                        abs(current_r - neighbor_r)
                        + abs(current_g - neighbor_g)
                        + abs(current_b - neighbor_b)
                    )

                    total_diff += diff
                    neighbor_count += 1

            # average difference (edge strength)
            if neighbor_count > 0:
                edge_strength = total_diff // neighbor_count

                # threshold: detect edges
                if edge_strength > 30:
                    new_data.append((255, 255, 255))  # white = edge
                else:
                    new_data.append((0, 0, 0))  # black = no edge
            else:
                new_data.append((0, 0, 0))

        # create new image from processed data
        edge_img = Image.new("RGB", (width, height))
        edge_img.putdata(new_data)
        edge_img.save(save_path)  # save processed image

    print(f"Processed {orig_path} and saved to {save_path}")
    return save_path


async def process_images(orig_paths: list[Path]) -> list[Path]:
    # process Images to Multi process

    loop = asyncio._get_running_loop()

    with ProcessPoolExecutor(max_workers=CPU_WORKERS) as pool:
        tasks_process = [
            loop.run_in_executor(pool, process_single_image, orig_path)
            for orig_path in orig_paths
        ]
        img_paths = await asyncio.gather(*tasks_process, return_exceptions=True)
    return img_paths


async def main():
    # create directories safely
    ORIGINAL_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    start_time = time.perf_counter()  # start timer

    # awaiting the co-routine obj from async fun
    img_paths =  await download_images(IMAGE_URLS)  # download images

    proc_start_time = time.perf_counter()  # start processing timer

    # awaiting the co-routine obj from async fun
    processed_paths = await process_images(img_paths)  # process images

    finished_time = time.perf_counter()  # end timer

    # calculate timings
    dl_total_time = proc_start_time - start_time
    proc_total_time = finished_time - proc_start_time
    total_time = finished_time - start_time

    # print stats
    print(
        f"\nDownloaded {len(img_paths)} images in: {dl_total_time:.2f} seconds. {(dl_total_time / total_time) * 100:.2f}% of total time",
    )
    print(
        f"Processed {len(processed_paths)} images in: {proc_total_time:.2f} seconds. {(proc_total_time / total_time) * 100:.2f}% of total time",
    )
    print(
        f"\nTotal execution time: {total_time:.2f} seconds. {(total_time / total_time) * 100:.2f}% of total time",
    )


# entry point of script
if __name__ == "__main__":
    asyncio.run(main(),debug=True)
