"""
This module contains generic, reusable functions for timing
experiments, complexity estimation, and plotting. These functions
know nothing about the specific algorithm being tested (3-sum,
sorting, etc.) -- they just take a function as a parameter and work
with whatever it does. This lets experiment1.py (Part 1) and
experiment2.py (Part 2) share the same experiment infrastructure.
"""

import time
import math
import matplotlib.pyplot as plt


def logspace_sizes(n_min, n_max, count):
    log_min = math.log2(n_min)
    log_max = math.log2(n_max)
    step = (log_max - log_min) / (count - 1)

    sizes = []
    for i in range(count):
        log_val = log_min + i * step
        sizes.append(round(2 ** log_val))

    return sorted(set(sizes))


def run_experiment(sizes, func, generate_input, num_runs=3):
    times = []

    for run in range(num_runs):
        run_times = []
        for n in sizes:
            data = generate_input(n)
            start = time.perf_counter()
            func(data)
            elapsed = time.perf_counter() - start
            run_times.append(elapsed)
        times.append(run_times)

    return times


def average_times(times):
    result = []
    for vals in zip(*times):
        avg = sum(vals) / len(vals)
        result.append(avg)
    return result


def lin_reg(x, y):
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    sum_x2 = sum(xi ** 2 for xi in x)

    k = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    m = (sum_y / n) - k * (sum_x / n)

    return m, k


def estimate_complexity(sizes, avg_times, label):
    log_sizes = [math.log2(n) for n in sizes]
    log_times = [math.log2(t) for t in avg_times]

    m, k = lin_reg(log_sizes, log_times)
    print(f"{label}: estimated complexity exponent k = {k:.3f}")

    return log_sizes, log_times, m, k


def plot_runs(sizes, times, title):
    plt.figure()
    for i, run_times in enumerate(times):
        plt.plot(sizes, run_times, marker='o', label=f"Run {i+1}")

    plt.xlabel("List size (n)")
    plt.ylabel("Time (seconds)")
    plt.title(title)
    plt.legend()
    plt.show()


def plot_averages(sizes, avg_times, title):
    plt.figure()
    plt.plot(sizes, avg_times, marker='o')
    plt.xlabel("List size (n)")
    plt.ylabel("Aberage time (seconds)")
    plt.title(title)
    plt.show()


def plot_loglog(log_sizes, log_times, m, k, title):
    plt.figure()
    plt.scatter(log_sizes, log_times, label="data")

    fit_line = [m + k * x for x in log_sizes]
    plt.plot(log_sizes, fit_line, color='red', label=f"fit, k={k:.3f}")

    plt.xlabel("log2(list size)")
    plt.ylabel("log2(time)")
    plt.title(title)
    plt.legend()
    plt.show()
