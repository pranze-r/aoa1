universe = {1, 2, 3, 4, 5}

sets = {
    "S1": {1, 2, 3},
    "S2": {2, 4},
    "S3": {3, 4, 5},
    "S4": {5}
}

uncovered = set(universe)
selected = []

while uncovered:

    best_set = max(
        sets,
        key=lambda s: len(sets[s] & uncovered)
    )

    selected.append(best_set)

    uncovered -= sets[best_set]

    del sets[best_set]

print("Selected sets:", selected)
print("All elements are covered.")