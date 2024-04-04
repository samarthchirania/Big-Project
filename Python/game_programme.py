import numpy as np

def constant_div(n):
    tot = 0.5
    glasses = np.zeros(n)
    addition = tot/n
    max_water = 0
    while max_water <= 1:
        if max_water <=1:
            for i in range(n):
                glasses[i] += addition
            removal_index = glasses.argmax()
            if removal_index == n-1:
                glasses[removal_index] = 0
                glasses[0] = 0
            else:
                glasses[removal_index] = 0
                glasses[removal_index+1] = 0
            max_water = glasses.max()
            print("No glasses full. Max water: " + str(max_water))
            print(glasses)
        else:
            print('A glass has overflown')
SSAYE
