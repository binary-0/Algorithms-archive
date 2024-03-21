arithString = input()

curNumStr = ''
curNum = 0
answer = 0
minusFlag = False

for char in arithString:
    if '0' <= char <= '9': #if char is a number
        curNumStr += char
    elif char == '+':
        curNum = int(curNumStr)
        curNumStr = ''
        
        if minusFlag == False:
            answer += curNum
        else:
            answer -= curNum
    elif char == '-':
        curNum = int(curNumStr)
        curNumStr = ''
        
        if minusFlag == False:
            answer += curNum
        else:
            answer -= curNum
        minusFlag = True
        
    else:
        print('Error')
        
curNum = int(curNumStr)
if minusFlag == False:
    answer += curNum
else:
    answer -= curNum
    
print(answer)