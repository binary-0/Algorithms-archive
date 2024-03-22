from collections import deque

numNode, numEdge, startPoint = list(map(int, input().split()))

graph = [[] for _ in range(numNode + 1)]
visited = [0 for _ in range(numNode + 1)]
counter = 0

for i in range(numEdge):
    src, dst = list(map(int, input().split()))
    
    graph[src].append(dst)
    graph[dst].append(src)
    
for i in range(1, numNode + 1):
    graph[i].sort()
    
def bfs(st):
    global counter
    
    queue = deque()
    queue.append(graph[st])
    counter += 1
    visited[st] = counter
    
    while queue:
        nextNode = queue.popleft()
        
        for adj in nextNode:
            if visited[adj] == 0:
                queue.append(graph[adj])
                counter += 1
                visited[adj] = counter
                
bfs(startPoint)

for i in range(1, numNode + 1):
    print(visited[i])