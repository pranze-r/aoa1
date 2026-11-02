n = int(input("Enter the number of elements: "))

print("Enter the elements:")
arr = list(map(int, input().split()))

print("Original Array:", arr)

max_num = max(arr)
exp = 1

while max_num // exp > 0:
    output = [0] * len(arr)
    count = [0] * 10

    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    arr = output
    exp *= 10
print("Sorted Array: ",arr)