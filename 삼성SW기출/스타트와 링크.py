# 14889
# https://www.acmicpc.net/problem/14889
import sys
def combination(arr, r):
    arr = sorted(arr)
    result = []
 
    def generate(buf, idx):
        if len(buf) == r:
            result.append(list(buf))
            return
 
        for i in range(idx, len(arr)):
            buf.append(arr[i])
            generate(buf, i + 1)
            buf.pop()
    generate([], 0)
    return result
N = int(input())
abilities = [[0]*(N+1)] + [[0] + list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]
combinations = combination([i for i in range(1,N+1)],N//2)
answer = 10000000
for combination in combinations:
    team1 = combination
    team2 = [i for i in range(1,N+1) if i not in team1]
    s1,s2 = 0,0
    for i in team1:
        for j in [num for num in team1 if num!=i]:
            s1+=abilities[i][j]
    for i in team2:
        for j in [num for num in team2 if num!=i]:
            s2+=abilities[i][j]
    if abs(s1-s2)<answer:
        answer = abs(s1-s2)
print(answer)
