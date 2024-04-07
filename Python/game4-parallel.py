import concurrent
from concurrent.futures import ProcessPoolExecutor
import random


def simulate_process(k):
    arr = [0, 0, 0, 0]  # Initial array
    largest_value = 0  # To keep track of the largest value encountered

    for _ in range(k):
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

        # Add the random vector to the array
        arr = [arr[i] + addition_vector[i] for i in range(4)]
        current_max = max(arr)
        if current_max > largest_value:
            largest_value = current_max

        # Removal process - executed in each iteration regardless of array values
        max_index = arr.index(max(arr))  # Index of the largest number
        left_index = (max_index - 1) % 4  # Circular left neighbor
        right_index = (max_index + 1) % 4  # Circular right neighbor

        # Determine the larger of the two adjacent elements
        larger_adjacent_index = left_index if arr[left_index] > arr[right_index] else right_index

        # Set the largest and the larger adjacent number to 0
        arr[max_index], arr[larger_adjacent_index] = 0, 0

        # Update the largest value if necessary
        current_max = max(arr)
        if current_max > largest_value:
            largest_value = current_max

        # Check for overfill
        if any(element > 1 for element in arr):
            return largest_value

    return largest_value


def run_parallel(k, n):
    largest_values = []  # To store the largest values from each run
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(simulate_process, k) for _ in range(n)]
        for future in concurrent.futures.as_completed(futures):
            largest_values.append(future.result())
    return largest_values


# Note: Uncomment the following lines to run the simulation with multicore processing
if __name__ == '__main__':

    k = 400_000  # Number of iterations for each simulation
    n = 10  # Number of parallel simulations
    print('Simulation Begun')
    largest_values = run_parallel(k, n)
    print(max(largest_values))
    print('Simulation End')
# The function calls and multiprocessing execution will be uncommented and tested in the final step.
