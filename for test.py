import threading
import time

def code1():
    """
    Code 1 – Uses a standard Lock to protect a shared counter.
    """
    COUNTER = 0
    mutex = threading.Lock()

    def worker(mutex, thread_number):
        nonlocal COUNTER
        for i in range(10000):
            print(f"Thread {thread_number}")
            with mutex:
                temp = COUNTER
                temp += 1
                time.sleep(0.0001)
                COUNTER = temp

    thread_1 = threading.Thread(target = worker, args = (mutex, 1))
    thread_2 = threading.Thread(target = worker, args = (mutex, 2))

    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()

    print(f"[Code 1] Final counter: {COUNTER}")

def code2():
    """
    Code 2 – Each thread works with its own counter (no synchronization needed).
    This is an efficient and scalable technique often used in industry.
    """
    NUMBER_OF_THREADS = 2
    COUNTERS = [0] * NUMBER_OF_THREADS

    def worker(index):
        for i in range(10000):
            temp = COUNTERS[index]
            temp += 1
            time.sleep(0.0001)
            COUNTERS[index] = temp

    threads = []
    for i in range(NUMBER_OF_THREADS):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total = sum(COUNTERS)
    print(f"[Code 2] Final counter: {total}")

def code3():
    """
    Code 3 – Similar to Code 2 but initially had incorrect thread.join() inside the loop.
    Fixed to allow proper parallel execution.
    """
    NUMBER_OF_THREADS = 2
    COUNTERS = [0] * NUMBER_OF_THREADS

    def worker(index):
        for i in range(10000):
            print(f"Thread index is {index}")
            temp = COUNTERS[index]
            temp += 1
            time.sleep(0.0001)
            COUNTERS[index] = temp

    threads = []
    for i in range(NUMBER_OF_THREADS):
        thread = threading.Thread(target = worker, args = (i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total = sum(COUNTERS)
    print(f"[Code 3] Final counter: {total}")

def code4():
    """
    Code 4 – Busy-waiting using a Lock.
    This approach wastes CPU and is shown here for learning purposes only.
    """
    COUNTER = 0
    lock = threading.Lock()

    def busy_acquire(lock):
        while not lock.acquire(blocking = False):
            continue  # Busy-wait: spins until the lock becomes available

    def worker(thread_number):
        nonlocal COUNTER
        for i in range(10000):
            print(f"Thread {thread_number}")
            busy_acquire(lock)
            try:
                temp = COUNTER
                temp += 1
                time.sleep(0.0001)
                COUNTER = temp
            finally:
                lock.release()

    thread_1 = threading.Thread(target=worker, args=(1,))
    thread_2 = threading.Thread(target=worker, args=(2,))

    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()

    print(f"[Code 4] Final counter: {COUNTER}")

def code5():
    """
    Code 5 – Using a Semaphore to control access to the critical section.
    A semaphore can allow a limited number of threads inside the critical region.
    """
    COUNTER = 0
    semaphore = threading.Semaphore(2)  # You can change this to 1 for exclusive access

    def worker(thread_number):
        nonlocal COUNTER
        for i in range(10000):
            semaphore.acquire()
            try:
                print(f"Thread {thread_number} entered semaphore")
                temp = COUNTER
                temp += 1
                time.sleep(0.0001)
                COUNTER = temp
            finally:
                semaphore.release()

    thread_1 = threading.Thread(target=worker, args=(1,))
    thread_2 = threading.Thread(target=worker, args=(2,))

    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()

    print(f"[Code 5] Final counter: {COUNTER}")

def main():
    print("Choose which code to run:")
    print("1 - Lock (standard mutual exclusion)")
    print("2 - Per-thread counter (no lock needed)")
    print("3 - Fixed .join() issue (parallel threads)")
    print("4 - Busy-Wait using Lock (for demonstration)")
    print("5 - Semaphore (control number of concurrent threads)")

    choice = input("Enter code number (1-5): ").strip()

    if choice == "1":
        code1()
    elif choice == "2":
        code2()
    elif choice == "3":
        code3()
    elif choice == "4":
        code4()
    elif choice == "5":
        code5()
    else:
        print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()
