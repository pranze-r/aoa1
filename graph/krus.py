edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]


edges.sort(key=lambda x: x[2])

parent = [0, 1, 2, 3]


def find(x):
    while parent[x] != x:
        x = parent[x]
    return x


result = []
total = 0

for u, v, weight in edges:

    a = find(u)
    b = find(v)

    if a != b:
        result.append((u, v, weight))
        total += weight
        parent[a] = b

    if len(result) == 3:
        break


print("Edges in Minimum Spanning Tree:")

for u, v, weight in result:
    print(u, "--", v, "=", weight)

print("Total Cost:", total)