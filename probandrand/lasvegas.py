import random

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return randomized_quicksort(left) + middle + randomized_quicksort(right)

arr = [12, 5, 8, 19, 3, 15, 7]

print("Original Array:", arr)
sorted_arr = randomized_quicksort(arr)
print("Sorted Array:", sorted_arr)
