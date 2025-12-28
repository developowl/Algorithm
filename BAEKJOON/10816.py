from collections import Counter
import sys

input = sys.stdin.readline

N = int(input())
list1 = Counter(map(int, input().split()))

M = int(input())
list2 = map(int, input().split())

for num in list2:
    print(list1[num])
    