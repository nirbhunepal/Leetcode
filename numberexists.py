def find_number(nums, number):
    if len(nums) == 0:
        return -1
    middle = len(nums)//2
    
    if len(nums) == 1 and nums[0] != number:
        return -1
    
    if nums[middle] == number:
        return number
    
    
    index = nums[middle]
    
    if index > number:
        nums = nums[0:middle]
        return find_number(nums, number)
    else:
        nums = nums[middle:]
        return find_number(nums, number)
    
    
    

nums = [1, 3, 4, 7, 9, 10]
a = find_number(nums, 7)
print(a)