class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        maxStr = ""

        for i in range(0, len(s)):
            for j in range(i, len(s)):
                subStr = s[i:j + 1]

                if subStr == subStr[::-1] and maxLen < len(subStr):
                    maxLen = len(subStr)
                    maxStr = subStr
        
        return maxStr
