class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictH = {}

        for i in range(0, len(nums)):
            required = target - nums[i]
            if dictH.get(required) != None:
                return [dictH[required], i]
            
            dictH[nums[i]] = i
