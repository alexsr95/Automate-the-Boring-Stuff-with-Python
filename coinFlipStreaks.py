#Heads and tails analysis
import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    #Code that creates a list of 100 heads or tails values
    flips = []
    for i in range(100):
        flips.append(random.choice(['H', 'T']))
    #Code that checks if there is a streak of 6 heads or tails in a row.
    streakFound = False
    count = 1
    for i in range(1, len(flips)):
        if flips[i] == flips[i -1]:
            count += 1
            if count == 6:
                numberOfStreaks += 1
                break
        else:
            count = 1
print('Chance of streak %s%%' % (numberOfStreaks / 100))