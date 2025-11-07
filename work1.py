from multiprocessing import Process, Queue
import time


def worker(start, end, q):
    total = 0
    for i in range(start, end + 1):
        total += i * i
    q.put(total)


if __name__ == "__main__":
    start_time = time.time()

    N = int(input("Enter N: "))
    processes = 8
    step = N // processes

    q = Queue()
    procs = []

    for i in range(processes):
        start = i * step + 1
        end = (i + 1) * step
        if i == processes - 1:
            end = N

        p = Process(target=worker, args=(start, end, q))
        procs.append(p)
        p.start()

    total = 0
    for _ in range(processes):
        total += q.get()

    for p in procs:
        p.join()

    end_time = time.time()

    print(f"Sum Squared: {total}")
    print(f"Time Taken: {end_time - start_time:.4f} seconds")

