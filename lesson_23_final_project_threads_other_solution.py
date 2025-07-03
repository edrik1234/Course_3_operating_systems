import time
import requests
import threading
import json

    

def downloader(url, index, COUNTERS):
    json_file =  requests.get(url).json()
    json_string = json.dumps(json_file)
    temp = COUNTERS[index]
    temp += len(json_string)
    COUNTERS[index] = temp
    time.sleep(0.0001)
    print(f"thread number {index} downloaded {temp} chars from {url}")
  

def main():
    urls = [
        'https://jsonplaceholder.typicode.com/posts',
        'https://jsonplaceholder.typicode.com/comments',
        'https://jsonplaceholder.typicode.com/albums',
        'https://jsonplaceholder.typicode.com/photos',
        'https://jsonplaceholder.typicode.com/todos',
        'https://jsonplaceholder.typicode.com/users'
    ]

    threads_list = []
    COUNTERS = [0] * len(urls)
    for i, url in enumerate(urls):
        thread = threading.Thread(target = downloader, args = (url, i, COUNTERS ))
        threads_list.append(thread)
        thread.start()


    for thread in threads_list:
        thread.join()# here you tell three workers to dig at a same time 
    total_chars = sum(COUNTERS)
    print(f"total chars is {total_chars}")
    


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"the total time of executing is {end - start} seconds")
