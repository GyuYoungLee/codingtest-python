# 좋은 수 구하기 (투포인터)

n = int(input())
A = list(map(int, input().split()))

A.sort()

# -5 0 1 2 3 =>  -5 + 3 = 2 (good), 0 + 1 = 1 (X)
count = 0

for k in range(n):
    i = 0
    j = n - 1

    # 투 포인터 알고리즘
    while i < j:
        if A[i] + A[j] > A[k]:
            j -= 1
        elif A[i] + A[j] < A[k]:
            i += 1
        else:
            if i == k:
                i += 1
            elif j == k:
                j -= 1
            else:
                count += 1
                break

print(count)
