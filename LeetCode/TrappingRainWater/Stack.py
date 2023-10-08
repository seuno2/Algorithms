# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            # 직전보다 벽이 높아지는 경우
            while stack and height[i] > height[stack[-1]]:
                # 직전의 높이를 offset으로 설정(나중에 물의 높이에서 빼기위해)
                offset = height[stack.pop()]

                if not len(stack):
                    break
                
                distance = i - stack[-1] - 1
                # 현재의 벽높이와 stack 직전 벽높이 중 낮은값까지 물이 차있음
                waterHeight = min(height[i], height[stack[-1]]) - offset

                volume += distance * waterHeight
                # print('+', distance * waterHeight)

            stack.append(i)
        return volume
