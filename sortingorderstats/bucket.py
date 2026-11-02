n=int(input("Enter the number of elements: "))

print("Enter the elemetns")
arr = list(map(int,input().split()))

print("Orignal Array: ",arr)

max_num=max(arr)
bucket=[]

for i in range(max_num+1):
    bucket.append(0)


for i in arr:
    bucket[i]+=1
sorted_arr=[]

for i in range(len(bucket)):
    while bucket[i]>0:
        sorted_arr.append(i)
        bucket[i]-=1

print("Sorted Array: ",sorted_arr)