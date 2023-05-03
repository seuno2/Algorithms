#1927
#https://www.acmicpc.net/problem/1927

import heapq, sys

input = sys.stdin.readline
n = int(input())
q = []

for _ in range(n):
    x = int(input())
    if x:
        heapq.heappush(q, x)
    else:
        if not q: print(0)
        else:
            print(heapq.heappop(q))
