def myadd(c):
    global checkArr, myArr, checkSecret
    if c == 'A':
        myArr[0] += 1
        if myArr[0] == checkArr[0]:
            checkSecret += 1
    elif c == 'C':
        myArr[1] += 1
        if myArr[1] == checkArr[1]:
            checkSecret += 1
    elif c == 'G':
        myArr[2] += 1
        if myArr[2] == checkArr[2]:
            checkSecret += 1
    elif c == 'T':
        myArr[3] += 1
        if myArr[3] == checkArr[3]:
            checkSecret += 1


def myremove(c):
    global checkArr, myArr, checkSecret
    if c == 'A':
        myArr[0] -= 1
        if myArr[0] == (checkArr[0] - 1):
            checkSecret -= 1
    elif c == 'C':
        myArr[1] -= 1
        if myArr[1] == (checkArr[1] - 1):
            checkSecret -= 1
    elif c == 'G':
        myArr[2] -= 1
        if myArr[2] == (checkArr[2] - 1):
            checkSecret -= 1
    elif c == 'T':
        myArr[3] -= 1
        if myArr[3] == (checkArr[3] - 1):
            checkSecret -= 1


S, P = map(int, input().split())
A = list(input())

checkArr = list(map(int, input().split()))
myArr = [0] * 4
checkSecret = 0
count = 0

# checkSecret 초기화
for i in range(4):
    if checkArr[i] == 0:
        checkSecret += 1

# myArr 초기화
for i in range(P):
    myadd(A[i])

if checkSecret == 4:
    count += 1

# 슬라이딩
for i in range(P, S):
    myadd(A[i])
    myremove(A[i - P])

    if checkSecret == 4:
        count += 1

print(count)
