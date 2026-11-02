def dfs(graph, node, visited=None, order=None):
    if visited is None:
        visited, order = set(), []
    visited.add(node)
    order.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, order)
    return order

graph = {
0: [1, 2],
1: [0, 3],
2: [0, 3],
3: [1, 2]
}
print("DFS Traversal:", dfs(graph, 0))