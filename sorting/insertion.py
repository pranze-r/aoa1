def insertion_sort(a):
    for i in range(1,len(a)):
        key=a[i]
        j=i-1

        while j>=0 and a[j]>key:
            a[j+1]=a[j]
            j-=1

        a[j+1]=key     
    return a

test_a= [10,45,68,11,26,34,41]
print("Unsorted array:", test_a) 
sorted_numbers = insertion_sort(test_a) 
print("Sorted array:", sorted_numbers) 

    
