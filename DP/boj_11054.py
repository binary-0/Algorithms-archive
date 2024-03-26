seqSize = int(input())
seq = list(map(int, input().split()))

dp = [[1, 1] for _ in range(seqSize)] #index 0: increasing, index 1: decreasing

for i in range(0, seqSize):
    for j in range(0, i):
        if seq[i] > seq[j]:
            dp[i][0] = max(dp[j][0] + 1, dp[i][0])
        elif seq[i] < seq[j]:
            dp[i][1] = max(dp[j][1] + 1, dp[i][1], dp[j][0] + 1)

maxSize = 0
for i in range(seqSize):
    if dp[i][0] > maxSize:
        maxSize = dp[i][0]
        
    if dp[i][1] > maxSize:
        maxSize = dp[i][1]
        
print(maxSize)