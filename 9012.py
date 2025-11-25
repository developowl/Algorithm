import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    stack = []
    parentheses = input()

    for j in parentheses:
        if j == "(":
            stack.append(j)
        elif j == ")":
            if len(stack) != 0:
                stack.pop()
            else:
                print("NO")
                break
    else: 
        if len(stack) == 0:
            print("YES")
        else:
            print("NO")
