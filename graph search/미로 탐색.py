#2178
#https://www.acmicpc.net/problem/2178

from collections import deque

N, M = map(int, input().split())
graph = []


for i in range(N):
    graph.append(list(map(int,input())))

# for col in graph: print(col)

def bfs(x,y):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    que = deque()
    que.append((x,y))

    while que:
        x,y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M or graph[nx][ny]==0 :
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                que.append((nx,ny))

        # for col in graph: print(col)
        # print(que)
        # print()

bfs(0,0)

print(graph[N-1][M-1])
