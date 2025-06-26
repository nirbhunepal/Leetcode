num1 = [2, 4, 0]
num2 = [6, 7]

while len(num1) != len(num2):
    if len(num1) < len(num2):
        num1.insert(0, 0)
    else:
        num2.insert(0, 0)

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
