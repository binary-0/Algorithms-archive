class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
            
        lvStore = [[] for _ in range(numRows)]

        row = 0
        isDec = True

        for ch in s:
            lvStore[row].append(ch)

            if isDec == True and row == numRows - 1:
                isDec = False
            elif isDec == False and row == 0:
                isDec = True

            if isDec == True:
                row += 1
            else:
                row -= 1

        output = ""
        for row in lvStore:
            for e in row:
                output += e
        
        return output



