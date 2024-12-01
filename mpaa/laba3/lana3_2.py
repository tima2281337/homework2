import itertools
import time

def get_max_activities_brute_force(S):
    max_subset = set()
    for r in range(len(S), 0, -1):
        for subset in itertools.combinations(S, r):
            subset1 = sorted(subset, key=lambda x: x[1])
            if is_compatible(subset1):
                max_subset = set(subset1)
                break
        if max_subset:
            break
    return max_subset

def is_compatible(subset):
    for i in range(len(subset)):
        for j in range(i + 1, len(subset)):
            if subset[i][1] > subset[j][0]:
                return False
    return True


def get_max_activities_greedy(processes):
    sorted_processes = sorted(processes, key=lambda x: x[1])
    result = [sorted_processes[0]]
    current = 0

    # Итерация по отсортированным процессам
    for i in range(1, len(sorted_processes)):
        # Если текущий процесс совместим с последним процессом в результате
        if sorted_processes[i][0] >= result[current][1]:
            result.append(sorted_processes[i])
            current += 1

    return result




# Замер времени работы алгоритмов
import random

def generate_processes(n):
    processes = []
    for _ in range(n):
        start = random.randint(0, 100)
        finish = start + random.randint(1, 50)
        processes.append((start, finish))
    return processes

n_values = [10, 20, 25]
brute_force_times = []
greedy_times = []

for n in n_values:
    processes = generate_processes(n)

    start_time = time.perf_counter()
    brute_force_subset = get_max_activities_brute_force(processes)
    brute_force_time = time.perf_counter() - start_time
    brute_force_times.append(brute_force_time)

    start_time = time.perf_counter()
    greedy_subset = get_max_activities_greedy(processes)
    greedy_time = time.perf_counter() - start_time
    greedy_times.append(greedy_time)

    
# Вывод результатов в таблицу
print("n | Brute Force Time | Greedy Time")
print("----------------------------------")
for n, brute_force_time, greedy_time in zip(n_values, brute_force_times, greedy_times):
    print(f"{n} | {brute_force_time:.6f} | {greedy_time:.6f}")
