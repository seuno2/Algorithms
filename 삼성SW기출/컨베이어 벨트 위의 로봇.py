# 20055
# https://www.acmicpc.net/problem/20055

import sys
def rotate():
    global belt, robots
    belt = [0] + [belt[2*N]] + belt[1:2*N]
    robots = [0, 0] + robots[1:N]
    if robots[N]==1:
        robots[N] = 0

def moveRobot():
    global belt, robots
    def movable(idx):
        if robots[idx+1]!=True and belt[idx+1]>=1:
            return True
        else:
            return False
        
    for idx in range(N-1,0,-1):
        if robots[idx]==1:
            if movable(idx):
                robots[idx+1] = 1
                robots[idx] = 0
                belt[idx+1] -= 1

    if robots[N]==1:
        robots[N] = 0


def loadRobot():
    global belt, robots
    if belt[1]!=0:
        robots[1] = 1
        belt[1] -= 1

def checkDurability():
    if belt.count(0)>=K+1:
        return False
    else:
        return True
    
N, K = map(int, sys.stdin.readline().split(' '))
belt = [0] + list(map(int, sys.stdin.readline().split(' ')))
robots = [0]*(N+1)
answer = 1

while True:
    rotate()
    # print(' ')
    # print('ROTATE')
    # print(belt)
    # print(robots)

    moveRobot()
    # print('MOVE ROBOT')
    # print(belt)
    # print(robots)

    loadRobot()
    # print('LOAD ROBOT')
    # print(belt)
    # print(robots)

    if not checkDurability():
        # print('--END--')
        print(answer)
        break
    else:
        answer += 1
