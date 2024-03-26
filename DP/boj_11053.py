seqSize = int(input())
seq = list(map(int, input().split()))

dp = [1 for _ in range(seqSize)]

for i in range(0, seqSize):
    for j in range(0, i):
        if seq[i] > seq[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))