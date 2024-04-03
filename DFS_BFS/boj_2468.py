from collections import deque

N = int(input())
areaMap = [[0 for _ in range(N)] for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

for i in range(N):
    rowList = list(map(int, input().split()))
    for j in range(N):
        areaMap[i][j] = rowList[j]
        
def bfs(TH, row, col):
    queue = deque()
    queue.append((row, col))   
    visited[row][col] = True
    
    while queue:
        nextRow, nextCol = queue.popleft()
        
        if nextRow + 1 < N and areaMap[nextRow + 1][nextCol] > TH and visited[nextRow + 1][nextCol] == False:
            queue.append((nextRow + 1, nextCol))
            visited[nextRow + 1][nextCol] = True
        if nextRow - 1 >= 0 and areaMap[nextRow - 1][nextCol] > TH and visited[nextRow - 1][nextCol] == False:
            queue.append((nextRow - 1, nextCol))
            visited[nextRow - 1][nextCol] = True
        if nextCol + 1 < N and areaMap[nextRow][nextCol + 1] > TH and visited[nextRow][nextCol + 1] == False:
            queue.append((nextRow, nextCol + 1))
            visited[nextRow][nextCol + 1] = True        
        if nextCol - 1 >= 0 and areaMap[nextRow][nextCol - 1] > TH and visited[nextRow][nextCol - 1] == False:
            queue.append((nextRow, nextCol - 1))
            visited[nextRow][nextCol - 1] = True        
    
        
maxCount = 0
for rainTH in range(0, 101):
    count = 0
    
    for i in range(N):
        for j in range(N):
            visited[i][j] = False
            
    for i in range(N):
        for j in range(N):
            if areaMap[i][j] > rainTH and visited[i][j] == False:
                count += 1
                bfs(rainTH, i, j)
                
    if count > maxCount:
        maxCount = count
        
print(maxCount)