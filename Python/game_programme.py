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

            print("No glasses full. Max water: " + str(max_water))
            print(glasses)
        else:
            print('A glass has overflown')
        k += 1
    print('Overall max water achieved = ', str(overall_max))
    return


n = 1000
steps = 2000000

# constant_div(n, steps)


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


# constant_div_2(n, steps)

n_s = [5, 10, 20, 40, 50, 80, 100, 150, 200, 500, 800, 1000]
steps = 200_000
waters = []
for i in range(len(n_s)):

    waters.append(constant_div_2(n_s[i], steps))
    print('Sim for ' + str(n_s[i]) + ' is ' + str(waters[i]))
    print(waters)

plt.plot(n_s, waters)
plt.xlabel('Number of glasses')
plt.ylabel('Maximum water at any point')
plt.show()



