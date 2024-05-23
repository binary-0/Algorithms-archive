h, m = list(map(int, input().split()))
add = int(input())

m += add

while m >= 60:
    m -= 60
    h += 1

if h >= 24:
    h -= 24

print(f'{h} {m}')