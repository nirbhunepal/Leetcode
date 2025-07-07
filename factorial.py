x = int(input("Enter a number: "))
ans = 1
for i in range(1, x):
    ans = ans*(x-i)

ans = x*ans
print(ans)
