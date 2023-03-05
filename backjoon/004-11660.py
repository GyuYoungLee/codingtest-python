# 구간 합 구하기 2 (구간합)

from sys import stdin, stdout

n, m = map(int, stdin.readline().split())

A = [[0] * (n + 1)]
S = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    row = [0] + [int(x) for x in stdin.readline().split()]
    A.append(row)

# 합배열 만들기
for i in range(1, n + 1):
    for j in range(1, n + 1):
        S[i][j] = S[i - 1][j] + S[i][j - 1] - S[i - 1][j - 1] + A[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    result = S[x2][y2] - S[x2][y1 - 1] - S[x1 - 1][y2] + S[x1 - 1][y1 - 1]
    stdout.write(str(result) + "\n")
