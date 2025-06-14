import threading
import time
import random


def worker(thread_id, url, results):
    start_time = time.time()
    sleep_seconds = random.randint(1, 5) 
    time.sleep(sleep_seconds)
    end_time = time.time()


    execution_time = round(end_time - start_time, 2)
    

    results[thread_id] = {
        'url': url,
        'time': execution_time,
        'sleep': sleep_seconds
    }


def main():
    urls = [
        'https://jsonplaceholder.typicode.com/posts',
        'https://jsonplaceholder.typicode.com/comments',
        'https://jsonplaceholder.typicode.com/albums',
        'https://jsonplaceholder.typicode.com/photos',
        'https://jsonplaceholder.typicode.com/todos',
        'https://jsonplaceholder.typicode.com/users'
    ]


    threads = []
    results = {}


    for i, url in enumerate(urls):
        thread = threading.Thread(target = worker, args = (i, url, results))
        threads.append(thread)
        thread.start()


    for thread in threads:
        thread.join()

 
    for thread_id, info in results.items():
        print(f"Thread {thread_id} handled {info['url']} | Slept: {info['sleep']}s | Execution: {info['time']}s")


if __name__ == "__main__":
    main()
