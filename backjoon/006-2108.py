# 연속된 자연수의 합 구하기 (투포인터)

n = int(input())

start = 1
end = 1
total = 1
count = 1

while end != n:
    if total < n:
        end += 1
        total += end
    elif total > n:
        total -= start
        start += 1
    else:
        end += 1
        total += end
        total -= start
        start += 1
        count += 1

print(count)
