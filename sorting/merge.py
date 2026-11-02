def merge_sort(a):
    if len(a)<=1:
        return a
    midd = len(a)//2
    
    left_side=a[:midd]
    right_side=a[midd:]

    left_sorted= merge_sort(left_side)
    right_sorted= merge_sort(right_side)

    def merge(left,right):
        sorted_array=[]
        i=j=0

        while i<len(left) and j <len(right):
            if left[i]<right[j]:
                sorted_array.append(left[i])
                i+=1
            else:
                sorted_array.append(right[j])
                j+=1

        sorted_array.extend(left[i:])
        sorted_array.extend(right[j:])

        return sorted_array
    return merge(left_sorted, right_sorted)

test_a=[10,45,68,11,26,34,41]
print("unsorted array: ",test_a)
print("sorted array: ",merge_sort(test_a))



