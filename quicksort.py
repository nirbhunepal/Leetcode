nums = [6, 7, 1, 3, 9, 5]


def sort(nums):
    first = nums[0]
    left = []
    right = []
    for i in nums[1:]:
        if i < first:
            left.append(i)
        else:
            right.append(i)
            
    return sort(left)+[first]+sort(right)
    
    
    
    
a = sort(nums)
print(a)
