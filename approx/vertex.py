edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("B", "D"),
    ("C", "D")
]

cover = []

while edges:

    u, v = edges[0]

    cover.append(u)
    cover.append(v)

    edges = [
        edge for edge in edges
        if u not in edge and v not in edge
    ]

print("Vertex Cover:", cover)
print("Number of vertices:", len(cover))