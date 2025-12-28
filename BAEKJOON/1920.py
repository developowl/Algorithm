import sys

input = sys.stdin.readline

N = int(input())

list1 = set(map(int, input().split()))

M = int(input())

list2 = map(int, input().split())

for num in list2:
    if num in list1:
        print(1)
    else:
        print(0)
