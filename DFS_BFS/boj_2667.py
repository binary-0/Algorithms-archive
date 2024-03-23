from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
map = [[0 for _ in range(N)] for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

for i in range(N):
    row = input()
    for j in range(N):
        map[i][j] = row[j]
        
def BFS(N, row, col):
    queue = deque()
    houseCnt = 0
    
    queue.append((row, col))
    visited[row][col] = True
    houseCnt += 1
    
    while queue:
        coordinate = queue.popleft()
        
        if coordinate[0] < N - 1 and visited[coordinate[0] + 1][coordinate[1]] == False and map[coordinate[0] + 1][coordinate[1]] == '1':
            queue.append((coordinate[0] + 1, coordinate[1]))
            visited[coordinate[0] + 1][coordinate[1]] = True
            houseCnt += 1
        if coordinate[0] > 0 and visited[coordinate[0] - 1][coordinate[1]] == False and map[coordinate[0] - 1][coordinate[1]] == '1':
            queue.append((coordinate[0] - 1, coordinate[1]))
            visited[coordinate[0] - 1][coordinate[1]] = True
            houseCnt += 1
        if coordinate[1] < N - 1 and visited[coordinate[0]][coordinate[1] + 1] == False and map[coordinate[0]][coordinate[1] + 1] == '1':
            queue.append((coordinate[0], coordinate[1] + 1))
            visited[coordinate[0]][coordinate[1] + 1] = True
            houseCnt += 1
        if coordinate[1] > 0 and visited[coordinate[0]][coordinate[1] - 1] == False and map[coordinate[0]][coordinate[1] - 1] == '1':
            queue.append((coordinate[0], coordinate[1] - 1))
            visited[coordinate[0]][coordinate[1] - 1] = True
            houseCnt += 1
    
    return houseCnt

vilCnt = 0
houseCntList = []
for i in range(N):
    for j in range(N):
        if map[i][j] == '1' and visited[i][j] == False:
            houseCnt = BFS(N, i, j)
            houseCntList.append(houseCnt)
            vilCnt += 1
            
houseCntList.sort()

print(vilCnt)
for i in range(vilCnt):
    print(houseCntList[i])