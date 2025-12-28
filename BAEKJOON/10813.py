import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = []

for i in range(1, N + 1):
    arr.append(i)
    
for _ in range(M):
    a, b = map(int, input().split())
    
    temp = arr[a-1]
    arr[a-1] = arr[b-1]
    arr[b-1] = temp
    
# print("".join(arr))
# join -> str에 사용 가능
print(" ".join(map(str, arr)))
