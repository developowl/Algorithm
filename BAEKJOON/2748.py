import sys

input = sys.stdin.readline

n = int(input())

dp = []
dp.append(0)
dp.append(1)

for i in range(2, n+1):
    dp.append(dp[i-1] + dp[i-2])

print(dp[n])

# 오답 분석: 기존 재귀 함수(fibo 함수 사용)의 경우 이전 수열의 값을
# 재사용할 때마다 "또" 연산을 하는 문제 발생. dp의 경우 이전에 계산한 결과를 배열에 저장함으로 이를 해결
