import threading
import time

NUMBER_OF_THREADS = 2
COUNTERS = [0] * NUMBER_OF_THREADS

def worker(index):
    global COUNTERS
    for i in range(10000):
        temp = COUNTERS[index]
        temp += 1
        time.sleep(0.0001)
        print(index)
        COUNTERS[index] = temp

def main():
    threads = []
    for i in range(NUMBER_OF_THREADS):
        thread = threading.Thread(target = worker, args=(i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()# here you tell three workers to dig at a same time 
    
    counter = 0
    for thread in COUNTERS:
        counter += thread

    #____________________________
        counter = sum(COUNTERS)
        print(counter)

if __name__ == "__main__":
    main()

