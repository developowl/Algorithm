import sys
from collections import deque

input = sys.stdin.readline

dq = deque()

N = int(input())

for _ in range(N):
    input_command = input().split()
    
    command = int(input_command[0])
    
    if command == 1:
        dq.appendleft(input_command[1])
        
    elif command == 2:
        dq.append(input_command[1])
        
    elif command == 3:
        if dq:
            print(dq.popleft())
        else:
            print('-1')
            
    elif command == 4:
        if dq:
            print(dq.pop())
        else:
            print('-1')
            
    elif command == 5:
        print(len(dq))
        
    elif command == 6:
        if not dq:
            print('1')
        else:
            print('0')
            
    elif command == 7:
        if dq:
            print(dq[0])
        else:
            print('-1')
            
    elif command == 8:
        if dq:
            print(dq[-1])
        else:
            print('-1')
            