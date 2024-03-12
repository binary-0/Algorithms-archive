N = input()
A = list(map(int, input().split()))

minSet = [-1 for _ in range(int(N))]

prevIdx = 0
prevMinSet = 0
prev = 0

for i in range(0, len(A)):
    idx = len(A) - 1 - i
    
    if i == 0:
        prev = A[idx]
        prevIdx = idx
        prevMinSet = -1
        
        minSet[idx] = prevMinSet
    else:
        if prev == A[idx]:
            minSet[idx] = prevMinSet
        else:
            minSet[idx] = idx + 2
            
            prev = A[idx]
            prevIdx = idx
            prevMinSet = idx + 2
            
for i in range(0, len(A)):
    print(minSet[i], end=" ")
    
print()
            
    
    