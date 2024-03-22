from collections import deque

numNode, numEdge, startPoint = list(map(int, input().split()))

graph = [[] for _ in range(numNode + 1)]
visited = [False for _ in range(numNode + 1)]

for i in range(numEdge):
    src, dst = list(map(int, input().split()))
    graph[src].append(dst)
    graph[dst].append(src)

for lst in graph:
    lst.sort()
    
def BFS(sp):
    queue = deque()
    queue.append(graph[sp])
    visited[sp] = True
    print(sp, end=" ")
    
    while queue:
        nextNode = queue.popleft()
        
        for adj in nextNode:
            if visited[adj] == False:
                queue.append(graph[adj])
                visited[adj] = True
                print(adj, end=" ")
    print()

def DFS(sp):
    visited[sp] = True
    print(sp, end=" ")
    
    for adj in graph[sp]:
        if visited[adj] == False:
            DFS(adj)

DFS(startPoint)
print()
for i in range(1, numNode + 1):
    visited[i] = False
BFS(startPoint)