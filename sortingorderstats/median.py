n1 = int(input("Enter the number of elements in Array 1: "))
print("Enter the elements of Array 1:")
arr1 = list(map(int, input().split()))

n2 = int(input("Enter the number of elements in Array 2: "))
print("Enter the elements of Array 2:")
arr2 = list(map(int, input().split()))
# Merge and sort the two 
# arrays
arr = arr1 + arr2
arr.sort()

print("Merged Sorted Array:", arr)
n = len(arr)
# Calculate the median
if n % 2 == 1:
    median = arr[n // 2]
else:
    median = (arr[n // 2 - 1] + arr[n // 2]) / 2

print("Median:", median)