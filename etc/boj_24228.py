def CalcR(N, R):
    return N + 2*(R - 1) + 1

N, R = map(int, input().split())
retVal = CalcR(N, R)
print(retVal)