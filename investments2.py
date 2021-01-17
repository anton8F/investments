#
#   this code wasn't completed
#
import math

file = open("./new.csv", "r")
strings = file.read().splitlines()
start = 0
growths = []
prices = []

for i in range(1, len(strings)):
    prices.append(float(strings[i].split(",")[3]))

for i in range(0, len(prices)):
    if i == len(prices) - 1 or prices[i+1] - prices[i] < 0:
        if start == i:
            start = i+1
            continue
        growths.append([start, i])
        start = i+1

while len(growths) > 2:
    minLoss = math.inf
    minLossGrowthsNum = 0
    for i in range(0, len(growths) - 1):
        if prices[growths[i][1]] - prices[growths[i + 1][0]] < minLoss:
            minLoss = prices[growths[i][1]] - prices[growths[i + 1][0]]
            minLossGrowthsNum = i
    growths[minLossGrowthsNum][1] = growths[minLossGrowthsNum+1][1]
    growths.pop(minLossGrowthsNum+1)

    
for i in range(2):
    print("buy: " + strings[growths[i][0]+1].split(",")[1])
    print("sell: " + strings[growths[i][1]+1].split(",")[1])
    print("profit: " + str(prices[growths[i][1]] - prices[growths[i][0]]))


