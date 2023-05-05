#3190
#https://www.acmicpc.net/problem/3190

from collections import deque

N = int(input())
graph = [[0] * (N + 1) for  _ in range(N + 1)]
apples = int(input())

for _ in range(apples):
    x,y = map(int,input().split())
    graph[x][y] = 1

# for col in graph: print(col)

L = int(input())
snake = deque()
snake.append([1,1])
dirDict = dict()

for _ in range(L):
    x, c = input().split()
    dirDict[int(x)] = c

cnt = 0
x,y = 0,1
dx = [-1,0,1,0]
dy = [0,-1,0,1]
direction = 2


while True:
    x,y = x + dx[direction], y + dy[direction]

    if 1 <= x <= N and 1 <= y <= N and graph[y][x] != 2:
        if graph[y][x] != 1:
            temp_x, temp_y = snake.popleft()
            graph[temp_y][temp_x] = 0
        graph[y][x] = 2
        snake.append([x,y])

        if cnt in dirDict.keys():
            if dirDict[cnt] == 'D':
                direction = (direction + 1) % 4
            elif dirDict[cnt] == 'L':
                direction = (direction - 1) % 4

        cnt += 1
        # print(snake)
        # for col in graph: print(col)
        # print()

    else:
        print(cnt)
        break
