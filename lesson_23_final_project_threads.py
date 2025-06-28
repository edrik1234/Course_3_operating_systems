import time
import requests
import threading


NUMBER_OF_THREADS = 5
COUNTERS = [0] * NUMBER_OF_THREADS


def downloader(url, index, mutex):
    global COUNTERS
    response = requests.get(url)
    content = response.text
    with mutex:
        temp = COUNTERS[index]
        temp += len(content)
        time.sleep(0.0001)
        COUNTERS[index] = temp
        time.sleep(0.0001)


def main():
    mutex = threading.Lock()
    urls = [
        'https://jsonplaceholder.typicode.com/posts',
        'https://jsonplaceholder.typicode.com/comments',
        'https://jsonplaceholder.typicode.com/albums',
        'https://jsonplaceholder.typicode.com/photos',
        'https://jsonplaceholder.typicode.com/todos',
        'https://jsonplaceholder.typicode.com/users'
    ]
    threads_list = []
    for i in range (NUMBER_OF_THREADS):
        url = urls[i]    
        thread = threading.Thread(target = downloader, args = (url, i, mutex))
        threads_list.append(thread)
        thread.start()


    for thread in threads_list:
        thread.join()# here you tell three workers to dig at a same time 


    for index in range (NUMBER_OF_THREADS):
        print(f"thread number {index} downloaded {COUNTERS[index]} chars from {url}")
    counter = 0
    counter = sum(COUNTERS)
    print(f"the total chars is {counter}")


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"the total time of executing is {end - start} seconds")
