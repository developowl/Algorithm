import sys

input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    arr.append(input().rstrip().split())


def paper_divide(x, y, n):
    now_num = arr[x][y]
    isDivide = False
    
    for i in range(x, x + n):
        for j in range(y, y + n):
            if now_num != arr[i][j]:
                isDivide = True
                break
        if isDivide:
            break

    if isDivide:
        # [minus_one, zero, plus_one]
        counts = [0, 0, 0]
        
        for k in range(3):
            for l in range(3):
                count = paper_divide((x + k * n // 3), (y + l * n // 3), (n // 3))
                
                counts[0] += count[0]
                counts[1] += count[1]
                counts[2] += count[2]
        return counts

    else:
        if now_num == '-1':
            return [1, 0, 0]
        elif now_num == '0':
            return [0, 1, 0]
        else:
            return [0, 0, 1]

final_counts = paper_divide(0, 0, N)

print(final_counts[0])
print(final_counts[1])
print(final_counts[2])

# 드디어 끝,,,,,,,,, 몇시간을 푼거야..
