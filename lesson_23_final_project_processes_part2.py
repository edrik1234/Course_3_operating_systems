import multiprocessing
import time
import requests


def downloader(url, process_index, queue, shared_total, shared_data, lock = None):
    response = requests.get(url)
    content = response.text
    char_count = len(content)
    time.sleep(0.001)


    if lock:
        with lock:
            time.sleep(0.001)
            shared_total.value += char_count

   
    if lock:
        with lock:
            shared_data[url] = {
                'chars': char_count,
                'source': process_index
            }


    queue.put((process_index, url, char_count))


def main(lock = True):
    queue = multiprocessing.Queue()
    lock = multiprocessing.Lock() if lock else None
    shared_total = multiprocessing.Value('i', 0)
    manager = multiprocessing.Manager()
    shared_data = manager.dict()


    urls = [
       'https://jsonplaceholder.typicode.com/posts',
        'https://jsonplaceholder.typicode.com/comments',
        'https://jsonplaceholder.typicode.com/albums',
        'https://jsonplaceholder.typicode.com/photos',
        'https://jsonplaceholder.typicode.com/todos',
        'https://jsonplaceholder.typicode.com/users'
    ]


    processes = []
    for i, url in enumerate(urls):
        process = multiprocessing.Process( target = downloader, args = (url, i, queue, shared_total, shared_data, lock) )  
        process.start()
        processes.append(process)


    for process in processes:
        process.join()


    results = []
    while not queue.empty():
        index, url, char_count = queue.get()
        results.append((index, url, char_count))


    results.sort()
    for index, url, char_count in results:
        print(f"Process {index} downloaded {char_count} chars from {url}")
    print(f"Shared total characters from all processes: {shared_total.value}")


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"total time is {start - end}")

