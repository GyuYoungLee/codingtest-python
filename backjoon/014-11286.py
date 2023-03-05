# 절대값 힙 구현하기 (우선순위큐)

from queue import PriorityQueue
from sys import stdin, stdout

N = int(input())
pqu = PriorityQueue()

for i in range(N):
    request = int(stdin.readline())

    if request == 0:
        if pqu.empty():
            stdout.write('0\n')
        else:
            abs_v, v = pqu.get()
            stdout.write(str(v) + '\n')
    else:
        pqu.put((abs(request), request))  # (1차기준, 2차기준)
