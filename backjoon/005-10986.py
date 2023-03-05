n, m = map(int, input().split())

A = [0] + list(map(int, input().split()))
S = [0] * (n + 1)
C = [0] * m

# A: 0, 1, 2, 3, 1, 2
# S: 0, 1, 3, 6, 7, 9
for i in range(1, n + 1):
    S[i] = S[i - 1] + A[i]

# S: 0, 1, 0, 0, 1, 0
for i in range(n + 1):
    remainder = S[i] % m
    C[remainder] += 1

answer = 0
for i in range(m):
    answer += C[i] * (C[i] - 1) // 2

print(answer)
