def climb_stairs(x):
    if x == 0 or x == 1:
        return 1

    two = x-2
    one = x-1
    ans = climb_stairs(two)+climb_stairs(one)
    
    return ans


a = climb_stairs(4)
print(a)