# https://www.acmicpc.net/problem/1260

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for neighbor in sorted(graph[start]):
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

# 입력 처리
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS 실행
visited = [False] * (n + 1)
dfs(graph, v, visited)
print()