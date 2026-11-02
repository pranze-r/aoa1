numbers = [3, 5, 7, 10, 12]

target = 15

numbers.sort(reverse=True)

subset = []
total = 0

for num in numbers:

    if total + num <= target:
        subset.append(num)
        total += num

print("Numbers:", numbers)
print("Target:", target)
print("Selected subset:", subset)
print("Subset sum:", total)