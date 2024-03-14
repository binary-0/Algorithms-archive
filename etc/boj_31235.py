N = int(input())
A = list(map(int, input().split()))

curDist = 0
maxDist = 0
prevNum = 0

for i in range(0, N):
    if i == 0:
        curDist = 1
        maxDist = 1
        prevNum = A[i]
    else:
        if prevNum > A[i]: #if current number is smaller than previous number
            curDist += 1
            if curDist > maxDist:
                maxDist = curDist
        else:
            curDist = 1
            prevNum = A[i]
            
print(maxDist)