a = int(input("Enter a number: "))
x = 1
diff = a-x
while abs(diff) > 0.001:
    ans = (x+(a/x))/2
    diff = ans-x
    x = ans
print(x)
    