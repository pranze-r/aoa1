def quick_sort(a):
    if len(a)<=1:
        return a

    pivot=a[-1]

    left=[x for x in a[:-1] if x<pivot]
    middle=[x for x in a [:-1] if x==pivot]
    right=[x for x in a[:-1] if x>pivot]
    return quick_sort(left)+middle+quick_sort(right)

test_a=[10,45,68,11,26,34,41]
print("unsorted: ",test_a)
print("sorted: ",quick_sort(test_a))
