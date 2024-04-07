# Function updated to keep track of the largest value encountered in the array
def modify_array(k_iterations):
    import random  # To generate random numbers

    arr = [0, 0, 0, 0]  # Initial array
    steps = []  # To keep track of steps
    largest_value = 0  # To keep track of the largest value encountered

    for _ in range(k_iterations):
        # Randomly select parts for the addition vector
        k = random.randint(0, 20)
        j = random.randint(0, 20 - k)
        l = random.randint(0, 20 - k - j)
        m = 20 - k - j - l  # Remaining parts for the last element

        # Convert these parts into fractions of 0.5
        addition_vector = [
            0.5 * (k / 20),
            0.5 * (j / 20),
            0.5 * (l / 20),
            0.5 * (m / 20)
        ]

        # Add the random vector to the array
        arr = [arr[i] + addition_vector[i] for i in range(4)]
        steps.append(('Addition', addition_vector, arr.copy()))
        # Update the largest value if the current max exceeds it
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
        steps.append(('Removal', [max_index, larger_adjacent_index], arr.copy()))

        # Update the largest value if necessary
        current_max = max(arr)
        if current_max > largest_value:
            largest_value = current_max

        # Check for overfill after removal
        if any(element > 1 for element in arr):
            print("A glass overfilled")
            return steps, largest_value
    print('Simulation complete')
    return steps, largest_value

# Note: The function call will be uncommented and tested in the final step after the code review and optimization.

# Test the function (this call will be uncommented later)
steps_made, largest_value_encountered = modify_array(10_000)
# for step in steps_made:
#     print(step)
print("Largest value encountered:", largest_value_encountered)

