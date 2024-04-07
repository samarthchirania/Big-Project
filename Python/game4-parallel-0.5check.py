import concurrent
from concurrent.futures import ProcessPoolExecutor
import random


def simulate_process(k):
    arr = [0, 0, 0, 0]  # Initial array
    steps = []  # To track all steps

    for i in range(k):  # Loop for k iterations
        # Randomly select parts for the addition vector
        r = random.randint(0, 20)
        j = random.randint(0, 20 - r)
        l = random.randint(0, 20 - r - j)
        m = 20 - r - j - l  # Remaining parts for the last element

        # Convert these parts into fractions of 0.5
        addition_vector = [
            0.5 * (r / 20),
            0.5 * (j / 20),
            0.5 * (l / 20),
            0.5 * (m / 20)
        ]

        arr = [arr[i] + addition_vector[i] for i in range(4)]
        steps.append(('Addition', i + 1, addition_vector, arr.copy()))

        # Perform the removal process
        max_index = arr.index(max(arr))  # Index of the largest number
        left_index = (max_index - 1) % 4  # Circular left neighbor
        right_index = (max_index + 1) % 4  # Circular right neighbor

        # Determine the larger of the two adjacent elements
        larger_adjacent_index = left_index if arr[left_index] > arr[right_index] else right_index

        # Set the largest and the larger adjacent number to 0
        arr[max_index], arr[larger_adjacent_index] = 0, 0
        steps.append(('Removal', i + 1, [max_index, larger_adjacent_index], arr.copy()))

        # Check if any value is greater than 0.5 only after the removal step
        if any(value > 0.5 for value in arr):
            return steps  # Return all steps up to this point including the removal step

    return False  # Return all steps if the condition is never met within k iterations


def run_parallel(k, n):
    results = []
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(simulate_process, k) for _ in range(n)]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())
    return results


# Main guard to prevent code execution on import by multiprocessing
if __name__ == '__main__':
    k = 300_000_0  # Maximum number of iterations for each simulation
    n = 10  # Number of parallel simulations to run
    results = run_parallel(k, n)

    # Print the steps for simulations where an element exceeded 0.5
    for simulation_result in results:
        if simulation_result:  # Check if the simulation result is not empty
            print("Simulation Steps where an element exceeded 0.5:")
            for step in simulation_result:
                print(step)
            print("End of Simulation\n---")
        else:
            print('Simulation Never Exceeded 0.5 value')