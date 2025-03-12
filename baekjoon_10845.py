# https://www.acmicpc.net/problem/10845

from collections import deque
import sys

n = int(sys.stdin.readline().strip())

queue = deque()

for _ in range(n):
    comm = sys.stdin.readline().strip()
    
    if comm == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif comm == "size":
        print(len(queue))
    elif comm == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif comm == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif comm == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
    else:
        comm, num = comm.split()
        
        queue.append(int(num))