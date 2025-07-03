import multiprocessing
import time
import requests
import json


def downloader(url, index, queue):
    json_data = requests.get(url).json()
    json_string = json.dumps(json_data)
    len_string = len(json_string)
    print(f"process numer {index} downloaded {len_string} chars from {url}")
    queue.put(len_string)
    time.sleep(0.01)
    

def main():
    urls = [
        'https://jsonplaceholder.typicode.com/posts',
        'https://jsonplaceholder.typicode.com/comments',
        'https://jsonplaceholder.typicode.com/albums',
        'https://jsonplaceholder.typicode.com/photos',
        'https://jsonplaceholder.typicode.com/todos',
        'https://jsonplaceholder.typicode.com/users'
    ]
    queue = multiprocessing.Queue()
    processes = []
    for i, url in enumerate(urls):
        process = multiprocessing.Process(target = downloader, args = (url, i, queue))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()


    total_length = 0
    for _ in urls:
        total_length += queue.get()
    print(f"total strings is: {total_length}")


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Total time: {end - start:.3f} seconds")