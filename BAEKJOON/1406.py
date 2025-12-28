import sys

input = sys.stdin.readline

text = input().strip()

left_stack = list(text) # 커서 왼쪽
right_stack = [] # 커서 오른쪽

N = int(input())

for i in range(N):
    command = input().split()
    cmd = command[0]
    
    if cmd == "L":
        if left_stack:
            right_stack.append(left_stack.pop())
            
    elif cmd == "D":
        if right_stack:
            left_stack.append(right_stack.pop())
            
    elif cmd == "B":
        if left_stack:
            left_stack.pop()
            
    elif cmd == "P":
        char_to_add = command[1]
        left_stack.append(char_to_add)
        
result = "".join(left_stack + right_stack[::-1])
print(result)
