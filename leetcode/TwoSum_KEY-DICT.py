#https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {key:val for key,val in zip(nums, range(len(nums)))}
        
        # 딕셔너리는 해시맵으로 탐색 시간복잡도 : O(1)
        # 전체 시간복잡도 : O(n)
        for i, n in enumerate(nums):
            if target - n in nums_map and i!=nums_map[target - n]:
                return [i, nums_map[target - n]]
