import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, K = map(int, input().split())

matrix = [[0] * (M + 1 for _ in range(N + 1))]
trash = []

for _ in range(K):
    row, column = map(int, input().split())
    matrix[row][column] = 1
    trash.append((row, column))

graph = [[] for _ in range(N * M + 1)]


