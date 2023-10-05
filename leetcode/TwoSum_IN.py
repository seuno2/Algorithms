#https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            complement = target - num

            # i+1번째 이후의 요소들에서 검색(중복 피하기 위햬)
            # in을 통한 탐색의 시간복잡도:O(n)
            # 부루트 포스 탐색처럼 매번 비교하는 것보다 in 사용이 훨씬 빠르게 실행된다
            if complement in nums[i+1:]:
                return [i, nums[i+1:].index(complement) + (i+1)]
