import sys

input = sys.stdin.readline


def kantour(n):
    if n == 0:
        return "-"

    side = kantour(n - 1)
    center = " " * len(side)
    
    return side + center + side

while 1:
    try:
        n = int(input())
        
        print(kantour(n))
    except:
        break
