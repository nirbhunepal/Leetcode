def sum_n(n):
    if n == 0:
        return 0
    last = n%10
    n = n//10
    answer = last + sum_n(n)
    return answer

a = sum_n(123)
print(a)