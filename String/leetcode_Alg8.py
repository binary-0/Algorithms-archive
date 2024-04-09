class Solution:
    def myAtoi(self, s: str) -> int:
        numList = []
        isIntro = True
        isSign = True
        isNeg = False

        for ch in s:
            if isIntro == True and ch == ' ':
                continue
            
            isIntro = False
            if ord('0') > ord(ch) or ord('9') < ord(ch):
                if isSign == True and (ch == '-' or ch == '+'):
                    isSign = False
                    if ch == '-':
                        isNeg = True
                    continue
                else:
                    break
            else:
                isSign = False
                numList.append(ch)  

        answer = 0
        for i in range(0, len(numList)):
            answer += (ord(numList[i]) - ord('0')) * (10 ** (len(numList) - 1 - i))

        if isNeg == True:
            answer *= -1

        if answer < -2**31:
            answer = -2**31
        elif answer > 2**31 - 1:
            answer = 2**31 - 1

        return answer
