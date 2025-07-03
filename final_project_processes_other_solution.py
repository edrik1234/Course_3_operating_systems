import multiprocessing
import time
import requests


def downloader(url, index, queue):
    content = requests.get(url).json()
    file = json.load(content)
    string = json.dumps(file)
    len_string = len(string)
    sum_strings += string
    print(f"process numer {index} downloaded {len_string} chars from {url}")
    queue.put((index, url, len(string), sum_strings))
    

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

    results = [queue.get() for _ in urls] # results = [queue.get(), queue.gett()...]

    print(f"total string is: {sum_strings}")
    
    
    


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"Total time: {end - start:.3f} seconds")
