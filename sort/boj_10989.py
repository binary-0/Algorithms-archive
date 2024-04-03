N = int(input())

lst = [0 for _ in range(10001)]
for i in range(N):
    lst[int(input())] += 1

for i in range(1, 10001):
    if lst[i] != 0:
        for j in range(lst[i]):
            print(i)