n=int(input("Enter the number of elements: "))
print("Enter the element: ")
arr=list(map(int(input().split())))

k=int(input("Enter the value of k: "))

arr.sort()
print("Sorted array: ", arr)
print("K smallest: ")
print("K largest value: ")
choice= int(input("Enter your choice (1 or 2 ): "))

if choice==1:
    print(k," th smallest element ",arr[k-1])
elif choice==2:
    print(k," th Largest element ",arr[n-1])
else:
    print("Invalid choice ")


