x = int(input("Enter a number: "))
ans = [int(digit) for digit in str(x)]

add = ['']

while len(ans)>1:
    y = sum(ans)
    add.append(y)
    temp = [int(digit) for digit in str(y)]
    ans = temp

print(ans)