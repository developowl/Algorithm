import sys

input = sys.stdin.readline

# B -> BA
# A -> B

dp_A = []
dp_B = []

K = int(input())

dp_A.append(1)
dp_A.append(0)

dp_B.append(0)
dp_B.append(1)

if K == 1:
    print('0 1')
elif K == 2:
    print('1 0')
else:
    for i in range(2, K+1):
        dp_A.append(dp_A[i-1] + dp_A[i-2])
        dp_B.append(dp_B[i-1] + dp_B[i-2])
        
        
    # print("A:", dp_A)
    # print("B:", dp_B)
    
    print(dp_A[K], dp_B[K])

