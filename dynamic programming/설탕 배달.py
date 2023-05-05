#2839
#https://www.acmicpc.net/problem/2839

import math
sugar = int(input())

max_three = math.ceil(sugar / 3)
max_five = math.ceil(sugar / 5)
three, five = 0, max_five

while three <= max_three:
    if (five*5 + three*3) == sugar:
        print(three + five)
        break
    elif (five*5 + three*3) > sugar:
        five -= 1
        three += 1
    elif (five*5 + three*3) < sugar:
        three += 1

else:
    print(-1)
