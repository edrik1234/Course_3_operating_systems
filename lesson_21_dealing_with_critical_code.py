import threading
import time

NUMBER_OF_THREADS = 3
COUNTERS = [0] * NUMBER_OF_THREADS

def worker(index):
    global COUNTERS
    for i in range(10000):
      #  with mutex:
            temp = COUNTERS[index]
            temp += 1
            time.sleep(0.0001)
            COUNTERS[index] = temp

def main():
   # mutex = threading.Lock()
    threads = []
    for i in range(NUMBER_OF_THREADS):
        thread = threading.Thread(target = worker, args = (i))
        threads.append(thread)
        thread.start()
        thread.join()# you tell 1 worker do a parrallel dig instead of three workers at the same time

   # for thread in threads:
  #      thread.join()
    
    counter = sum(COUNTERS)
    print(counter)

if __name__ == "__main__":
    main()

