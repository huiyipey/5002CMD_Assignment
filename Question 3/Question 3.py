# generate 100 random number (0-10000)
# generate 3 set random number (1 set 100 num) (func up)
# multithreading - create separate thread (3 thread each set one)
# measure time taken (nanosecond) for generate 3 set random number
# Time_Elapsed = End_Time_Of_Thread_Finished_Last – Start_Time_Of_Thread_That_Started_First
# generate 3 set 10 rounds (time taken each and average time taken)
# generate 3 set 10 rounds (no multithreading) (time taken each and average)
import random
import threading
import time

def generate_numbers():
    return [random.randint(0, 10001) for _ in range(100)]

def worker(thread_index, nums, start_times, end_times):
    start_times[thread_index] = time.perf_counter_ns()
    nums[thread_index] = generate_numbers()
    end_times[thread_index] = time.perf_counter_ns()
    # time.sleep(0.01)

def multithreaded():
    round_times = []

    for r in range(10):
        rand_num = {}
        start_times = {}
        end_times = {}
        threads = []

        for i in range(3):
            thread = threading.Thread(target=worker, args=(i, rand_num, start_times, end_times))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        t1 = min(start_times.values())
        t2 = max(end_times.values())
        elapsed_time = t2 - t1
        round_times.append(elapsed_time)

        # for i in range(3):
        #     thread = threading.Thread(target=generate_numbers)
        #     threads.append(thread)
        #     thread.start()
        #
        # start = time.time_ns()
        # for thread in threads:
        #     thread.join()
        # end = time.time_ns()
        # round_times.append(end - start)

    return round_times

def single_threaded():
    round_times = []

    for r in range(10):
        start_time = time.perf_counter_ns()

        for i in range(3):
            generate_numbers()

        elapsed_time = time.perf_counter_ns() - start_time
        round_times.append(elapsed_time)

    return round_times

def print_results(multi_times, single_times):
    """Print results in the requested table format"""
    print("\nRound-by-Round Performance Comparison:")
    print("+-------+--------------------------+------------------------------+-----------------+")
    print("| Round | Multithreading Time (ns) | Non-Multithreading Time (ns) | Difference (ns) |")
    print("+-------+--------------------------+------------------------------+-----------------+")

    for i in range(10):
        print(f"| {i+1:^5} | {multi_times[i]:^24} | {single_times[i]:^28} | {multi_times[i] - single_times[i]:^15} |")

    print("+-------+--------------------------+------------------------------+-----------------+")

    # Summary section
    total_multi = sum(multi_times)
    total_single = sum(single_times)
    avg_multi = total_multi / len(multi_times)
    avg_single = total_single / len(single_times)

    print("\nSummary of Results:")
    print("+--------------+---------------------+-------------------------+-----------------+")
    print("|    Metric    | Multithreading (ns) | Non-Multithreading (ns) | Difference (ns) |")
    print("+--------------+---------------------+-------------------------+-----------------+")
    print(f"| {'Total Time':^6}   | {total_multi:^20}| {total_single:^24}| {total_single - total_multi:^14}  |")
    print(f"| {'Average TIme':^6} | {avg_multi:^20.1f}| {avg_single:^24.1f}| {avg_single - avg_multi:^14.1f}  |")
    print("+--------------+---------------------+-------------------------+-----------------+")

def main():
    # print("===== Threading Performance Test =====")

    # Run tests
    multi_times = multithreaded()
    single_times = single_threaded()

    # Print formatted results
    print_results(multi_times, single_times)

if __name__ == "__main__":
    main()