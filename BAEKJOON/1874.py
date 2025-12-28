n = int(input())
stack = []
answer = []

now = 1
flag = True
for _ in range(n):
    num = int(input())
    
    while now <= num:
        stack.append(now)
        answer.append("+")
        now += 1
    
    if stack[-1] == num:
        stack.pop()
        answer.append("-")
        
    else:
        flag = False # 불가능한 경우
    
if not flag: # flag == False
    print("NO")
else:
    for symbol in answer:
        print(symbol)
