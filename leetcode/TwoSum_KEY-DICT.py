#https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {key:val for key,val in zip(nums, range(len(nums)))}
        
        
        for i, n in enumerate(nums):
            if target - n in nums_map and i!=nums_map[target - n]:
                return [i, nums_map[target - n]]
