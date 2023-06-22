# 1966
# https://www.acmicpc.net/problem/1966

import sys

caseNum = int(input())
answer = []

for _ in range(caseNum):
    N, M = map(int, sys.stdin.readline().split())
    importanceQue = list(map(int, sys.stdin.readline().split()))
    
    targetDoc = importanceQue[M]
    cnt = 0

    while(True):
        if M == 0:
            if targetDoc == max(importanceQue):
                cnt += 1
                answer.append(cnt)
                break
            else:
                importanceQue.append(importanceQue.pop(0))
                M = len(importanceQue) - 1
        
        else :
            if importanceQue[0] == max(importanceQue) :
                importanceQue.pop(0)
                M -= 1
                cnt += 1
            
            else:
                importanceQue.append(importanceQue.pop(0))
                M -= 1

for i in answer:
    print(i)
