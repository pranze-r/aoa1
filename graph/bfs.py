from collections import deque

def bfs(graph,start):
    visited = {start}
    queue = deque([start])
    order=[]

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    return order

graph={
    0:[1,2],
    1:[0,3],
    2:[0,3],
    3:[1,2]
}
print("BFS Traversal: ",bfs(graph,0))