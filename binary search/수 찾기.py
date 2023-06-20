# 1920
# https://www.acmicpc.net/problem/1920

import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

A.sort()

def binarySearch(num, arr):
    start = 0
    end = N - 1
    while(start <= end):
        mid = (start + end) // 2
        if arr[mid] == num:
            return 1
        elif arr[mid] < num:
            start = mid + 1
        else :
            end = mid -1
    return 0

for num in B:
    print(binarySearch(num, A))
