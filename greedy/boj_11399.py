numPeople = int(input())
timeList = list(map(int, input().split()))
accList = [0 for i in range(numPeople)]
timeList.sort()

timeCnt = 0

for i in range(numPeople):
    timeCnt = timeCnt + timeList[i]
    accList[i] = timeCnt

ans = 0
for i in range(numPeople):
    ans += accList[i]
    
print(ans)