n = int(input())
scores = list(map(int, input().split()))

score_sum = sum(scores)
score_max = max(scores)

print(score_sum * 100 / n / score_max)
