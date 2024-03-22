from collections import deque

numPC = int(input())
numEdge = int(input())

graph = [[] for _ in range(numPC + 1)]
visited = [False for _ in range(numPC + 1)]

for i in range(numEdge):
    src, dest = list(map(int, input().split()))
    
    graph[src].append(dest)
    graph[dest].append(src)
    
def BFS():
    queue = deque()
    queue.append(graph[1])
    visited[1] = True
    
    while queue:
        nextPC = queue.popleft()
        
        for adj in nextPC:
            if visited[adj] == False:
                queue.append(graph[adj])
                visited[adj] = True
                
BFS()

counter = 0
for i in range(2, numPC + 1):
    if visited[i] == True:
        counter += 1
        
print(counter)