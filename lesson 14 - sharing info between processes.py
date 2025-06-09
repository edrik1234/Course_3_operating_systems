import multiprocessing.process
import os
import time
import multiprocessing


def main():
    print(f"The Main pid is: {(os.getpid())} , and the main parent pid is: {(os.getppid())}")
    process = multiprocessing.Process(target = second, args = (23,"edrian"))
    process.start()
    print("between start and join ")
    time.sleep(5)
    print("two")
    time.sleep(5)
    print("three")
    process.join()
    print("done")

def second(age, name):
    time.sleep(5)
    print(f"the name is: {name} , and age is: {age}")
    print(f"The Seconday pid is: {(os.getpid())} , and the Secondary  parent pid is: {(os.getppid())}")
    for i in range(0, age+1, 1):
        time.sleep(1)
        print(i)
    return 10




if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time  = time.time()
    print(end_time - start_time)