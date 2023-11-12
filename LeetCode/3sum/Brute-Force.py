#https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        # 중복이 생기는 경우는 건너뛴다
        # i 는 0보다 클 때,
        # j,k 는 각각 i,j 보다 2이상 큰 경우를 비교

        for i in range(len(nums) - 2):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums) - 1):
                if j > i + 1 and nums[j]==nums[j-1]:
                    continue
                for k in range(j+1,len(nums)):
                    if k > j + 1 and nums[k]==nums[k-1]:
                        continue

                    if nums[i] + nums[j] + nums[k] == 0:
                        results.append([nums[i],nums[j],nums[k]])

        return results
