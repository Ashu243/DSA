
# this checks all the numbers upto n

# n = 10
# factors = []
# for i in range(1, n+1):
#     if(n % i == 0):
#         factors.append(i)

# print(factors)

# more optimised code
# if we are calculating factors of 20 then if we divide it in half --> 10 --> we will see that there is not any numbers that are divisilbe by 20


# n = 20
# factors = []
# for i in range(1, (n // 2) + 1):
#     if(n % i == 0):
#         factors.append(i)


# factors.append(n)
# print(factors)


# optimal code

n = 25
factors = []

for i in range(1, int((n ** .5))+1):
    if(n % i == 0):
        factors.append(i)
        if(n // i != i):
            factors.append(n//i)

print(factors)