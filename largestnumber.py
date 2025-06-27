int_nums = [10, 2]


nums = [str(num) for num in int_nums]


nextup = nums[0]

for i in range(len(nums)-1):
    ans1 = nextup + nums[i+1]
    ans2 = nums[i+1]+nextup
    
    ans1_int = int(ans1)
    ans2_int = int(ans2)
        
    if ans1_int>ans2_int:
        nextup = ans1
    elif ans1_int<ans2_int:
        nextup = ans2
    else:
        nextup = ans1

print(nextup)