import numpy as np
import matplotlib.pyplot as plt


def constant_div(n_1, steps_1):
    tot = 0.5
    glasses = np.zeros(n_1)
    addition = tot / n_1
    max_water = 0
    overall_max = 0
    k = 0
    while k <= steps_1:
        if max_water <= 1:
            for i in range(n_1):
                glasses[i] += addition
            removal_index = glasses.argmax()
            if removal_index == n_1 - 1:
                glasses[removal_index] = 0
                glasses[0] = 0
            else:
                glasses[removal_index] = 0
                glasses[removal_index + 1] = 0
            max_water = glasses.max()
            if max_water >= overall_max:
                overall_max = max_water

            #print("No glasses full. Max water: " + str(max_water))
            #print(glasses)
        else:
            return overall_max
        k += 1
    #print('Overall max water achieved = ', str(overall_max))
    return overall_max


def constant_div_2(n_2, steps_2):
    tot = 0.5
    glasses = np.zeros(n_2)
    addition = (tot * 2) / n_2
    max_water = 0
    overall_max = 0
    k = 0
    addition_index = np.arange(0, n_2, 2)
    while k <= steps_2:
        if max_water <= 1:
            for i in addition_index:
                glasses[i] += addition
            removal_index = glasses.argmax()
            if removal_index == n_2 - 1:
                glasses[removal_index] = 0
                glasses[0] = 0
            else:
                glasses[removal_index] = 0
                glasses[removal_index + 1] = 0
            max_water = glasses.max()
            if max_water >= overall_max:
                overall_max = max_water

            #print("No glasses full. Max water: " + str(max_water))
        else:
            return overall_max
        k += 1

        #print('Overall max water achieved = ', str(overall_max))
    return overall_max


constant_div_2(n, steps)

n_s = [5, 10, 20, 40, 50, 80, 100, 150, 200, 500, 800, 1000]
steps = 200_000


def variable_div(n, steps, space):
    tot = 0.5
    glasses = np.zeros(n)
    addition = ((tot * space) / n)
    max_water = 0
    overall_max = 0
    k = 0
    addition_index = np.arange(0, n, space)
    while k <= steps:
        if max_water <= 1:
            for i in addition_index:
                glasses[i] += addition
            removal_index = glasses.argmax()
            if removal_index == n-1:
                glasses[removal_index] = 0
                glasses[0] = 0
            else:
                glasses[removal_index] = 0
                glasses[removal_index + 1] = 0
            max_water = glasses.max()
            if max_water >= overall_max:
                overall_max = max_water
            if overall_max > 1:
                return overall_max
        k += 1
    return overall_max


n_s = [10, 20, 40, 50, 80, 100, 150, 200, 500, 800, 1000]
steps = 200_000
space = [1, 2, 3, 4, 5, 6, 7]
for i in space:
    water_level = []  # Initialize the list for this space configuration
    for j in n_s:
        level = variable_div(j, steps, i)  # Get the water level for the current configuration
        water_level.append(level)  # Append to the list
        print('Done for ', str(j), 'glasses with gap of', str(i) )
    plt.plot(n_s, water_level, label=f'Gap of {i}')  # Plot for the current space configuration

plt.legend()
plt.xlabel('Number of Glasses')
plt.ylabel('Maximum Water level')  # Corrected from plt.plot to plt.ylabel for the label
plt.show()