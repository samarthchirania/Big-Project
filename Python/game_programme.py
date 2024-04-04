import numpy as np


def constant_div(n, steps):
    tot = 0.5
    glasses = np.zeros(n)
    addition = tot / n
    max_water = 0
    overall_max = 0
    k = 0
    while k <= steps:
        if max_water <= 1:
            for i in range(n):
                glasses[i] += addition
            removal_index = glasses.argmax()
            if removal_index == n - 1:
                glasses[removal_index] = 0
                glasses[0] = 0
            else:
                glasses[removal_index] = 0
                glasses[removal_index + 1] = 0
            max_water = glasses.max()
            if max_water >= overall_max:
                overall_max = max_water

            print("No glasses full. Max water: " + str(max_water))
            print(glasses)
        else:
            print('A glass has overflown')
        k += 1
    print('Overall max water achieved = ', str(overall_max))
    return

def max_water(x,y):
    x = np.zeros(8)
    for i in len(y):
        x[i] = i
    return x

n = 8
steps = 20
constant_div(n, steps)
