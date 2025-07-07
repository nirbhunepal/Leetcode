x = int(input("Enter a number: "))

counter = 0

temp = x

while temp > 0:
    temp = temp//10
    counter = counter + 1

answer = 0
original = x
while original > 0:
    last = original%10
    power = last**counter
    answer = answer+power
    original = original//10
    
    
print(answer)