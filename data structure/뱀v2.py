#3190
#https://www.acmicpc.net/problem/3190

import sys
from collections import deque

#보드의 크기
N = int(input())
#사과 개수
K = int(input()) 

graph = [[0] * (N + 1) for _ in range(N + 1)]

#사과의 위치(행,열)
for _ in range(K): 
    y,x = map(int, sys.stdin.readline().split())
    graph[y][x] = 1

#움직임 횟수
L = int(input()) 

# 움직임 정보(sec초 후, 왼/오)
movements = deque()
for _ in range(L):
    sec, d = input().split()
    movements.append([int(sec),d])

snake = deque()
snake.append([1,1])

dx = [-1,0,1,0]
dy = [0,-1,0,1]
direction = 2
cnt = 0
x,y = 1,1
# for i in graph:print(i)
# print(snake)
while True:
    x, y = x + dx[direction], y + dy[direction]
    cnt += 1

    if 1 <= x <= N and 1 <= y <= N and [x,y] not in snake:
        snake.append([x,y])
        if graph[y][x]==0:
            snake.popleft()
        elif graph[y][x]==1:
            graph[y][x]=0
        # print(snake)
        
        # print(cnt, direction)
        if len(movements)!=0:
            if cnt==movements[0][0]:
                if movements[0][1]=="L":
                    direction = (direction + 3) % 4
                    # print('changed(L)', direction)
                elif movements[0][1]=="D":
                    direction = (direction + 1) % 4
                    # print('changed(R)', direction)
                movements.popleft()

    else:
        # print('stop!', [x,y] in snake)
        print(cnt)
        break


