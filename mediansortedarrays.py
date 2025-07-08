nums1 = [1, 2]
nums2 = [3, 4]
comb_nums = nums1+nums2
length = len(comb_nums)
half = length//2

swapped = True

while swapped:
    swapped = False
    for i in range(len(comb_nums)-1):
        if comb_nums[i] > comb_nums[i+1]:
            comb_nums[i], comb_nums[i+1] = comb_nums[i+1], comb_nums[i]
            swapped = True
        else:
            continue
        
print(comb_nums)

if length%2 == 0:
    a = comb_nums[half]
    b = comb_nums[half-1]
    median = (a+b)/2
else:
    median = comb_nums[half]
        
print("The median of the sorted arrays are: " + str(median))
