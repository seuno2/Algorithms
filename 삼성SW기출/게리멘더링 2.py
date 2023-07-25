# 17779
# https://www.acmicpc.net/problem/17779

import sys
# r행 c열 arr[r][c] (r,c)
N = int(input())
population = [[0]*(N + 1)] + [[0] + list(map(int,sys.stdin.readline().split(' '))) for _ in range(N)]


def getDivision(x,y,d1,d2):
    board = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1,N + 1):
        for j in range(1, N + 1):
            if  (x <= i <= x + d1 and y - d1 <= j <= y and i + j == x + y) or \
                (x <= i <= x + d2 and y <= j <= y + d2 and i - j == x - y) or \
                (x + d1 <= i <= x + d1 + d2 and y - d1 <= j <= y - d1 + d2 and i - j == x - y + 2*d1) or \
                (x + d2 <= i <= x + d1 + d2 and y + d2 - d1 <= j <= y +d2 and i + j == x + y + 2*d2):
                board[i][j] = 5

    boundary = []
    for i in range(1,N+1):
        if board[i].count(5)==2:
            boundary.append(i)

    for i in boundary:
        flag = False
        for j in range(1, N + 1):
            if board[i][j] == 5 and flag == False:
                flag = True
                continue
            if board[i][j]==0 and flag == True:
                board[i][j] = 5
                continue
            if board[i][j] == 5 and flag == True:
                flag = False
            
    for i in range(1, x+d1):
        for j in range(1, y+1):
            if board[i][j] != 5:
                board[i][j] = 1 
    for i in range(1, x+d2+1):
        for j in range(y+1, N+1):
            if board[i][j] != 5:
                board[i][j] = 2      
    for i in range(x+d1, N+1):
        for j in range(1, y-d1+d2+1):
            if board[i][j] != 5:
                board[i][j] = 3   
    for i in range(x+d2+1, N+1):
        for j in range(y-d1+d2, N+1):
            if board[i][j] != 5:
                board[i][j] = 4   
    return board

# board = getDivision(3,5,2,1)
# for row in board:print(row)

answer = 1000000
for x in range(1, N-1):
    for y in range(2, N):
        for d1 in range(1, min(N - x, y) + 1):
            for d2 in range(1, min(N -x - d1, N - y + d1) + 1):
                board = getDivision(x,y,d1,d2)
                # print(x,y,d1,d2)
                
                # if x==3 and y==5 and d1==2 and d2==1:
                #     for row in board : print(row) 

                voter = [0, 0, 0, 0, 0, 0]
            # for num in range(1,6):    
                for i in range(N+1):
                    for j in range(N+1):
                        if board[i][j]==1:
                            voter[1] += population[i][j]
                        elif board[i][j] ==2:
                            voter[2] += population[i][j]
                        elif board[i][j] ==3:
                            voter[3] += population[i][j]
                        elif board[i][j] ==4:
                            voter[4] += population[i][j]
                        elif board[i][j] ==5:
                            voter[5] += population[i][j]

                # if x==3 and y==5 and d1==2 and d2==2:
                #     for row in board : print(row)                            

                if (max(voter) - min(voter[1:])) < answer:
                    answer = max(voter) - min(voter[1:])
                    # print(f'x={x},y={y},d1={d1},d2={d2}') 
                    # for row in board:print(row) 
                    # print(voter)
                    # print(f'answer:{answer}')
                          
                                
print(answer)

