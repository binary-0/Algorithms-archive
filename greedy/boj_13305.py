numCity = int(input())
lenRoadList = list(map(int, input().split()))
oilCostList = list(map(int, input().split()))

for i in range(numCity):
    oilCostList[i] = [oilCostList[i], i]
    
oilCostList.sort(key=lambda x:x[0])

curIdx = numCity - 1
totalCost = 0
for i in range(numCity):
    if curIdx > oilCostList[i][1]:
        roadLen = 0
        for j in range(oilCostList[i][1], curIdx):
            roadLen += lenRoadList[j]
        totalCost += oilCostList[i][0] * roadLen
        
        curIdx = oilCostList[i][1]
        
print(totalCost)