#1874 
#https://www.acmicpc.net/problem/1874

import sys

n = int(sys.stdin.readline())
stack = []
answer = []
flag = 0
cur = 1


for i in range(n):
    num = int(sys.stdin.readline())
    while cur <= num:
        stack.append(cur)
        answer.append("+")
        cur += 1
    
    if stack[-1] == num:
        answer.append("-")
        stack.pop()

    else :
        print("NO")
        flag = 1
        break

if flag == 0:
    for i in answer:
        print(i)
