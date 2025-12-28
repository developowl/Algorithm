import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
order = 1

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(v):
    global order
    visited[v] = order
    graph[v].sort()

    for next in graph[v]:
        if visited[next] == 0:
            order += 1
            dfs(next)


dfs(r)

for i in range(n):
    print(visited[i + 1])
