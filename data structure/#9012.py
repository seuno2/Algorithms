#9012
#https://www.acmicpc.net/problem/9012

num = int(input())
strings = []
for _ in range(num):
    st = input()
    strings.append(st)

for row in strings:
    stack = []

    for p in row:
        if p=='(':
            stack.append(p)
        elif p==')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if not stack:
            print('YES')
        else:
            print('NO')
