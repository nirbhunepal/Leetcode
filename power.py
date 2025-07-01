x = int(input("Enter a number: "))
n = int(input("Enter another number: "))

ans = 1

for i in range(n):
    ans = x*ans
    
print(ans)