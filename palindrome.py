string = ["b", "b", "b", "a"]

i = 0

length = len(string)

while i < length //2:
    start = string[i]
    end = string[length-i-1]
    if start != end:
        print("Isn't a palindrome")
        break
    i = i+1

else:
    print("Is a palindrome")        

