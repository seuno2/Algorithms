# https://www.acmicpc.net/problem/23288
# 23288

import sys
from collections import deque

global map
global dx, dy

# 현재의 위치와 방향을 입력받아 다음 주사위 위치를 반환
def moveDice(x, y, direction, diceStatus:list)->tuple:
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    if  (not((0 <= (x+dx[direction]) <= (M-1))) or not(0 <= (y+dy[direction]) <= (N-1))): ## 바뀐 방향이 map을 벗어난다면
        direction = (direction + 2) % 4 # 방향 거꾸로

    if direction==0:
        tmp = diceStatus[1][0]
        diceStatus[1] = diceStatus[1][1:] + [diceStatus[-1][1]]
        diceStatus[-1][1] = tmp
        return (x+1, y, diceStatus, direction)
    elif direction==1:
        tmp = diceStatus[0][1]
        diceStatus[0][1] = diceStatus[1][1]
        diceStatus[1][1] = diceStatus[2][1]
        diceStatus[2][1] = diceStatus[3][1]
        diceStatus[3][1] = tmp
        return (x, y+1, diceStatus, direction)
    elif direction==2:
        tmp = diceStatus[1][-1]
        diceStatus[1] =  [diceStatus[-1][1]] + diceStatus[1][:2]
        diceStatus[-1][1] = tmp
        return (x-1, y, diceStatus, direction)
    else:
        tmp = diceStatus[3][1]
        diceStatus[3][1] = diceStatus[2][1]
        diceStatus[2][1] = diceStatus[1][1]
        diceStatus[1][1] = diceStatus[0][1]
        diceStatus[0][1] = tmp
        return (x, y-1, diceStatus, direction)
    
def getDirection(x, y, direction, diceStatus):
    # print('주사위숫자',diceStatus[1][1],"그전방향",direction)
    if diceStatus[1][1] > map[y][x]:
        direction = (direction+1)%4
        # print('바뀐방향',direction)
    elif diceStatus[1][1] < map[y][x]:
        direction = (direction+3)%4
        # print('바뀐방향',direction)
    else:
        direction = direction
        # print('방향안바뀜',direction)
    
    return direction

def getScore(x:int, y:int)->int:
    def getAvailableSpots(x,y):##너비우선 탐색으로 접근가능한 좌표 반
        q = [[x, y]]
        visited = [[False] * M for _ in range(N)]
        visited[y][x] = True
        # print(q)
        availableSpots = []
        while q:
            V = q.pop()
            availableSpots.append(V)
            # print(V)
            for i in range(4):
                if 0<=(V[0]+dx[i])<=(M-1) and 0<=(V[1]+dy[i])<=(N-1): #위치가 map 안에 있어야 한다
                    if (not visited[V[1]+dy[i]][V[0]+dx[i]]) and (map[V[1]+dy[i]][V[0]+dx[i]] == map[y][x]): #  방문하지 않았고, 현재 숫자와 같아야한다
                        q.append([V[0]+dx[i], V[1]+dy[i]])
                        visited[V[1]+dy[i]][V[0]+dx[i]] = True
    
        return availableSpots
    
    availableSpots = getAvailableSpots(x,y)
    # print(availableSpots, map[y][x])
    return len(availableSpots)*map[y][x]


N, M, K = map(int, sys.stdin.readline().split(' '))
map = [list(map(int,sys.stdin.readline().split(" "))) for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

x,y = 0,0
direction = 0 #0:오른쪽, 1:아래, 2:왼쪽, 3:위
diceStatus =[
    [False, 2, False],
         [4,6,3],
    [False, 5, False],
    [False, 1, False]
]
totalScore = 0


for iter in range(K):
    x, y, diceStatus, direction = moveDice(x, y, direction, diceStatus)
    # print(f'현재 위치:({y+1},{x+1}), 주사위:{diceStatus[1][1]}')
    totalScore += getScore(x,y)
    direction = getDirection(x, y, direction, diceStatus)
    # print(f'다음방향:{direction}')

print(totalScore)




