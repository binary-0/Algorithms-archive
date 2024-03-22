import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

numNode, numEdge, startPoint = list(map(int, input().split()))

graph = [[] for i in range(numNode + 1)]
visited = [0 for i in range(numNode + 1)]
counter = 0

for i in range(numEdge):
    start, end = list(map(int, input().split()))
    
    graph[start].append(end)
    graph[end].append(start)
    
for adjList in graph:
    adjList.sort(reverse=True)

def dfs(start):
    global counter
    counter += 1
    visited[start] = counter
    
    for adj in graph[start]:
        if visited[adj] == 0:
            dfs(adj)

dfs(startPoint)
            
for i in range(len(visited)):
    if i > 0:
        print(visited[i])