class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        history = {}

        for i in range(0, len(nums)):
            required = target - nums[i]
            if history.get(required) != None:
                return [history[required], i]
            
            history[nums[i]] = i
