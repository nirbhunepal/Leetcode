nums = [3, 6, 9, 1]

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

diff = 0
for i in range(len(nums)-1):
    a = nums[i]
    b = nums[i+1]
    ans = b-a
    
    if ans > diff:
        diff = ans
    else:
        continue

print("The highest difference between adjacent elements is: " + str(diff))   
