import random
n= 10

canditates=list(range(1,n+1))
random.shuffle(canditates)

best = float('inf')
hires=0

print("Candidates order: ", canditates)

for i in range(n):
    print(f"Interview candidate rank : {canditates[i]}")

    if canditates[i]<best:
        best = canditates[i]
        hires+=1
        print(" -> hired")
    else:
        print(" -> rejected")

print("\nTotal interviews = ", n)
print("Total Hires = ",hires)
