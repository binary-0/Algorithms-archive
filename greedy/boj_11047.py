N, K = list(map(int, input().split()))
coinList = []
cnt = 0

for i in range(0, N):
    coinList.append(int(input()))
    
for i in range(N - 1, -1, -1): #from N-1 to 0 (index ref)
    cnt += K // coinList[i]
    K %= coinList[i]
    
print(cnt)