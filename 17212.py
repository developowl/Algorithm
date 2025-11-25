import sys

input = sys.stdin.readline

# dp[0] -> 7원 개수
# dp[1] -> 5won
# dp[2] -> 3won
# dp[3] -> 2won
# dp[4] -> 1won

N = int(input())

dp = []

dp.append(N // 7)
N = N % 7
dp.append(N // 5)
N = N % 5
dp.append(N // 2)
N = N % 2
dp.append(N)

print(dp[0]+dp[1]+dp[2]+dp[3])

# ----- 예외는 뭘까

N = int(input())
dp = [0 for i in range(N + 1)]

for i in range(1, N + 1):
    if i >= 7:
        dp[i] = min(dp[i - 1], dp[i - 2], dp[i - 5], dp[i - 7]) + 1
    elif i >= 5:
        dp[i] = min(dp[i - 1], dp[i - 2], dp[i - 5]) + 1
    elif i >= 2:
        dp[i] = min(dp[i - 1], dp[i - 2]) + 1
    else:
        dp[i] = dp[i - 1] + 1
print(dp[N])
