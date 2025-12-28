import sys

input = sys.stdin.readline

N = int(input())

liquid = list(map(int, input().split()))

min_sum = liquid[0] + liquid[-1]
a = liquid[0]
b = liquid[-1]

for i in range(len(liquid) // 2):
    sum = liquid[i] + liquid[-(i + 1)]

    if min_sum > abs(sum):
        min_sum = abs(sum)
        a = liquid[i]
        b = liquid[-(i + 1)]

print(a, b)
