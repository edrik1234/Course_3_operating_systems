import threading
import time
import random


def worker(thread_id, text):
    time.sleep(random.randint(0,10))
    print(f"thread id is: {thread_id}, and text is {text}")


def main():
    num_of_threads = 5
    thread_list = []
    for i in range (num_of_threads):
        thread = threading.Thread(target = worker, args = (i, "Good Morning"))
        thread.start()
        thread_list.append(thread)
    

    for thread in thread_list:
        thread.join()


if __name__ == "__main__":
    main()