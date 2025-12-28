import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
connect = int(input())

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
count = 0

for _ in range(connect):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(v):
    global count
    visited[v] += 1

    for next in graph[v]:
        if visited[next] == 0:
            count += 1
            dfs(next)


dfs(1)

print(count)
