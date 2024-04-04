import numpy as np
import matplotlib.pyplot as plt
from concurrent.futures import ProcessPoolExecutor

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
            if removal_index == n - 1:
                glasses[removal_index] = 0
                glasses[0] = 0
            else:
                glasses[removal_index] = 0
                if removal_index + 1 < n:
                    glasses[removal_index + 1] = 0
            max_water = glasses.max()
            if max_water >= overall_max:
                overall_max = max_water
            if overall_max > 1:
                return overall_max
        k += 1
    return overall_max

def worker(space_value):
    water_level_for_space = []
    for n in n_s:
        level = variable_div(n, steps, space_value)
        water_level_for_space.append(level)
    return (space_value, water_level_for_space)

n_s = [10, 20, 40, 50, 80, 100, 150, 200, 500, 800, 1000]
steps = 200_000
space = [1, 2, 3, 4, 5, 6, 7]

with ProcessPoolExecutor() as executor:
    results = list(executor.map(worker, space))

for space_value, water_levels in sorted(results):
    plt.plot(n_s, water_levels, label=f'Gap of {space_value}')

plt.legend()
plt.xlabel('Number of Glasses')
plt.ylabel('Maximum Water Level')
plt.show()
