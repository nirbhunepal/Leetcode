a = input("Enter a string of numbers from digits 2-9: ")
a = list(a)

ans = ['']


letters = {
    '2': "abc",
    '3': "def",
    '4': "ghi",
    '5': "jkl",
    '6': "mno",
    '7': "pqrs",
    '8': "tuv",
    '9': "wxyz"
    }
    
for i in a:
    l = letters[i]
    list = []
    for k in ans:  
        for j in l:
            list.append(k + j)
    ans = list


print(ans)