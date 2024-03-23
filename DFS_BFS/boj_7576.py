from collections import deque

M, N = list(map(int, input().split()))
box = [[-1 for _ in range(M)] for _ in range(N)]
visited = [[-1 for _ in range(M)] for _ in range(N)]

dn = [0, 0, 1, -1]
dm = [1, -1, 0, 0]
stList = []

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        box[i][j] = row[j]
        
        if row[j] == 1:
            stList.append((i, j))
        
def BFS(N, M, stList):
    queue = deque()
    maxVisited = 0
    
    for i in range(len(stList)):
        queue.append((stList[i][0], stList[i][1]))
        visited[stList[i][0]][stList[i][1]] = 0
        
    while queue:
        cn, cm = queue.popleft()
        
        for i in range(4):
            nn = cn + dn[i]
            nm = cm + dm[i]
            
            if 0 <= nn <= N - 1 and 0 <= nm <= M - 1 and box[nn][nm] == 0 and visited[nn][nm] == -1:
                queue.append((nn, nm))
                visited[nn][nm] = visited[cn][cm] + 1
                if visited[nn][nm] > maxVisited:
                    maxVisited = visited[nn][nm]
                    
    return maxVisited

res = BFS(N, M, stList)

flag = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == 0 and visited[i][j] == -1:
            flag = 1
            
if flag == 1:
    print(-1)
else:
    print(res)