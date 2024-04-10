class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        maxWater = 0
        while l <= r:
            water = (r - l) * min(height[l], height[r])
            if water > maxWater:
                maxWater = water

            cand1 = l + 1
            cand2 = r - 1

            if cand1 > len(height) - 1 and cand2 < 0:
                break
            elif cand1 > len(height) - 1:
                r = cand2
                continue
            elif cand2 < 0:
                l = cand1
                continue

            if height[l] < height[r]:
                l = cand1
            else:
                r = cand2

        return maxWater

            
