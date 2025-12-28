import sys

input = sys.stdin.readline

stack = []

N = int(input())

# 1.push / 2.pop[-1] / 3.count / 4.isEmpty / 5.pop

for _ in range(N):
    input_command = input().split()

    command = int(input_command[0])

    # 1.push
    if command == 1:
        stack.append(input_command[1])
    
    # 2. 정수가 있다면 맨 위의 정수를 빼고 출력. 없다면 -1을 출력
    elif command == 2:
        if stack:
            print(stack.pop())
        else: print(-1)

    # 3. conut
    elif command == 3:
        print(len(stack))
    
    # 4. isEmpty
    elif command == 4:
        if stack:
            print(0)
        else:
            print(1)

    # 5. print top([-1])
    elif command == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)
