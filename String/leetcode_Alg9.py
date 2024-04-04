class Solution:
    def isPalindrome(self, x: int) -> bool:
        isNeg = False
        strLen = 0

        if x < 0:
            return False    

        y = x * 1

        while x > 0:
            strLen += 1
            x = x // 10

        m = 1
        stack = []
        for i in range(0, strLen // 2):
            stack.append(y % 10)
            y = y // 10

        if strLen % 2 == 1:
            y = y // 10

        for i in range(0, strLen // 2):
            a = stack.pop()
            if a != y % 10:
                return False
            y = y // 10
        
        return True

