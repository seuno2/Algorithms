# 20057
# https://www.acmicpc.net/problem/20057

import sys

# 모래변화 업데이트
def getSandMovement(arr:list, direction:int, x:int,y:int)->list:
    direction = direction
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]    
    x,y = x + dx[direction], y + dy[direction]
    
    gain = [0.01, 0.02, 0.07, 0.1, 0.05, 0.1, 0.02, 0.07, 0.01]

    # 네가지 방향별로 상대위치
    bias_x = [
        [1,0,0,-1,-2,-1,0,0,1],
        [-1,-2,-1,-1,0,1,2,1,1],
        [-1,0,0,1,2,1,0,0,-1],
        [1,2,1,1,0,-1,-2,-1,-1]
        ]
    
    bias_y = [
        [-1,-2,-1,-1,0,1,2,1,1],
        [-1,0,0,1,2,1,0,0,-1],
        [1,2,1,1,0,-1,-2,-1,-1],
        [1,0,0,-1,-2,-1,0,0,1]
        ]

    remainder = 0
    
    for i in range(9):
        tmp = arr[y][x]*gain[i]
        remainder += (tmp - int(tmp))
        arr[y + bias_y[direction][i]][x + bias_x[direction][i]] += int(tmp)
    
    arr[y + dy[direction]][x + dx[direction]] += (arr[y][x]*0.55 + remainder)
    arr[y][x] = 0
    return arr

# 방향 업데이트
def getDirection(visited:list, x:int, y:int, direction:int)->int:
    if direction==0:
        return 1 if not visited[y+1][x] else 0
    elif direction==1:
        return 2 if not visited[y][x+1] else 1
    elif direction==2:
        return 3 if not visited[y-1][x] else 2         
    elif direction==3:
        return 0 if not visited[y][x-1] else 3

N = int(input())

# 격자입력
# 좌우로 +2씩 마진
A = []
for _ in range(N):
    A.append([0, 0] + list(map(int, sys.stdin.readline().split(' '))) + [0, 0]) 

# 모래 총량 구하기
sandTotal = 0
for row in A:
    for i in row:
        sandTotal += i

# 위아래 +2 마진 격자 생성
arr = [[0]*(N+4),[0]*(N+4)] + A + [[0]*(N+4),[0]*(N+4)]

# 방문한곳 표시
visited = [[False]*(N+4) for _ in range(N+4)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
# 현재 위치,방향
x,y = (N+4)//2, (N+4)//2
direction = 0

while True:
    arr = getSandMovement(arr, direction, x, y)
    visited[y][x] = True
    x += dx[direction]
    y += dy[direction]
    direction = getDirection(visited, x, y, direction)
    
    # for row in arr:
    #     print(row)
    # print(' ')

    # for row in visited:
    #     print(row)
    # print(' ')

    if visited[2][3]:    
        break

sandInside = 0

for i in range(2, N + 2):
    for j in range(2, N + 2):
        sandInside += arr[i][j]

sandOutside = sandTotal - sandInside
print(sandOutside)
