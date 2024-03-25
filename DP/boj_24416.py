globalExecCnt = 0

def fib(num):
    global globalExecCnt
    if num == 1 or num == 2:
        globalExecCnt += 1
        return 1
    else:
        return fib(num - 1) + fib(num - 2)

def fib_dp(num):
    dp = [0 for _ in range(num + 1)]
    
    dp[1] = 1
    dp[2] = 1
    
    execCnt = 0
    for i in range(3, num + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        execCnt += 1
        
    return execCnt

num = int(input())

fib(num)
dpfibCnt= fib_dp(num)

print(f'{globalExecCnt} {dpfibCnt}')