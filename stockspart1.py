prices = [7, 6, 4, 3, 1]

min_value = 1000

min_index = -1

for index, value in enumerate(prices):
    if value < min_value:
        min_value = value
        min_index = index

i = min_index

max_value = min_value
while i < len(prices):
    if prices[i] > max_value:
        max_value = prices[i]
    i = i+1

ans = max_value-min_value

print("The profit is: " + str(ans))