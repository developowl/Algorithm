import sys

input = sys.stdin.readline

round = 4
N = int(input())

if N == 1:
    print(round)

elif N == 2:
    print(6)
    
else:
    dp = []

    dp.append(1)
    dp.append(1)

    for i in range(2, N + 1):
        dp.append(dp[i - 1] + dp[i - 2])

    # print(dp)
    
    round = dp[N-1] * 4 + dp[N - 2] * 2
    print(round)
