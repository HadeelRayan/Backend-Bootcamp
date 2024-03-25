import time
import random as rd
import threading


def do_somthing():
    print('sleeping for randomly time')
    sleeping_time = rd.uniform(0, 5)
    time.sleep(sleeping_time)
    print(f'Done sleeping for: {sleeping_time:.2f} seconds')


def main():
    start = time.perf_counter()
    threads = []

    for i in range(0, 4):
        print(f'Runnig thread {i}')
        thread = threading.Thread(target=do_somthing)
        thread.start()
        #thread.join()
        threads.append(thread)

    for thread in threads:
        thread.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} seconds')


if __name__ == "__main__":
    main()
