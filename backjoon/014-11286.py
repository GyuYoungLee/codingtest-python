from queue import PriorityQueue
from sys import stdin, stdout

N = int(input())
qu = PriorityQueue()

for i in range(N):
    request = int(stdin.readline())

    if request == 0:
        if qu.empty():
            stdout.write('0\n')
        else:
            abs_v, v = qu.get()
            stdout.write(str(v) + '\n')
    else:
        qu.put((abs(request), request))
