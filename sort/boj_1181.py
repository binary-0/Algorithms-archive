N = int(input())

lst = list()
for i in range(N):
    lst.append(input())
    
setList = set(lst)
lst = list(setList)

lst.sort()
lst.sort(key=lambda x: len(x))

for i in range(len(lst)):
    print(lst[i])