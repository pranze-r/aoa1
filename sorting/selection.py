def selection_sort(a):
    n= len(a)

    for i in range(n):
        min_index= i

        for j in range(i+1,n):
            if a[j]<a[min_index]:
                min_index=j
        a[i],a[min_index] = a[min_index],a[i]
    return a

test_a = [10,45,68,11,26,34,41]
print("unseorted array: ", test_a)
print("sorrted array: ", selection_sort(test_a))

