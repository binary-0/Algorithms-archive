from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hasher = defaultdict(int)
        curLen = 0
        maxLen = 0

        for i in range(0, len(s)):
            curLen = 0
            hasher = defaultdict(int)

            for j in range(i, len(s)):
                if s[j] not in hasher:
                    hasher[s[j]] = j
                    curLen += 1
                else:
                    if maxLen < curLen:
                        maxLen = curLen
                    i = hasher[s[j]]
                    break

            if maxLen < curLen:
                maxLen = curLen

        return maxLen
