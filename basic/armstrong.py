n = 1634
num = n
num2 = n
count = 0
sum = 0

while num > 0:
    count += 1
    num = num // 10

while num2 > 0:
    # last digit
    last_digit = num2 % 10
    sum = sum + (last_digit ** count)

    num2 = num2 // 10

print(sum)
    