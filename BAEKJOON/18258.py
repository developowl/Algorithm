import sys
from collections import deque

# push, pop, size, empty, front, back

q = deque()

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    input_command = input().split()
    
    command = input_command[0]
    
    if command == 'push':
        q.append(input_command[1])
        
    elif command == 'pop':
        if q:
            print(q.popleft())
        else:
            print("-1")
            
    elif command == 'size':
        print(len(q))
    
    elif command == 'empty':
        if not q:
            print('1')
        else:
            print('0')
        
    elif command == 'front':
        if q:
            print(q[0])
        else:
            print('-1')
        
    elif command == 'back':
        if q:
            print(q[-1])
        else:
            print('-1')
