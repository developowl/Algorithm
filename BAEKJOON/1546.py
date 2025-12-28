import sys

input = sys.stdin.readline

N = int(input())

score = list(map(int, input().split()))

max_num = max(score)
total = 0
for i in range(N):
    score[i] = score[i]/max_num*100
    total = total + score[i]
    
print(float(total/N))
