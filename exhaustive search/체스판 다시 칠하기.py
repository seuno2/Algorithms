#1018
#https://www.acmicpc.net/problem/1018

import sys

row, col = map(int,sys.stdin.readline().split())
whole_plate = []
for _ in range(row):
    whole_plate.append(str(sys.stdin.readline().strip()))

answer = 32

def get_revision_times(a,b):
    temp_plate = []
    for r in range(a,a+8):
        temp_plate.append(whole_plate[r][b:b+8])
    cnt1, cnt2 = 0, 0

    for row_num in range(8):
        for col_num in range(8):
            if ((row_num + col_num)%2 == 1) and (temp_plate[row_num][col_num] == 'W') or ((row_num + col_num)%2 == 0) and (temp_plate[row_num][col_num] == 'B'):
                cnt1 += 1
            elif ((row_num + col_num)%2 == 1) and (temp_plate[row_num][col_num] == 'B') or ((row_num + col_num)%2 == 0) and (temp_plate[row_num][col_num] == 'W'):
                cnt2 += 1

    return min(cnt1, cnt2)


for i in range(row-7):
    for j in range(col-7):
        tmp = get_revision_times(i,j)
        if answer > tmp:
            answer = tmp

print(answer)
