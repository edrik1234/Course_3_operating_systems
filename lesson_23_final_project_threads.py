import time
import requests
import threading
import json

def downloader(url, index, results):

        response = requests.get(url)
        json_data = json.loads(response.text)
        json_string = json.dumps(json_data)
        char_count = len(json_string)
        results[index] = char_count
        print(f"✅ Thread {index} downloaded {char_count} chars from {url}")
    
def main():
    urls = [
        'https://jsonplaceholder.typicode.com/posts',
        'https://jsonplaceholder.typicode.com/comments',
        'https://jsonplaceholder.typicode.com/albums',
        'https://jsonplaceholder.typicode.com/photos',
        'https://jsonplaceholder.typicode.com/todos',
        'https://jsonplaceholder.typicode.com/users'
    ]

    # מערך תוצאות – לא גלובלי, עובר כ־argument בלבד
    results = [0] * len(urls)
    threads = []

    for i, url in enumerate(urls):
        thread = threading.Thread(target=downloader, args=(url, i, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total = sum(results)
    print(f"\n📦 Total characters downloaded: {total}")

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"⏱️ Execution time: {end - start:.3f} seconds")
