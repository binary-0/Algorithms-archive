N = int(input())

numList = []
for i in range(N):
    numList.append(int(input()))
    
numList.sort()

for num in numList:
    print(num)