class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        
        minLen = len(strs[0])
        for word in strs:
            if minLen > len(word):
                minLen = len(word)

        for idx in range(0, minLen):
            target = strs[0][idx]
            flag = False
            for word in strs:
                if word[idx] != target:
                    flag = True
            
            if flag == False:
                answer += target
            else:
                break

        return answer