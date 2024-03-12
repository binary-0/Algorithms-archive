def increArray(N, M, K):
    #K >= N + M - 1
    
    if K < N + M - 1:
        print('NO')
    else:
        print('YES')
        for i in range(0, N):
            for j in range(1, M + 1):
                if j == M:
                    print(f'{j + i}', end="")
                else:
                    print(f'{j + i}', end=" ")
            print()

N, M, K = map(int, input().split())
increArray(N, M, K)