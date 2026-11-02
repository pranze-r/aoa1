graph = [
    [0, 10, 6, 5],
    [10, 0, 0, 15],
    [6, 0, 0, 4],
    [5, 15, 4, 0]
]

n = 4

visited = [False] * n
visited[0] = True

result = []
total = 0

for _ in range(n - 1):

    minimum = 999
    x = y = 0

    for i in range(n):
        if visited[i]:

            for j in range(n):

                if not visited[j] and graph[i][j] != 0:

                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x = i
                        y = j

    result.append((x, y, minimum))
    total += minimum

    visited[y] = True


print("Edges in Minimum Spanning Tree:")

for x, y, weight in result:
    print(x, "--", y, "=", weight)

print("Total Cost:", total)