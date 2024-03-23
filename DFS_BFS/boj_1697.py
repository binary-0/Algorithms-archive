from collections import deque

MAX = 100001
Subin, Ototo = list(map(int, input().split()))
visited = [-1 for _ in range(MAX)]

def BFS(Subin, Ototo):
    queue = deque()
    
    curPos = Subin
    queue.append(curPos)
    visited[curPos] = 0
    
    while queue:
        curPos = queue.popleft()
        if curPos == Ototo:
            return visited[curPos]
        
        if curPos > 0 and visited[curPos - 1] == -1:
            nextPos = curPos - 1
            queue.append(nextPos)
            visited[nextPos] = visited[curPos] + 1
        if curPos < MAX - 1 and visited[curPos + 1] == -1:
            nextPos = curPos + 1
            queue.append(nextPos)
            visited[nextPos] = visited[curPos] + 1
        if curPos * 2 <= MAX - 1 and visited[curPos * 2] == -1:
            nextPos = curPos * 2
            queue.append(nextPos)
            visited[nextPos] = visited[curPos] + 1
            
            
print(BFS(Subin, Ototo))