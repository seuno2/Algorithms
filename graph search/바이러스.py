#2606
#https://www.acmicpc.net/problem/2606

from collections import deque

N = int(input())
M = int(input())

graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited = [1]

# for col in graph: print(col)

def bfs(v):
    que = deque([v])

    while que:
        v = que.popleft()
        for i in range(1,N+1):
            if i not in visited and graph[i][v]:
                que.append(i)
                visited.append(i)
        # print(que)

bfs(1)
print(len(visited)-1)
