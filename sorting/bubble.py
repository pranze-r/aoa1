def bubble_sort(a):
    n=len(a)

    for i in range(n):
        swapped=False

        for j in range(0,n-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                swapped=True
        if not swapped:
            break
        return a

test_a = [10,45,68,11,26,34,41]
print("unseorted array: ", test_a)
print("sorrted array: ", bubble_sort(test_a))


    

    


