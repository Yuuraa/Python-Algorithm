from collections import deque


# graph: 2D integer list. graph[i] containes all index of adjacent nodes of node i
# v: starting node
def dfs(graph, v):
    visited = [False for i in range(len(graph))]
    stack = deque([v])
    visited[v] = True

    while stack:
        root = stack.pop()
        print(root)
        for i in graph[root][::-1]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)


def dfs_recursive(graph, visited, v):
    visited[v] = True
    print(v)
    for i in graph[v]:
        if not visited[i]:
            dfs_recursive(graph, visited, i)


def bfs(graph, v):
    visited = [False for i in range(len(graph))]
    queue = deque([v])
    visited[v] = True
    while queue:
        root = queue.popleft()
        print(root)
        for i in graph[root]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


if __name__ == '__main__':
    graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
    ]
    print("DFS")
    dfs(graph, 1)

    print("Recursive DFS")
    visited = [False for i in range(len(graph))]
    dfs_recursive(graph, visited, 1)

    print("BFS")
    bfs(graph, 1)