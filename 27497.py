import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

result_deque = deque() 
history_stack = [] # 두 번 연속 삭제하는 경우 오류가 발생했음(이전 제출) -> 입력값들의 위치(position)를 기록하는 스택 생성

for _ in range(N):
    command = list(input().split())
    
    if not command:
        continue
    
    command_type = command[0]

    if command_type == '1':
        result_deque.append(command[1])
        history_stack.append('R')

    elif command_type == '2':
        result_deque.appendleft(command[1])
        history_stack.append('L')
    
    elif command_type == '3':
        if not history_stack:
            continue
        
        last_added_position = history_stack.pop() 
        
        if result_deque: 
            if last_added_position == 'R':
                result_deque.pop()
            elif last_added_position == 'L':
                result_deque.popleft()

if not result_deque:
    print(0)
    
else:
    print("".join(result_deque))
