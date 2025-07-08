nums = [2, 12, 5, 9, 7, 2]
swapped = True
while swapped:
    swapped = False
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            swapped = True
        else:
            continue

print(nums)