import multiprocessing.process
import os
import time
import multiprocessing


def main():
    print(f"The Main pid is: {(os.getpid())} , and the main parent pid is: {(os.getppid())}")
    time.sleep(3) # sleep 3(s)
    process = multiprocessing.Process(target = second, args = (23,"edrian"))
    process.start()
    process.join()


def second(age, name):
    print(f"the name is: {name} , and age is: {age}")
    print(f"The Seconday pid is: {(os.getpid())} , and the Secondary  parent pid is: {(os.getppid())}")
    time.sleep(2)
    for i in range(0, age+1, 1):
        print(i)





if __name__ == "__main__":
    main()