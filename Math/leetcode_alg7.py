class Solution:
    def reverse(self, x: int) -> int:
        reversedList = list()

        isNeg = False
        isFirstZero = True

        if x < 0:
            isNeg = True
            x = -x

        calcX = x * 1
        while calcX > 0:
            target = calcX % 10
            
            if target != 0 or isFirstZero == False:
                reversedList.append(calcX % 10)
                isFirstZero = False

            calcX = calcX // 10

        ans = 0
        for i in range(0, len(reversedList)):
            ans += reversedList[i]*10**(len(reversedList) - i - 1)
        
        if isNeg == True:
            ans = -ans

        if not -2**31 <= ans <= 2**31 - 1:
            return 0
            
        return ans

        


        
