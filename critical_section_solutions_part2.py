import time, threading


COUNTER = 0


def worker(mutex, thread_number):
    global COUNTER
    for i in range(10000):
        print(thread_number)
        with mutex:
            temp = COUNTER
            temp += 1
            time.sleep(0.0001)
            COUNTER = temp
def main():
    mutex = threading.Lock()
    thread_1 = threading.Thread(target = worker, args = (mutex, 1))
    thread_2 = threading.Thread(target = worker, args = (mutex, 2))
    thread_3 = threading.Thread(target = worker, args =(mutex, 3))
    thread_1.start()
    thread_2.start()
    thread_3.start()


    thread_1.join()
    thread_2.join()
    thread_3.join()

    
    print(COUNTER)

if __name__ == "__main__":
    main()