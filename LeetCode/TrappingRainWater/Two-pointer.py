#https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)

            # 왜 left, right 두 포인터를 두는지 이해가 안갔다(한쪽끝에서만 원 포인터로만 volume을 채워나갈 수 있다고 생각함)

            # left, right 두 포인터 사이에 벽이 얼마나 높은지, 몇개가 있는지는 영향을 끼치지 않음
            # left_max, right_max 중 낮을곳을 기준으로 빗물이 채워지기 때문
            # left, right 사이에 벽이 높든지 낮든지, 벽의 수와 무관하게 어떤 경우라도 양쪽 max값 중의 낮은곳을 기준으로 빗물은 채워진다!
            
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume
