def fibonnaci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    ans = fibonnaci(n-1)+fibonnaci(n-2)
    return ans
    

a = fibonnaci(7)
print(a)