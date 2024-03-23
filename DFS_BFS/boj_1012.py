from collections import deque

numTestCase = int(input())
for _ in range(numTestCase):
    M, N, K = list(map(int, input().split()))
    bmap = [['0' for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]

    for i in range(K):
        m, n = list(map(int, input().split()))
        bmap[n][m] = '1'
            
    def BFS(N, M, row, col):
        queue = deque()
        bugCnt = 0
        
        queue.append((row, col))
        visited[row][col] = True
        bugCnt += 1
        
        while queue:
            coordinate = queue.popleft()
            
            if coordinate[0] < N - 1 and visited[coordinate[0] + 1][coordinate[1]] == False and bmap[coordinate[0] + 1][coordinate[1]] == '1':
                queue.append((coordinate[0] + 1, coordinate[1]))
                visited[coordinate[0] + 1][coordinate[1]] = True
                bugCnt += 1
            if coordinate[0] > 0 and visited[coordinate[0] - 1][coordinate[1]] == False and bmap[coordinate[0] - 1][coordinate[1]] == '1':
                queue.append((coordinate[0] - 1, coordinate[1]))
                visited[coordinate[0] - 1][coordinate[1]] = True
                bugCnt += 1
            if coordinate[1] < M - 1 and visited[coordinate[0]][coordinate[1] + 1] == False and bmap[coordinate[0]][coordinate[1] + 1] == '1':
                queue.append((coordinate[0], coordinate[1] + 1))
                visited[coordinate[0]][coordinate[1] + 1] = True
                bugCnt += 1
            if coordinate[1] > 0 and visited[coordinate[0]][coordinate[1] - 1] == False and bmap[coordinate[0]][coordinate[1] - 1] == '1':
                queue.append((coordinate[0], coordinate[1] - 1))
                visited[coordinate[0]][coordinate[1] - 1] = True
                bugCnt += 1
        
        return bugCnt

    rBugCnt = 0
    for i in range(N):
        for j in range(M):
            if bmap[i][j] == '1' and visited[i][j] == False:
                bugCnt = BFS(N, M, i, j)
                rBugCnt += 1
    print(rBugCnt)
    