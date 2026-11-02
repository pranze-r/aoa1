graph = [
    [0, 10, 6, 5],
    [10, 0, 0, 15],
    [6, 0, 0, 4],
    [5, 15, 4, 0]
]

n = 4

distance = [999] * n
visited = [False] * n

distance[0] = 0

for _ in range(n):

    minimum = 999
    u = -1

    for i in range(n):
        if not visited[i] and distance[i] < minimum:
            minimum = distance[i]
            u = i

    if u == -1:
        break

    visited[u] = True

    # Update distances
    for v in range(n):

        if graph[u][v] != 0 and not visited[v]:

            new_distance = distance[u] + graph[u][v]

            if new_distance < distance[v]:
                distance[v] = new_distance


print("Shortest distances from vertex 0:")

for i in range(n):
    print("0 ->", i, "=", distance[i])