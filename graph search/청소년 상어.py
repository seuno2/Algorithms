# 19236
# https://www.acmicpc.net/problem/19236


import sys
import copy
global DX, DY, SCORES

def dfs(sx, sy, score, arr):
    def moveFish(sx,sy, arr:list):
        def movable(i, j)->bool:
            nextX = j + DX[arr[i][j][1]]
            nextY = i + DY[arr[i][j][1]]
            if (0<= nextX <= 3) and  (0<= nextY <= 3) and ([nextX, nextY] != [sx, sy] or arr[nextY][nextX]==None ) : 
                return True  ##이동할 칸이 격자 안에있고, 상어가 없거나 또는 빈칸일 경우 True 반환
            else:
                return False

        def findFish(fishNum):
            for i in range(4):
                for j in range(4):
                    if arr[i][j] != None:
                        if arr[i][j][0]==fishNum:
                            return i,j
            return False

        for fishNum in range(1,17):
            if not findFish(fishNum):
                continue
            else:
                i, j = findFish(fishNum)
            for _ in range(8):
                if movable(i, j):
                    nextX = j + DX[arr[i][j][1]]
                    nextY = i + DY[arr[i][j][1]]
                    if arr[nextY][nextX]==None: ##빈칸일 경우 None
                        arr[nextY][nextX] = arr[i][j]
                        arr[i][j] = None
                    else:
                        tmp = arr[nextY][nextX] ## 빈칸이 아닐 경우 위치 교환
                        arr[nextY][nextX] = arr[i][j]
                        arr[i][j] = tmp
                    break
                else:
                    arr[i][j][1] = (arr[i][j][1] + 1) if arr[i][j][1] !=8 else 1
        return arr

    def sharkMovableLocation(sx, sy, arr)->list:
        locations = []
        for i in range(1,4):
            tmpY = sy + DY[arr[sy][sx][1]]*i
            tmpX = sx + DX[arr[sy][sx][1]]*i
            if 0<=tmpX<=3 and 0<=tmpY<=3 and arr[tmpY][tmpX]!=None:
                locations.append([tmpX,tmpY])
        if locations == []:
            return False
        else:
            return locations
    
    score += arr[sy][sx][0]
    arr[sy][sx] = ['*', arr[sy][sx][1]]
    # print('after shark move')
    # for row in arr: print(row)
    # print(' ')
    arr = moveFish(sx, sy, arr)

    # print('after fish move')
    # for row in arr: print(row)
    locations = sharkMovableLocation(sx, sy, arr)    
    
    if not locations:
        SCORES.append(score)
        # print('go back!!')
    else:
        # print(locations)
        for loc in locations:
            # print(loc, sx, sy)
            # for row in arr : print(row)   
            arr[sy][sx] = None
            dfs(copy.deepcopy(loc[0]), copy.deepcopy(loc[1]), score, copy.deepcopy(arr))

DX = [None, 0, -1, -1, -1, 0, 1, 1, 1] #1부터 북쪽방향에서 45도씩 시계 반대방향으로 8까지
DY = [None, -1, -1, 0, 1, 1, 1, 0, -1]
SCORES = []

arr = []

for _ in range(4):
    line = list(map(int, sys.stdin.readline().split(' ')))
    row = []
    for i in range(0,8,2):
        row.append(line[i:i+2])
    arr.append(row)

sx, sy = 0, 0

dfs(sx, sy, 0, arr)
answer = max(SCORES)
print(answer)
