#1181
#https://www.acmicpc.net/problem/1181

import sys

num = int(sys.stdin.readline())
words = []
for _ in range(num):
    words.append(str(sys.stdin.readline().strip()))

words = list(set(words))

words = sorted(words, key = lambda x : (len(x), x))

for i in words: print(i)
