def FoldAndFlip(k):
    if k == 0:
        return 0
    elif k == 1:
        return 1
    elif k % 2 == 1:
        return 1 - FoldAndFlip(k//2)
    else:
        return FoldAndFlip(k//2)

k = int(input())
isFlipped = FoldAndFlip(k - 1)

print(isFlipped)