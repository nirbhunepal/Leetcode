num1 = [2, 4, 3]
num2 = [5, 7, 8]

final = []

carry = 0

length = len(num1)

i = 1

while i <= length:
    ans: int = carry+num1[length-i]+num2[length-i]
    if ans > 9:
        carry = ans // 10
        ans = ans%10
        

    final.insert(0, ans)
    i = i+1


print(final)