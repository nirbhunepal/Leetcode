from collections import Counter

nums = [1, 3, 2, 2, 5, 2, 3, 7]

values = Counter(nums)



max_length = 0
counter = 0
for i in values:
    first = values[i]+1
    second = values[i]-1
    if first in values or second in values:
        counter = values[i]+values[i+1]
        if counter > max_length:
            max_length = counter
    else:
        continue

print(max_length)