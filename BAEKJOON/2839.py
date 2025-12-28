import sys

input = sys.stdin.readline

# only 3kg, 5kg
count = 0

N = int(input())

while N >= 0:
    if N % 5 == 0:
        count += N //5
        print(count)
        break
    
    N -= 3
    count += 1

else:
    print(-1)

        
        