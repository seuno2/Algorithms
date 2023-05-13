#1259
#https://www.acmicpc.net/problem/1259

import sys

nums = []

while True:
    nums.append(str(sys.stdin.readline().strip()))
    if nums[-1] == '0':break

for num in nums[:-1]:
    if num[::-1]==num:
        print('yes')
    else : print('no')
