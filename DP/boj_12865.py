numItems, capacity = list(map(int, input().split()))

itemList = [[0, 0] for _ in range(numItems + 1)]
for i in range(1, numItems + 1):
    itemList[i] = list(map(int, input().split()))
    
dp = [[0 for _ in range(capacity + 1)] for _ in range(numItems + 1)]

for i in range(1, numItems + 1):
    for j in range(1, capacity + 1):
        weight = itemList[i][0]
        value = itemList[i][1]
        
        if j < weight:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

print(dp[numItems][capacity])