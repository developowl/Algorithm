import sys

input = sys.stdin.readline

N, M = map(int, input().split())

times = list(map(int, input().split()))

short = 0
long = max(times) * M
result = long

while short <= long:
    mid = (short + long) // 2

    total = 0

    for time in times:
        total += mid // time

        if total >= M:
            break

    if total >= M:
        result = mid
        long = mid - 1
    else:
        short = mid + 1

print(result)
