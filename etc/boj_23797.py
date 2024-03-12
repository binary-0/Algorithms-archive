S = input()

kUnsolved = 0
pUnsolved = 0
maxUnsolved = 0

for ch in S:
    if ch == 'K':
        if pUnsolved >= 1:
            pUnsolved -= 1
            kUnsolved += 1
        else:
            kUnsolved += 1
            if maxUnsolved < kUnsolved:
                maxUnsolved = kUnsolved
    else:   #P detected
        if kUnsolved >= 1:
            kUnsolved -= 1
            pUnsolved += 1
        else:
            pUnsolved += 1
            if maxUnsolved < pUnsolved:
                maxUnsolved = pUnsolved
                
print(maxUnsolved)