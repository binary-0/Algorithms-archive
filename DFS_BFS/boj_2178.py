from collections import deque
import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
maze = [[0 for _ in range(M)] for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    row = input()
    for j in range(M):
        maze[i][j] = int(row[j])
        
def BFS(N, M, n, m):
    queue = deque()
    
    queue.append((n, m))
    visited[n][m] = 1
    
    while queue:
        coordinate = queue.popleft()
        
        if coordinate[0] < N - 1 and visited[coordinate[0] + 1][coordinate[1]] == 0 and maze[coordinate[0] + 1][coordinate[1]] == 1:
            queue.append((coordinate[0] + 1, coordinate[1]))
            visited[coordinate[0] + 1][coordinate[1]] = visited[coordinate[0]][coordinate[1]] + 1
        if coordinate[0] > 0 and visited[coordinate[0] - 1][coordinate[1]] == 0 and maze[coordinate[0] - 1][coordinate[1]] == 1:
            queue.append((coordinate[0] - 1, coordinate[1]))
            visited[coordinate[0] - 1][coordinate[1]] = visited[coordinate[0]][coordinate[1]] + 1
        if coordinate[1] < M - 1 and visited[coordinate[0]][coordinate[1] + 1] == 0 and maze[coordinate[0]][coordinate[1] + 1] == 1:
            queue.append((coordinate[0], coordinate[1] + 1))
            visited[coordinate[0]][coordinate[1] + 1] = visited[coordinate[0]][coordinate[1]] + 1
        if coordinate[1] > 0 and visited[coordinate[0]][coordinate[1] - 1] == 0 and maze[coordinate[0]][coordinate[1] - 1] == 1:
            queue.append((coordinate[0], coordinate[1] - 1))
            visited[coordinate[0]][coordinate[1] - 1] = visited[coordinate[0]][coordinate[1]] + 1
            
    return visited[N - 1][M - 1]

print(BFS(N, M, 0, 0))
