file = open("./new.csv", "r")
strings = file.read().splitlines()
bestStartTime = 0
bestEndTime = 0
bestProfit = 0
start = 1

for i in range(1, len(strings)):
    if float(strings[start].split(",")[3]) >= float(strings[i].split(",")[3]):
        start = i
    elif float(strings[i].split(",")[3]) - float(strings[start].split(",")[3]) > bestProfit:
        bestProfit = float(strings[i].split(",")[3]) - float(strings[start].split(",")[3])
        bestStartTime = start 
        bestEndTime = i 

print("buy: " + strings[bestStartTime].split(",")[1])
print("sell: " + strings[bestEndTime].split(",")[1])
print("profit: " + str(bestProfit))
