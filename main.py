import heapq

def parallel_processing(n, m, data):
    output = []

    threads = [(0, i) for i in range(n)]
    heapq.heapify(threads)

    for job_time in data:
        time, thread_index = heapq.heappop(threads)
        output.append((thread_index, time))
        heapq.heappush(threads, (time + job_time, thread_index))
    return output


def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)
    
    for thread_index, start_time in result:
        print(thread_index, start_time)


if __name__ == "__main__":
    main()
