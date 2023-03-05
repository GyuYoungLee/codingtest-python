# 구간 합 구하기 (구간합)

from sys import stdin, stdout

n, m = map(int, stdin.readline().split())
numbers = list(map(int, stdin.readline().split()))

S = [0]

# 합배열 만들기
for x in numbers:
    S.append(S[-1] + x)

for _ in range(m):
    start, end = map(int, stdin.readline().split())
    stdout.write(str(S[end] - S[start - 1]) + "\n")
