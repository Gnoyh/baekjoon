# https://www.acmicpc.net/problem/10828

import sys

n = int(sys.stdin.readline().strip())

stack = []

for _ in range(n):
    comm = sys.stdin.readline().strip()
    
    if comm == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif comm == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif comm == 'size':
        print(len(stack))
    elif comm == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    else:
        comm, num = comm.split()
        
        stack.append(int(num))